"""Question 1 : FizzBuzz B. Première évolution du code ) :

Ici, on demande un entier 'n' et on renvoie la concaténation
des tokens FizzBuzz de 1 à 'n'.
"""

from .fizzbuzz import _token

def affiche(n: int) -> str:
    """Retourne la chaîne FizzBuzz de 1 à n.

    - Si 'n' n'est pas un entier positif, on renvoie une chaîne vide.
    - Sinon, on colle tous les tokens de 1 à 'n'.
    """
    if not isinstance(n, int) or n < 1:
        return ""
    return "".join(_token(i) for i in range(1, n + 1))


