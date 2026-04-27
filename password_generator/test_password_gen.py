from password_gen import generate_password

def test_password_length():
    dict_config = {
        "length": 8,
        "use_uppercase": True,
        "use_digits": True,
        "use_special_chars": True,
        "avoid_ambiguous": True,
        "minimum_uppercase": 1,
        "minimum_digits": 1,
        "minimum_special_chars": 1
    }
    assert generate_password(dict_config) == 8