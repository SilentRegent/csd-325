import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country_with_language(self):
        self.assertEqual(
            city_country("santiago", "chile", 5000000, "spanish"),
            "Santiago, Chile - population 5000000, Spanish"
        )

    def test_city_country_without_language(self):
        self.assertEqual(
            city_country("tokyo", "japan", 13929286),
            "Tokyo, Japan - population 13929286"
        )

if __name__ == "__main__":
    unittest.main()
