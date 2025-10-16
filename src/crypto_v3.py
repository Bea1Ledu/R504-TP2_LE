"""Question 2 : Cryptage C. Deuxième évolution du code):

Cette version ajoute la fonction decrypt() permettant de déchiffrer
les messages produits par la fonction crypt() de crypto_v2.py.
"""

from .crypto import _shift_char


def decrypt(message: str) -> str:
    """Déchiffre un message produit par crypt() de crypto_v2.py."""
    if not message:
        return ""

    # On récupère le dernier caractère (le pas)
    pas_char = message[-1]
    if not pas_char.isdigit():
        raise ValueError("Message chiffré invalide : pas manquant ou incorrect")

    pas = int(pas_char)
    core = message[:-1]  # partie du message sans le pas

    # On décale chaque caractère dans le sens inverse
    return "".join(_shift_char(c, -pas) for c in core)
