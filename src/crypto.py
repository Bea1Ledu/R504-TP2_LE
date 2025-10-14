import string

# Table de caractères : lettres ASCII, ponctuation, chiffres, puis espace
CARACTERES = string.ascii_letters + string.punctuation + string.digits + " "

def _shift_char(c: str, step: int = 1) -> str:
    if c not in CARACTERES:
        return c
    i = CARACTERES.index(c)
    return CARACTERES[(i + step) % len(CARACTERES)]

def crypt(message: str) -> str:
    return "".join(_shift_char(c, 1) for c in message)

