from .fizzbuzz import _token

def affiche(n1: int, n2: int) -> str:
    if not all(isinstance(x, int) for x in (n1, n2)):
        return ""
    if n1 > n2:
        return ""
    return "".join(_token(i) for i in range(n1, n2 + 1))
