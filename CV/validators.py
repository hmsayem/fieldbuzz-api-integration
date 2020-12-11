from django.core.exceptions import ValidationError


def validate_file(value):
    value = str(value)
    if not value.endswith(".pdf"):
        raise ValidationError("Only PDF document can be uploaded")
    else:
        return value
