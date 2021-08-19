from django.core.exceptions import ValidationError


def validate_file(value):
    value = str(value)
    if not value.endswith(".pdf"):
        raise ValidationError("Only PDF document can be uploaded")
    else:
        return value


def validate_file_size(value):
    filesize = value.size
    if filesize > 4000000:
        raise ValidationError("The maximum file size can be uploaded 4MB")
    else:
        return value
