class File:
    """Implémentation simple d'une file FIFO.

    La file conserve des objets dans l'ordre d'insertion et fournit
    des opérations de base utilisées par le reste du projet.
    """

    def __init__(self):
        """Initialiser une file vide."""
        self.file = []

    def isEmpty(self):
        """Retourner True si la file est vide."""
        return self.file == []

    def vider(self):
        """Vider complètement la file."""
        self.file = []

    def size(self):
        """Retourner le nombre d'éléments dans la file."""
        return len(self.file)

    def print(self):
        """Afficher tous les éléments de la file dans l'ordre."""
        for e in self.file:
            print(e)

    def enfiler(self, n):
        """Ajouter un élément à la fin de la file."""
        self.file.append(n)

    def defiler(self):
        """Retirer et retourner le premier élément, ou None si vide."""
        if not self.isEmpty():
            return self.file.pop(0)
        else:
            return None