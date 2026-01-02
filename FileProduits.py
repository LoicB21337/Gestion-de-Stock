from File import *


class FileProduits(File):
    """File spécialisée pour stocker des instances de `Produit` groupées par id.

    L'attribut `id` représente l'identifiant du produit (lettre + volume).
    """

    def __init__(self, id: str):
        """Créer une FileProduits avec l'identifiant fourni."""
        super().__init__()
        self.id: str = id

    def __str__(self):
        """Retourner une représentation compacte (id, nombre)."""
        return str((self.id, self.size()))