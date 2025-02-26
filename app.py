"""
Module de calculs mathématiques de base et de salutations.
Ce module fournit des fonctions pour additionner, multiplier, diviser et saluer.
"""

def add(a, b):
    """Ajoute deux nombres et retourne le résultat.

    Args:
        a (float): Premier nombre.
        b (float): Deuxième nombre.

    Returns:
        float: La somme de a et b.
    """
    return a + b


def multiply(x, y):
    """Multiplie deux nombres et retourne le résultat.

    Args:
        x (float): Premier nombre.
        y (float): Deuxième nombre.

    Returns:
        float: Le produit de x et y.
    """
    return x * y


def divide(x, y):
    """Divise deux nombres et retourne le résultat.

    Args:
        x (float): Dividende.
        y (float): Diviseur.

    Returns:
        float or None: Le résultat de la division si y != 0, sinon None.
    """
    if y == 0:
        return None
    return x / y


def greet(name):
    """Retourne une salutation personnalisée.

    Si le nom est une chaîne vide, retourne une salutation générique.

    Args:
        name (str): Le nom à saluer.

    Returns:
        str: Un message de salutation.
    """
    if not name:
        return "Hello, World!"
    return f"Hello,{name}"