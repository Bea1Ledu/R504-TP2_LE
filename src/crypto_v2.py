"""Question 2 : Cryptage B. Première évolution du code) :

On réutilise la fonction _shift_char et on permet de choisir le pas de
chiffrement (entre 1 et 9). On retourne le message chiffré suivi du pas,
pour pouvoir le retrouver facilement.
"""

from .crypto import _shift_char

def crypt(message: str, pas: int) -> str:
    """Chiffre avec un décalage de 'pas' (1..9) et ajoute 'pas' en suffixe.

    Lève une ValueError si 'pas' n'est pas un entier dans [1, 9].
    """
    if not isinstance(pas, int) or pas < 1 or pas > 9:
        raise ValueError("pas doit être un entier entre 1 et 9")
    core = "".join(_shift_char(c, pas) for c in message)
    return core + str(pas)
