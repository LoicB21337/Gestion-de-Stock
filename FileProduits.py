from File import File


class FileProduits(File):
    """File spécialisée pour stocker des instances de `Produit` groupées par id.

    L'attribut `id` représente l'identifiant du produit (lettre + volume).
    """

    def __init__(self, id: str):
        """Créer une FileProduits avec l'identifiant fourni."""
        super().__init__()
        self.id: str = id

    def getId(self) -> str:
        """Retourner l'identifiant associé à cette file de produits."""
        return self.id

    def setId(self, new_id: str):
        """Modifier l'identifiant associé à cette file de produits."""
        self.id = new_id

    def __str__(self):
        """Retourner une représentation compacte (id, nombre)."""
        return str((self.getId(), self.size()))