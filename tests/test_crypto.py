from src.crypto import crypt

def test_crypt_decale_de_1_sur_table():
    assert crypt("a") != "a"
    assert crypt("aZ")
    out = crypt("Az 9!")
    assert isinstance(out, str) and len(out) == len("Az 9!")
