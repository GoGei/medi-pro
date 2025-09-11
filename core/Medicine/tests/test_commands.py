import io
import zipfile
from unittest.mock import patch, Mock
from openpyxl import Workbook
from django.core.management import CommandError, call_command
from django.test import TestCase
from ..factories import AllergyCauseFactory, AllergyReactionFactory, AllergyTypeFactory, ICD10Factory
from ..models import AllergyCause, AllergyReaction, AllergyType, ICD10, MedicineHandbookSources


class ExtractAllergyCauseTestCase(TestCase):
    FIXTURE_PATH = 'core/Medicine/tests/mocks/mocked_allergy_table.html'

    def test_extract_success(self):
        with open(self.FIXTURE_PATH, 'rb') as f:
            fixture_content = f.read()

        mock_response = Mock()
        mock_response.content = fixture_content
        mock_response.status_code = 200

        AllergyCauseFactory.create(code='Code2')

        c1 = AllergyCause.objects.count()
        with patch('requests.get', return_value=mock_response) as mock_get:
            call_command('extract_allergy_cause')
        mock_get.assert_called_once()
        c2 = AllergyCause.objects.count()
        self.assertEqual(c1 + 1, c2)

    def test_extract_failed(self):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = Exception('Mocked bad exception')

        c1 = AllergyCause.objects.count()
        with patch("requests.get", return_value=mock_response) as mock_get:
            with self.assertRaises(CommandError) as e:
                call_command("extract_allergy_cause")
        mock_get.assert_called_once()
        self.assertIn('Mocked bad exception', str(e.exception))

        c2 = AllergyCause.objects.count()
        self.assertEqual(c1, c2)

    def test_extract_table_failed(self):
        mock_response = Mock()
        mock_response.content = None
        mock_response.status_code = 200

        c1 = AllergyCause.objects.count()
        with patch('requests.get', return_value=mock_response) as mock_get:
            with self.assertRaises(CommandError) as e:
                call_command('extract_allergy_cause')
        mock_get.assert_called_once()
        self.assertIn('Unable to extract data from table', str(e.exception))

        c2 = AllergyCause.objects.count()
        self.assertEqual(c1, c2)


class ExtractAllergyReactionTestCase(TestCase):
    FIXTURE_PATH = 'core/Medicine/tests/mocks/mocked_allergy_table.html'

    def test_extract_success(self):
        with open(self.FIXTURE_PATH, 'rb') as f:
            fixture_content = f.read()

        mock_response = Mock()
        mock_response.content = fixture_content
        mock_response.status_code = 200

        AllergyReactionFactory.create(code='Code2')

        c1 = AllergyReaction.objects.count()
        with patch('requests.get', return_value=mock_response) as mock_get:
            call_command('extract_allergy_reaction')
        mock_get.assert_called_once()
        c2 = AllergyReaction.objects.count()
        self.assertEqual(c1 + 1, c2)

    def test_extract_failed(self):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = Exception('Mocked bad exception')

        c1 = AllergyReaction.objects.count()
        with patch("requests.get", return_value=mock_response) as mock_get:
            with self.assertRaises(CommandError) as e:
                call_command("extract_allergy_reaction")
        mock_get.assert_called_once()
        self.assertIn('Mocked bad exception', str(e.exception))

        c2 = AllergyReaction.objects.count()
        self.assertEqual(c1, c2)

    def test_extract_table_failed(self):
        mock_response = Mock()
        mock_response.content = None
        mock_response.status_code = 200

        c1 = AllergyReaction.objects.count()
        with patch('requests.get', return_value=mock_response) as mock_get:
            with self.assertRaises(CommandError) as e:
                call_command('extract_allergy_reaction')
        mock_get.assert_called_once()
        self.assertIn('Unable to extract data from table', str(e.exception))

        c2 = AllergyReaction.objects.count()
        self.assertEqual(c1, c2)


class ExtractAllergyTypeTestCase(TestCase):
    FIXTURE_PATH = 'core/Medicine/tests/mocks/mocked_allergy_table.html'

    def test_extract_success(self):
        with open(self.FIXTURE_PATH, 'rb') as f:
            fixture_content = f.read()

        mock_response = Mock()
        mock_response.content = fixture_content
        mock_response.status_code = 200

        AllergyTypeFactory.create(code='Code2')

        c1 = AllergyType.objects.count()
        with patch('requests.get', return_value=mock_response) as mock_get:
            call_command('extract_allergy_types')
        mock_get.assert_called_once()
        c2 = AllergyType.objects.count()
        self.assertEqual(c1 + 1, c2)

    def test_extract_failed(self):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = Exception('Mocked bad exception')

        c1 = AllergyType.objects.count()
        with patch("requests.get", return_value=mock_response) as mock_get:
            with self.assertRaises(CommandError) as e:
                call_command("extract_allergy_types")
        mock_get.assert_called_once()
        self.assertIn('Mocked bad exception', str(e.exception))

        c2 = AllergyType.objects.count()
        self.assertEqual(c1, c2)

    def test_extract_table_failed(self):
        mock_response = Mock()
        mock_response.content = None
        mock_response.status_code = 200

        c1 = AllergyType.objects.count()
        with patch('requests.get', return_value=mock_response) as mock_get:
            with self.assertRaises(CommandError) as e:
                call_command('extract_allergy_types')
        mock_get.assert_called_once()
        self.assertIn('Unable to extract data from table', str(e.exception))

        c2 = AllergyType.objects.count()
        self.assertEqual(c1, c2)


class LoadICD10TestCase(TestCase):
    def _make_test_zip(self) -> io.BytesIO:
        wb = Workbook()
        ws = wb.active
        ws.append(["CODE", "SHORT DESCRIPTION (VALID ICD-10 FY2025)", "NF EXCL"])
        ws.append(["A00", "Cholera", None])
        ws.append(["B00", "Herpesviral infections", "Y"])  # archived
        ws.append(["C00", "Already presented", None])  # archived

        bio = io.BytesIO()
        wb.save(bio)
        bio.seek(0)

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zf:
            zf.writestr("section111validicd10-jan2025_0.xlsx", bio.getvalue())
        zip_buffer.seek(0)
        return zip_buffer

    def test_load_success(self):
        test_zip = self._make_test_zip()

        RealZipFile = zipfile.ZipFile

        def fake_zipfile(file, mode="r", *args, **kwargs):
            return RealZipFile(test_zip, mode, *args, **kwargs)

        ICD10Factory.create(code='C00')
        c1 = ICD10.objects.count()
        with patch("zipfile.ZipFile", side_effect=fake_zipfile):
            call_command("load_icd10")
        c2 = ICD10.objects.count()
        self.assertEqual(c1 + 2, c2)

        cholera = ICD10.objects.get(code="A00")
        self.assertEqual(cholera.name, "Cholera")
        self.assertEqual(cholera.source, MedicineHandbookSources.CMS_GOV)
        self.assertIsNone(cholera.archived_stamp)

        herpes = ICD10.objects.get(code="B00")
        self.assertEqual(herpes.name, "Herpesviral infections")
        self.assertIsNotNone(herpes.archived_stamp)
