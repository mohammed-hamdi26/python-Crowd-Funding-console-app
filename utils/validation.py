import re


def validate_phone(phone_number):
    pattern = r"^01[0125]\d{8}$"
    return re.match(pattern, phone_number)


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)
