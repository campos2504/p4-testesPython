import os
import unittest
from dataProcessor import avgAgeCountry, read_json_file

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Amy Owens')
        self.assertEqual(data[1]['age'], 50)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")
    
    def test_avgAgeCountry_empty_json(self):
        empty_data = []
        result = avgAgeCountry(empty_data)
        self.assertDictEqual(result, {})

    def test_avgAgeCountry_missing_age(self):
        data = [
            {"name": "John Doe", "country": "US"},
            {"name": "Jane Doe", "country": "US"}
        ]
        result = avgAgeCountry(data)
        self.assertDictEqual(result, {}) 

    def test_avgAgeCountry_missing_country(self):
        data = [
            {"name": "John Doe", "age": 30},
            {"name": "Jane Doe", "age": 25}
        ]
        result = avgAgeCountry(data)
        self.assertDictEqual(result, {})


    def test_avgAgeCountry_with_transform_function(self):
        data = [
            {"name": "John Doe", "age": 30, "country": "US"},
            {"name": "Jane Doe", "age": 25, "country": "US"}
        ]
        # Transform function: convert age from years to months
        transform_function = lambda age: age * 12
        result = avgAgeCountry(data, transform_function)
        self.assertDictEqual(result, {"US": (30*12 + 25*12) / 2})

if __name__ == '__main__':
    unittest.main()