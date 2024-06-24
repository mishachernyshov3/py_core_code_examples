# Валідувати опис (не більше 120 символів)

MAX_DESCRIPTION_LENGTH = 120

response_body = {
    "course_name": "Math",
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
}

if len(response_body['description']) > MAX_DESCRIPTION_LENGTH:
    print("The description is too long.")
