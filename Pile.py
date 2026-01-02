class Pile:
    """Simple pile (LIFO) d'objets."""

    def __init__(self):
        """Initialiser une pile vide."""
        self.pile = []

    def isEmpty(self):
        """Retourner True si la pile est vide."""
        return self.pile == []

    def size(self):
        """Retourner le nombre d'éléments dans la pile."""
        return len(self.pile)

    def print(self):
        """Afficher les éléments de la pile du dernier au premier."""
        self.pile.reverse()
        for e in self.pile:
            print(e)
        self.pile.reverse()

    def empiler(self, n):
        """Ajouter un élément au sommet de la pile."""
        self.pile.append(n)

    def depiler(self):
        """Retirer et retourner l'élément du sommet, ou None si vide."""
        if not self.isEmpty():
            return self.pile.pop(-1)
        else:
            return None