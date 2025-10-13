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
from src.fizzbuzz_v3 import affiche as affiche_range

def test_affiche_intervalle_5_10():
    assert affiche_range(5, 10) == "BuzzFizz78FizzBuzz"

def test_affiche_intervalle_10_16():
    assert affiche_range(10, 16) == "Buzz11Fizz1314FrisBee16"
