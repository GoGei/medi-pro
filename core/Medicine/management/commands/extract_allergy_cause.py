from django.db.transaction import atomic
from django.core.management.base import BaseCommand, CommandError

from core.Medicine.enums import MedicineHandbookSources
from core.Medicine.extractors.hl7 import FHIRPageExtractor, FHIRPageExtractorException
from core.Medicine.models import AllergyCause


class Command(BaseCommand):
    help = 'Load allergy causes (Allergy intolerance codes) from HL7 FHIR'
    default_url = 'https://hl7.org/fhir/valueset-allergyintolerance-code.html'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            help='URL to https://hl7.org/',
        )

    def handle(self, *args, **options):
        extractor = FHIRPageExtractor(options.get('url') or self.default_url)

        try:
            extractor.get_content()
        except FHIRPageExtractorException as e:
            raise CommandError(f'Unable to get content from page: {e}')

        try:
            extractor.extract_from_table()
        except Exception as e:
            raise CommandError(f'Unable to extract data from table: {e}')

        self.stdout.write(self.style.SUCCESS(f'Successfully received {len(extractor.data)} items'))
        try:
            self.update_allergy_causes(extractor)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unable to update allergy causes: {e}'))

    @atomic
    def update_allergy_causes(self, extractor: FHIRPageExtractor):
        batch_size = 200
        updated_count = created_count = total_count = 0
        allergy_causes_to_create: list[AllergyCause] = list()
        allergy_causes_to_update: list[AllergyCause] = list()
        fields = ('name', 'source')
        for item in extractor.data:
            allergy_item = {
                'source': MedicineHandbookSources.HL7,
                'name': item['display'],
                'code': item['code'],
            }
            try:
                obj = AllergyCause.objects.get(code=allergy_item['code'])
                for field, value in allergy_item.items():
                    setattr(obj, field, value)
                allergy_causes_to_update.append(obj)
                updated_count += 1
            except AllergyCause.DoesNotExist:
                allergy_causes_to_create.append(AllergyCause(**allergy_item))
                created_count += 1
            total_count += 1
            if total_count % batch_size == 0:
                self.stdout.write(f'Processed {total_count} allergy causes')

            if len(allergy_causes_to_create) == batch_size:
                AllergyCause.objects.bulk_create(allergy_causes_to_create)
                allergy_causes_to_create = list()
            if len(allergy_causes_to_update) == batch_size:
                AllergyCause.objects.bulk_update(allergy_causes_to_update, fields=fields)
                allergy_causes_to_update = list()

        if allergy_causes_to_create:
            AllergyCause.objects.bulk_create(allergy_causes_to_create)
        if allergy_causes_to_update:
            AllergyCause.objects.bulk_update(allergy_causes_to_update, fields=fields)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} allergy causes'))
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} allergy causes'))
