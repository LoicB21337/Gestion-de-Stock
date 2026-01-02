from Stockage import *
from Produit import *
from Pile import Pile

SEUIL_STOCK = 3
LOG_SIZE = 3

 
class GestionDeStock:
    def __init__(self, stock):
        self.stock: Stockage = Stockage(SEUIL_STOCK)
        self.entreeRapide(stock)
    
    def afficherStock(self):
        self.stock.afficher()
    
    def afficherJournal(self):
        self.stock.journal.afficherLog()

    def separerProduitEtVolume(self, entree:str)->list:
        entree=entree.split(', ')
        sortie=[]
        for elt in entree:
            typeProduit = elt[0]
            volume = elt.removeprefix(typeProduit)
            sortie.append((typeProduit, int(volume)))
        return sortie

    def entreeRapide(self, entree:str):
        for typeProduit, volume in self.separerProduitEtVolume(entree):
            produits = Produit(typeProduit,volume)
            self.stock.ajouterProduit(produits)

    def commander(self):
        colis=Pile()
        print("Ecrivez votre commande")
        entree=str(input())
        listeProduit=self.separerProduitEtVolume(entree)
        listeCommande=[]
        for elt in listeProduit:
            id=str(elt[0]+str(elt[1]))
            commande: Produit = self.stock.retirerProduit(id)
            if commande == None:
                reste: int = int(id[1])
                substitution: list[Produit] = []
                newId: str = id
                while reste > 0 and int(newId[1]) > 0:
                    if self.stock.isProduitEmpty(newId):
                        newId = str(newId[0]+str(int(newId[1])-1))
                    commande = self.stock.retirerProduit(newId)
                    if commande != None:
                        reste-=int(newId[1])
                        if reste >= 0:
                            substitution.append(commande)
                    
                if int(newId[1]) <= 0 or reste < 0:
                    print("Produit " + id + " indisponible")
                else:
                    reponse = str(input("Volume pour le produit " + id + " indisponible. Voulez vous séparer en plus petit volumes ?(o/n)"))
                    if reponse.lower() == 'o':
                        listeCommande+=substitution
                    else:
                        print("Produit " + id + " indisponible")
            else:
                listeCommande.append(commande)
        listeCommande.sort(key=lambda x: x.id()[1], reverse=True)
        for elt in listeCommande:
            colis.empiler(elt)
        colis.print()