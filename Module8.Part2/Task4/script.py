# Створити словник із валідованими даними, який окрім оригінальних даних містить додаткові. Початкові дані мають
# вкладений словник із даними профілю. Словник із початковими данними повинен залишитися без змін.
import copy
import re


COUNTRY_CODES = {
    "+36": "Hungary",
    "+371": "Latvia",
    "+372": "Estonia",
    "+49": "Germany",
    "+380": "Ukraine",
    "+1": "USA",
}


def get_validated_data(initial_data):
    validated_data = copy.deepcopy(initial_data)
    first_name = validated_data["first_name"]
    last_name = validated_data["last_name"]
    age = validated_data["age"]
    phone_number = validated_data["profile"]["phone_number"]

    validated_data["full_name"] = f"{first_name} {last_name}"

    if isinstance(age, str) and age.isdigit():
        validated_data["age"] = int(age)

    validated_data.setdefault("lang", "en")

    validated_data["profile"].setdefault("education", "No formal education")

    if match := re.match(r"^(\+\d{1,3})\d{9}$", phone_number):
        country_code = match.group(1)
        if country := COUNTRY_CODES.get(country_code):
            validated_data["profile"]["country"] = country

    return validated_data


form_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "user1@example.com",
    "age": "18",
    "profile": {
        "gender": "m",
        "city": "New York",
        "phone_number": "+1224567890",
    },
}
validated_data = get_validated_data(form_data)

print(f"Initial data: {form_data}")
print(f"Validated data: {validated_data}")
