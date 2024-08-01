# Створити словник із валідованими даними, який окрім оригінальних даних містить додаткові. Словник із початковими
# данними повинен залишитися без змін.
import copy


def get_validated_data(initial_data):
    validated_data = copy.copy(initial_data)
    first_name = validated_data["first_name"]
    last_name = validated_data["last_name"]
    age = validated_data["age"]

    validated_data["full_name"] = f"{first_name} {last_name}"

    if isinstance(age, str) and age.isdigit():
        validated_data["age"] = int(age)

    validated_data.setdefault("lang", "en")

    return validated_data


form_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "user1@example.com",
    "age": "18",
}
validated_data = get_validated_data(form_data)

print(f"Initial data: {form_data}")
print(f"Validated data: {validated_data}")
