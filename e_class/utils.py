from django.utils.crypto import get_random_string #type:ignore

def generate_account_id():
    return get_random_string(8, allowed_chars='0123456789')