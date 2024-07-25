# Create form validation functors.
from dataclasses import dataclass
from typing import Any


class FieldValidationError(Exception):
    pass


class FormValidationError(Exception):
    def __init__(self, errors):
        self.errors = errors


class ValidateField:
    field_type = None

    def __init__(self, is_required=True, additional_validators=None):
        if additional_validators is None:
            additional_validators = []

        self.is_required = is_required
        self.additional_validators = additional_validators

    def __call__(self, value):
        if not self.field_type:
            raise FieldValidationError("The field type must be specified.")

        if (self.is_required or value is not None) and not isinstance(value, self.field_type):
            raise FieldValidationError(f"The value must be of type '{self.field_type.__name__}'.")

        if self.is_required and value is None:
            raise FieldValidationError("The field is required.")

        for additional_validator in self.additional_validators:
            additional_validator(value)


class ValidateCharField(ValidateField):
    field_type = str


class ValidateIntField(ValidateField):
    field_type = int


@dataclass
class ValidateStringLength:
    min_length: Any
    max_length: Any

    def __call__(self, value):
        if self.min_length:
            if len(value) < self.min_length:
                raise FieldValidationError(f"The field length must be at least {self.min_length} characters.")

        if self.max_length:
            if len(value) > self.max_length:
                raise FieldValidationError(f"The field length mustn't be more than {self.max_length} characters.")


class FormValidator:
    def __call__(self, data):
        field_validators = {
            key: value
            for key, value
            in self.__class__.__dict__.items()
            if isinstance(value, ValidateField)
        }
        errors = {}

        for validator_name, validator in field_validators.items():
            value = data.get(validator_name)

            try:
                validator(value)
            except FieldValidationError as exc:
                errors[validator_name] = str(exc)

        if errors:
            raise FormValidationError(errors)


class RegistrationFormValidator(FormValidator):
    name = ValidateCharField(additional_validators=[ValidateStringLength(min_length=5, max_length=64)])
    email = ValidateCharField()
    password = ValidateCharField()
    age = ValidateIntField(is_required=False)


validate_registration_data = RegistrationFormValidator()

try:
    validate_registration_data({
        "name": "John",
        "email": "jh2012@gmail.com",
        "password": "Dkgo30dKS&kdF",
        "age": "23",
    })
except FormValidationError as exc:
    print(f"Registration errors: {exc.errors}")
