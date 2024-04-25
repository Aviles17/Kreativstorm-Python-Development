import unittest
from unittest.mock import patch, Mock
from scripts.api_managment_util import get_weather_data, get_device_location, get_adress_latlong, decompose_json_info, get_icon

class TestApiManagementUtil(unittest.TestCase):

    @patch('requests.get')
    def test_get_weather_data(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'coord': {'lat': 51.51, 'lon': -0.13}}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        data = get_weather_data(51.51, -0.13, 'your_api_key')
        self.assertEqual(data, {'coord': {'lat': 51.51, 'lon': -0.13}})

    @patch('geopy.geocoders.Nominatim.geocode')
    def test_get_device_location(self, mock_geocode):
        mock_geocode.return_value = Mock(address='London, UK', latitude=51.51, longitude=-0.13)

        location = get_device_location('London')
        self.assertEqual(location, ('London, UK', 51.51, -0.13))

    @patch('geopy.geocoders.Nominatim.reverse')
    def test_get_adress_latlong(self, mock_reverse):
        mock_reverse.return_value = Mock(address='London, UK')

        address = get_adress_latlong(51.51, -0.13)
        self.assertEqual(address, 'London, UK')

    def test_decompose_json_info(self):
        data = {
            'coord': {'lat': 51.51, 'lon': -0.13},
            'weather': [{'description': 'light rain'}],
            'main': {'temp_min': 280.15, 'temp_max': 282.15, 'feels_like': 281.15, 'humidity': 93},
            'sys': {'country': 'GB', 'sunrise': 1617867360, 'sunset': 1617916440},
            'timezone': 3600,
            'weather': [{'icon': '10d'}]
        }
        weather_data = decompose_json_info(data)
        self.assertEqual(weather_data.lat, 51.51)

    def test_get_icon(self):
        icon = get_icon('10d')
        self.assertEqual(icon, 'resources/10d@2x.png')

if __name__ == '__main__':
    unittest.main()