from .fizzbuzz import _token

def affiche(n: int) -> str:
    if not isinstance(n, int) or n < 1:
        return ""
    return "".join(_token(i) for i in range(1, n + 1))
