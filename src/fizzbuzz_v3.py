"""Question 1 : FizzBuzz (C. Deuxième évolution du code):
On prend deux bornes, on valide rapidement, puis on renvoie la
concaténation des tokens pour tous les nombres de l'intervalle.
"""

from .fizzbuzz import _token

def affiche(n1: int, n2: int) -> str:
    """Retourne la chaîne FizzBuzz pour l'intervalle [n1, n2].

    - Si les bornes ne sont pas des entiers, on renvoie "".
    - Si n1 est strictement supérieur à n2, on renvoie "".
    - Sinon, on colle tous les tokens de 'n1' à 'n2' inclus.
    """
    if not all(isinstance(x, int) for x in (n1, n2)):
        return ""
    if n1 > n2:
        return ""
    return "".join(_token(i) for i in range(n1, n2 + 1))
