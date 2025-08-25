from django.test import TestCase
from unittest.mock import patch, MagicMock

from requests import HTTPError, Timeout

from ..models import Country
from ..factories import CountryFactory
from ..services import import_countries_from_fixture, import_countries_from_external_api, LoadCountriesException


class CountryTestCase(TestCase):
    def test_create_obj(self):
        obj = CountryFactory()
        self.assertIn(obj, Country.objects.all())

    def test_delete_obj(self):
        obj = CountryFactory()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, Country.objects.all().values_list('id', flat=True))

    def test_import_countries_from_fixture(self):
        c1 = Country.objects.count()
        import_countries_from_fixture()
        c2 = Country.objects.count()
        self.assertTrue(c2 > c1)


class ImportCountriesFromExternalApiTestCase(TestCase):
    @patch('core.Country.services.requests.get')
    def test_import_countries_from_external_api_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                'name': {'common': 'Test', 'official': 'Test'},
                'cca2': 'TT',
                'ccn3': '000',
            }
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        c1 = Country.objects.count()
        qs = import_countries_from_external_api(fields=('name', 'cca2', 'ccn3'))
        c2 = Country.objects.count()

        self.assertTrue(c2 > c1)
        self.assertEqual(qs.count(), 1)
        obj = qs.first()
        self.assertEqual(obj.name, 'Test')
        self.assertEqual(obj.cca2, 'TT')
        self.assertEqual(obj.ccn3, '000')

    @patch('core.Country.services.requests.get')
    def test_import_countries_from_external_api_no_fields(self, mock_get):
        with self.assertRaises(LoadCountriesException):
            import_countries_from_external_api(fields=())

    @patch('core.Country.services.requests.get')
    def test_import_countries_from_external_api_timeout(self, mock_get):
        mock_get.side_effect = Timeout('Test timeout')
        with self.assertRaises(LoadCountriesException) as e:
            import_countries_from_external_api(fields=('test',))
        self.assertIn('Timeout', str(e.exception))
        mock_get.assert_called()

    @patch('core.Country.services.requests.get')
    def test_import_countries_from_external_api_http_error(self, mock_get):
        mock_get.side_effect = HTTPError('Test')
        with self.assertRaises(LoadCountriesException) as e:
            import_countries_from_external_api(fields=('test',))
        self.assertIn('HTTPError', str(e.exception))
        mock_get.assert_called()

    @patch('core.Country.services.requests.get')
    def test_import_countries_from_external_api_invalid_json(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError('Not a JSON')
        mock_get.return_value = mock_response
        with self.assertRaises(LoadCountriesException) as ctx:
            import_countries_from_external_api(fields=('name', 'cca2', 'ccn3'))
        self.assertIn('Not a JSON', str(ctx.exception))
        mock_get.assert_called()
