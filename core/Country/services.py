import json
import requests
from requests.exceptions import Timeout, HTTPError
from collections import Counter

from django.db.models import QuerySet
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _

from .const import DEFAULT_FIXTURE, EXTERNAL_API_DOCUMENTATION_URL, EXTERNAL_API_URL
from .models import Country


class LoadCountriesException(Exception):
    pass


def run_validations(data: list[dict]):
    ccn3_list: list[str] = [x['ccn3'] for x in data]
    duplicated = [item for item, count in Counter(ccn3_list).items() if count > 1]
    if duplicated:
        msg = _('Duplicated CCN3 codes presented: {duplicated}').format(duplicated=', '.join(duplicated))
        raise LoadCountriesException(msg)

    cca2_list: list[str] = [x['cca2'] for x in data]
    duplicated = [item for item, count in Counter(cca2_list).items() if count > 1]
    if duplicated:
        msg = _('Duplicated CCA2 codes presented: {duplicated}').format(duplicated=', '.join(duplicated))
        raise LoadCountriesException(msg)


@atomic
def import_countries_from_fixture(archive_not_mentioned: bool = True, fixture: str = DEFAULT_FIXTURE,
                                  data: list[dict] = None) -> QuerySet[Country]:
    mentioned: set[int] = set()
    if not data:
        data = json.load(open(fixture, 'r'))

    run_validations(data=data)

    for item in data:
        obj, _ = Country.objects.update_or_create(
            ccn3=item['ccn3'],
            defaults={
                'cca2': item['cca2'],
                'name': item['name']['common'],
            }
        )
        mentioned.add(obj.id)
        if not obj.is_active:
            obj.restore()

    if archive_not_mentioned:
        Country.objects.exclude(id__in=mentioned).archive()
    return Country.objects.filter(id__in=mentioned)


def import_countries_from_external_api(fields: tuple = ('name', 'ccn3', 'cca2')) -> QuerySet[Country]:
    if not fields:
        raise LoadCountriesException(f'Please, specify fields to get. Documentation: {EXTERNAL_API_DOCUMENTATION_URL}')

    try:
        response = requests.get(url=EXTERNAL_API_URL, params={'fields': fields}, timeout=15)
        response.raise_for_status()
    except Timeout as e:
        raise LoadCountriesException(f'Timeout: {str(e)}')
    except HTTPError as e:
        raise LoadCountriesException(f'HTTPError status is not succeeded: {str(e)}')

    try:
        data = response.json()
    except Exception as e:
        raise LoadCountriesException(f'Unable to load data from countries API: {str(e)}')

    return import_countries_from_fixture(data=data, archive_not_mentioned=False)
