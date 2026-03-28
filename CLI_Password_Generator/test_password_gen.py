from password_gen import generate_password

def test_password_length():
    profile = {"length": 16}
    resultado = generate_password(profile)
    assert len(resultado) == 16