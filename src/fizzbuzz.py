"""Question 1 : FizzBuzz (A. Création d'une première solution) :

Ici on génère une chaîne pour chaque nombre selon les règles du TP:
- multiple de 3 -> "Fizz"
- multiple de 5 -> "Buzz"
- multiple de 15 -> "FrisBee" (variante demandée)
- sinon on renvoie le nombre tel quel
"""

def _token(n: int) -> str:
    """Retourne le token associé à un entier n selon les règles FizzBuzz (voir en haut)
    """
    if n % 15 == 0:
        return "FrisBee"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def affiche():
    """Affiche le FizzBuzz complet de 1 à 100, sans retour à la ligne.

    Note: on colle tout dans une seule chaîne pour aller plus vite,
    puis on l'imprime sans ajouter de nouvelle ligne à la fin.
    """
    s = "".join(_token(i) for i in range(1, 101))
    print(s, end="")

