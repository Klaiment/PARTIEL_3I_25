"""
Module de test pour les fonctions de app.py.
Ce module teste les fonctions mathématiques et de salutation.
"""

import unittest
from app import add, multiply, divide, greet


class TestAddFunction(unittest.TestCase):
    """Classe de test pour la fonction add."""

    def test_add(self):
        """Teste la fonction add avec différents cas."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


class TestMultiplyFunction(unittest.TestCase):
    """Classe de test pour la fonction multiply."""

    def test_multiply(self):
        """Teste la fonction multiply avec différents cas."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)


class TestDivideFunction(unittest.TestCase):
    """Classe de test pour la fonction divide."""

    def test_divide(self):
        """Teste la fonction divide avec différents cas."""
        self.assertEqual(divide(10, 2), 5)
        self.assertIsNone(divide(5, 0))
        self.assertEqual(divide(0, 5), 0)


class TestGreetFunction(unittest.TestCase):
    """Classe de test pour la fonction greet."""

    def test_greet(self):
        """Teste la fonction greet avec différents cas."""
        self.assertEqual(greet("Alice"), "Hello,Alice")
        self.assertEqual(greet(""), "Hello, World!")
        self.assertEqual(greet("Bob"), "Hello,Bob")


if __name__ == "__main__":
    unittest.main()
