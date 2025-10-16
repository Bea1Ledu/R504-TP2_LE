"""Question 2 : Cryptage A. Création de la première solution) :

On définit un alphabet étendu (lettres ASCII, ponctuation, chiffres et espace),
et on décale chaque caractère d'un certain nombre de positions dans cet alphabet.
"""

import string

# Table de caractères : lettres ASCII, ponctuation, chiffres, puis espace
CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "

def _shift_char(c: str, step: int = 1) -> str:
    """Décale un caractère 'c' de 'step' positions dans l'alphabet custom.
'
    Si le caractère n'est pas dans l'alphabet, on le laisse inchangé.
    """
    if c not in CARACTERES:
        return c
    i = CARACTERES.index(c)
    return CARACTERES[(i + step) % len(CARACTERES)]

def crypt(message: str) -> str:
    """Chiffre un message en décalant chaque caractère d'une position.

    Version simple: décalage fixe de 1.
    """
    return "".join(_shift_char(c, 1) for c in message)

