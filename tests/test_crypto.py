from src.crypto import crypt

def test_crypt_decale_de_1_sur_table():
    assert crypt("a") != "a"
    assert crypt("aZ")
    out = crypt("Az 9!")
    assert isinstance(out, str) and len(out) == len("Az 9!")

from src.crypto_v2 import crypt as crypt_v2

def test_crypt_avec_pas_concatene_a_la_fin():
    out = crypt_v2("Az 9!", 3)
    assert out.endswith("3")
    core = out[:-1]
    assert len(core) == len("Az 9!")
    out1 = crypt_v2("Hello", 1)
    assert out1[:-1] != "Hello" and out1.endswith("1")

from src.crypto_v3 import decrypt
from src.crypto_v2 import crypt as crypt_v2

def test_decrypt_inverse_crypt_v2():
    original = "Bonjour, le monde! 42"
    for pas in (1, 3, 9):
        enc = crypt_v2(original, pas)
        dec = decrypt(enc)
        assert dec == original
