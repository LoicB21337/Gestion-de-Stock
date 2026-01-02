from Log import *
from FileProduits import *
from Produit import *


class Stockage:
    """Conteneur principal des produits stockés.

    Les produits sont organisés en `FileProduits` groupées par identifiant.
    """

    def __init__(self, seuil: int):
        """Initialiser le stockage avec un seuil de réapprovisionnement."""
        self.SEUIL_STOCK = seuil
        self.journal = Log(3, self)
        self.stock: list[FileProduits] = []

    def ajouterProduit(self, produit: Produit):
        """Ajouter un produit au stockage, en créant une file si nécessaire."""
        for elt in self.stock:
            if elt.id == produit.id():
                elt.enfiler(produit)
                return None
        file = FileProduits(produit.id())
        file.enfiler(produit)
        self.stock.append(file)

    def retirerProduit(self, idProduit: str) -> Produit:
        """Retirer et retourner un produit correspondant à `idProduit`, ou None."""
        for elt in self.stock:
            if elt.id == idProduit:
                if elt.size() == 0:
                    return None
                if elt.size() - 1 == 0:
                    self.journal.ajoutLog("Produit " + elt.id + " en rupture de stock")
                    self.journal.gererLog()
                elif elt.size() - 1 < self.SEUIL_STOCK:
                    self.journal.ajoutLog("Produit " + elt.id + " en faible quantité")
                return elt.defiler()

    def isProduitEmpty(self, idProduit: str) -> bool:
        """Retourner True si l'identifiant n'existe pas ou si la file est vide."""
        eltExistant: list[str] = []
        for elt in self.stock:
            if elt.id == idProduit and elt.isEmpty():
                return True
            elif elt.id == idProduit and not elt.isEmpty():
                return False
            eltExistant.append(elt.id)
        if idProduit in eltExistant:
            return False
        else:
            return True

    def afficher(self):
        """Afficher la liste des files de produits et leurs tailles."""
        for elt in self.stock:
            print(elt)
            print("----------")