from .crypto import _shift_char

def crypt(message: str, pas: int) -> str:
    if not isinstance(pas, int) or pas < 1 or pas > 9:
        raise ValueError("pas doit être un entier entre 1 et 9")
    core = "".join(_shift_char(c, pas) for c in message)
    return core + str(pas)
