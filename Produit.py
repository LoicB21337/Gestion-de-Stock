class Produit:
    """Représente un produit avec un type et un volume."""

    def __init__(self, typeProduit: str, volume: int):
        """Initialiser un produit avec son type (lettre) et son volume (chiffre)."""
        self.typeProduit = typeProduit
        self.volume = volume

    def id(self) -> str:
        """Retourner l'identifiant du produit sous la forme 'T<volume>'."""
        return self.typeProduit + str(self.volume)

    def __str__(self) -> str:
        """Retourner la représentation sous forme d'identifiant."""
        return self.id()

    def getTypeProduit(self):
        """Retourner le type (lettre) du produit."""
        return self.typeProduit

    def getVolume(self):
        """Retourner le volume (entier) du produit."""
        return self.volume