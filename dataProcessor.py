import json

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def avgAgeCountry(data, transform_function=None):
    country_age_sum = {}
    country_count = {}

    for person in data:
        country = person.get('country')
        age = person.get('age')

        if country is None or age is None:
            continue

        if transform_function:
            age = transform_function(age)

        country_age_sum[country] = country_age_sum.get(country, 0) + age
        country_count[country] = country_count.get(country, 0) + 1

    avg_age_country = {country: country_age_sum[country] / country_count[country] for country in country_age_sum}

    return avg_age_country