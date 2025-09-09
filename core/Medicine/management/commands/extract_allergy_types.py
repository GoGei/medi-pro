from django.db.transaction import atomic
from django.core.management.base import BaseCommand, CommandError

from core.Loggers.models import HandbookUpdateLog
from core.Medicine.enums import MedicineHandbookSources
from core.Medicine.extractors.hl7 import FHIRPageExtractor, FHIRPageExtractorException
from core.Medicine.models import AllergyType


class Command(BaseCommand):
    help = 'Load allergy types (Allergy intolerance categories) from HL7 FHIR'
    default_url = 'https://hl7.org/fhir/valueset-allergy-intolerance-category.html'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            help='URL to https://hl7.org/',
        )
        parser.add_argument(
            '--user_id',
            type=int,
            help='Optional user ID',
        )

    def handle(self, *args, **options):
        extractor = FHIRPageExtractor(options.get('url') or self.default_url)

        try:
            extractor.get_content()
        except FHIRPageExtractorException as e:
            raise CommandError(f'Unable to get content from page: {e}')

        try:
            extractor.extract_from_table()
            HandbookUpdateLog.objects.create(user_id=options.get('user_id'),
                                             handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_TYPE)
        except FHIRPageExtractorException as e:
            raise CommandError(f'Unable to extract data from table: {e}')
        except Exception as e:
            raise CommandError(f'Unknown error: {e}')

        self.stdout.write(self.style.SUCCESS(f'Successfully received {len(extractor.data)} items'))
        try:
            self.update_allergy_types(extractor)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unable to update allergy types: {e}'))

    @atomic
    def update_allergy_types(self, extractor: FHIRPageExtractor):
        batch_size = 200
        updated_count = created_count = total_count = 0
        allergy_types_to_create: list[AllergyType] = list()
        allergy_types_to_update: list[AllergyType] = list()
        fields = ('name', 'source')
        for item in extractor.data:
            allergy_item = {
                'source': MedicineHandbookSources.HL7,
                'name': item['display'],
                'code': item['code'],
            }
            try:
                obj = AllergyType.objects.get(code=allergy_item['code'])
                for field, value in allergy_item.items():
                    setattr(obj, field, value)
                allergy_types_to_update.append(obj)
                updated_count += 1
            except AllergyType.DoesNotExist:
                allergy_types_to_create.append(AllergyType(**allergy_item))
                created_count += 1
            total_count += 1
            if total_count % batch_size == 0:
                self.stdout.write(f'Processed {total_count} allergy types')

            if len(allergy_types_to_create) == batch_size:
                AllergyType.objects.bulk_create(allergy_types_to_create)
                allergy_types_to_create = list()
            if len(allergy_types_to_update) == batch_size:
                AllergyType.objects.bulk_update(allergy_types_to_update, fields=fields)
                allergy_types_to_update = list()

        if allergy_types_to_create:
            AllergyType.objects.bulk_create(allergy_types_to_create)
        if allergy_types_to_update:
            AllergyType.objects.bulk_update(allergy_types_to_update, fields=fields)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} allergy types'))
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} allergy types'))
