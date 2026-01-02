from Stockage import *
from Produit import *
from Pile import Pile

SEUIL_STOCK = 3
LOG_SIZE = 3


class GestionDeStock:
    """Gestionnaire principal du stock et des commandes.

    Ce gestionnaire initialise le stockage, permet d'afficher l'état,
    d'entrer rapidement des produits et de traiter une commande saisie
    par l'utilisateur.
    """

    def __init__(self, stock):
        """Initialiser le stockage avec une chaîne d'entrée initiale.

        Le paramètre `stock` est une chaîne au format "A1, B2, C3".
        """
        self.stock: Stockage = Stockage(SEUIL_STOCK)
        self.entreeRapide(stock)

    def afficherStock(self):
        """Afficher le contenu du stockage."""
        self.stock.afficher()

    def afficherJournal(self):
        """Afficher le journal des événements stockés."""
        self.stock.journal.afficherLog()

    def separerProduitEtVolume(self, entree: str) -> list:
        """Convertir une chaîne d'entrée en liste de tuples (type, volume).

        Exemple: 'A1, A2' -> [('A', 1), ('A', 2)].
        """
        entree = entree.split(', ')
        sortie = []
        for elt in entree:
            typeProduit = elt[0]
            volume = elt.removeprefix(typeProduit)
            sortie.append((typeProduit, int(volume)))
        return sortie

    def entreeRapide(self, entree: str):
        """Ajouter rapidement plusieurs produits décrits par une chaîne."""
        for typeProduit, volume in self.separerProduitEtVolume(entree):
            produits = Produit(typeProduit, volume)
            self.stock.ajouterProduit(produits)

    def commander(self):
        """Traiter une commande saisie par l'utilisateur.

        Le format attendu est une chaîne comme 'C3' ou 'A1, B2'. Si le
        produit demandé n'existe pas en un seul lot, la méthode tente de
        trouver une combinaison exacte de lots plus petits et propose à
        l'utilisateur de l'accepter.
        """
        colis = Pile()
        print("Ecrivez votre commande")
        entree = str(input())
        if not entree:
            return 
        listeProduit = self.separerProduitEtVolume(entree)
        listeCommande = []
        for typeProduit, volume in listeProduit:
            id_str = typeProduit + str(volume)
            commande: Produit = self.stock.retirerProduit(id_str)
            if commande is None:
                def find_combination(remaining, max_v):
                    if remaining == 0:
                        return []
                    if max_v == 0:
                        return None
                    for v in range(min(max_v, remaining), 0, -1):
                        prod = self.stock.retirerProduit(typeProduit + str(v))
                        if prod is None:
                            continue
                        rest = find_combination(remaining - v, v)
                        if rest is not None:
                            return [prod] + rest
                        self.stock.ajouterProduit(prod)
                    return None

                substitution = find_combination(volume, volume - 1)
                if substitution is None:
                    print("Produit " + id_str + " indisponible")
                else:
                    reponse = str(input("Volume pour le produit " + id_str + " indisponible. Voulez vous séparer en plus petit volumes ?(o/n)"))
                    if reponse.lower() == 'o':
                        listeCommande += substitution
                    else:
                        for p in substitution:
                            self.stock.ajouterProduit(p)
                        print("Produit " + id_str + " indisponible")
            else:
                listeCommande.append(commande)

        listeCommande.sort(key=lambda x: x.getVolume(), reverse=True)
        for elt in listeCommande:
            colis.empiler(elt)
        colis.print()