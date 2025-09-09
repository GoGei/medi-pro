import django_tables2 as tables
from django.utils.translation import gettext_lazy as _
from Admin.utils.tables import fields as custom_fields
from core.ClinicPreSettings.models import ClinicPreSettings


class ClinicPreSettingsTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='clinic-settings:clinic-pre-settings-view')
    country = custom_fields.HrefColumn(verbose_name=_('Country'),
                                       reverse_url='handbooks:country-view',
                                       reverse_field='country_id',
                                       record_label='country')
    timezones = custom_fields.ManyToManyHrefColumn(verbose_name=_('Timezones'),
                                                   reverse_url='handbooks:timezones-view',
                                                   related_qs_param='timezones',
                                                   item_label='label')
    primary_timezone = custom_fields.HrefColumn(verbose_name=_('Primary timezone'),
                                                reverse_url='handbooks:timezones-view',
                                                reverse_field='primary_timezone_id',
                                                record_label='primary_timezone')
    currencies = custom_fields.ManyToManyHrefColumn(verbose_name=_('Currencies'),
                                                    reverse_url='handbooks:currency-view',
                                                    related_qs_param='currencies',
                                                    item_label='label')
    primary_currency = custom_fields.HrefColumn(verbose_name=_('Primary currency'),
                                                reverse_url='handbooks:currency-view',
                                                reverse_field='primary_currency_id',
                                                record_label='primary_currency')
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(base_url='clinic-settings:clinic-pre-settings')

    class Meta:
        model = ClinicPreSettings
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'country', 'timezones', 'primary_timezone', 'currencies', 'primary_currency', 'is_active',
                  'actions')
        ordering_fields = ('id',)
