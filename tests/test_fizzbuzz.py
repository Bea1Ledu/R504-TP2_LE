from io import StringIO
from contextlib import redirect_stdout
from src.fizzbuzz import affiche

def capture_output(func):
    buf = StringIO()
    with redirect_stdout(buf):
        func()
    return buf.getvalue()

def test_affiche_sans_param_remplace_multiples():
    out = capture_output(affiche)
    assert out.startswith("12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")
    assert out.endswith("9798FizzBuzz")

from src.fizzbuzz_v2 import affiche as affiche_n

def test_affiche_n_retourne_chaine():
    assert affiche_n(15) == "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee"
