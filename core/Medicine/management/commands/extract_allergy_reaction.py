from django.db.transaction import atomic
from django.core.management.base import BaseCommand, CommandError

from core.Medicine.enums import MedicineHandbookSources
from core.Medicine.extractors.hl7 import FHIRPageExtractor, FHIRPageExtractorException
from core.Medicine.models import AllergyReaction


class Command(BaseCommand):
    help = 'Load allergy reactions (Allergy intolerance reaction) from HL7 FHIR'
    default_url = 'https://build.fhir.org/ig/hl7ch/ch-term/ValueSet-CHAllergyIntoleranceReactionManifestationValueSet.html'  # noqa

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
        except FHIRPageExtractorException as e:
            raise CommandError(f'Unable to extract data from table: {e}')
        except Exception as e:
            raise CommandError(f'Unknown error: {e}')

        self.stdout.write(self.style.SUCCESS(f'Successfully received {len(extractor.data)} items'))
        try:
            self.update_allergy_reactions(extractor)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Unable to update allergy reactions: {e}'))

    @atomic
    def update_allergy_reactions(self, extractor: FHIRPageExtractor):
        batch_size = 200
        updated_count = created_count = total_count = 0
        allergy_reactions_to_create: list[AllergyReaction] = list()
        allergy_reactions_to_update: list[AllergyReaction] = list()
        fields = ('name', 'source')
        for item in extractor.data:
            allergy_item = {
                'source': MedicineHandbookSources.HL7,
                'name': item['display'],
                'code': item['code'],
            }
            try:
                obj = AllergyReaction.objects.get(code=allergy_item['code'])
                for field, value in allergy_item.items():
                    setattr(obj, field, value)
                allergy_reactions_to_update.append(obj)
                updated_count += 1
            except AllergyReaction.DoesNotExist:
                allergy_reactions_to_create.append(AllergyReaction(**allergy_item))
                created_count += 1
            total_count += 1
            if total_count % batch_size == 0:
                self.stdout.write(f'Processed {total_count} allergy reactions')

            if len(allergy_reactions_to_create) == batch_size:
                AllergyReaction.objects.bulk_create(allergy_reactions_to_create)
                allergy_reactions_to_create = list()
            if len(allergy_reactions_to_update) == batch_size:
                AllergyReaction.objects.bulk_update(allergy_reactions_to_update, fields=fields)
                allergy_reactions_to_update = list()

        if allergy_reactions_to_create:
            AllergyReaction.objects.bulk_create(allergy_reactions_to_create)
        if allergy_reactions_to_update:
            AllergyReaction.objects.bulk_update(allergy_reactions_to_update, fields=fields)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} allergy reactions'))
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} allergy reactions'))
