import re


class Validator():
    def __init__(self):
        pass

    def validate_name(self, name):
        if not isinstance(name, str):
            return None
        if len(name.strip()) < 2:
            return None
        if not all(c.isalpha() or c.isspace() or c in "-'." for c in name):
            return None
        return True

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def is_valid_password(self, password):
        if not isinstance(password, str):
            return False
        if len(password) < 8:
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
            return False
        return True
