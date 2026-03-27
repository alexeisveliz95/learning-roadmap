from password_gen import generate_password

def test_password_length():
    resultado = generate_password(16)
    assert len(resultado) == 16