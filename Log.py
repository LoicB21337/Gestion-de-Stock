from File import File
from Produit import Produit


class Log:
    """Journal d'événements du stockage.

    Stocke les messages dans une `File` et permet de gérer la taille
    maximale du journal.
    """

    def __init__(self, size: int):
        """Initialiser le journal avec une taille maximale et la référence
        vers le stockage associé.
        """
        self.log = File()
        self.LOG_SIZE = size

    def ajoutLog(self, message: str):
        """Ajouter un message au journal en gérant la taille maxima.

        Si la capacité est atteinte, `gererLog` est appelée avant
        d'enfiler le nouveau message.
        """
        if self.log.size() >= self.LOG_SIZE:
            self.gererLog()
        self.log.enfiler(message)

    def afficherLog(self):
        """Afficher tous les messages du journal."""
        self.log.print()
        print("-----------------------------")

    def isLogPlein(self) -> bool:
        """Retourner True si le journal est plein."""
        return self.log.size() == self.LOG_SIZE

    def viderLog(self):
        """Vider complètement le journal."""
        self.log.vider()

    def gererLog(self):
        """Gérer le journal lorsque sa capacité est atteinte."""
        self.viderLog()