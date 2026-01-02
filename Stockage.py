from Log import *
from FileProduits import *
from Produit import *

class Stockage:
    def __init__(self, seuil: int):
        self.SEUIL_STOCK=seuil
        self.journal=Log(3, self)
        self.stock: list[FileProduits] = []
    
    def ajouterProduit(self, produit:Produit):
        for elt in self.stock:
            if elt.id==produit.id():
                elt.enfiler(produit)
                return None
        file=FileProduits(produit.id())
        file.enfiler(produit)
        self.stock.append(file)

    def retirerProduit(self,idProduit:str)->Produit:
        for elt in self.stock:
            if elt.id==idProduit:
                if elt.size()==0:
                    return None
                if elt.size()-1==0:
                    self.journal.ajoutLog("Produit " + elt.id + " en rupture de stock")
                    self.journal.gererLog()
                elif elt.size()-1<self.SEUIL_STOCK:
                    self.journal.ajoutLog("Produit " + elt.id + " en faible quantité")
                return elt.defiler()
            
    def isProduitEmpty(self, idProduit: str)-> bool:
        eltExistant: list[str] = []
        for elt in self.stock:
            if elt.id == idProduit and elt.isEmpty():
                return True
            elif elt.id == idProduit and  not elt.isEmpty():
                return False
            eltExistant.append(elt.id)
        if idProduit in eltExistant:
            return False
        else :
            return True

    def afficher(self):
        for elt in self.stock:
            print(elt)
            print("----------")