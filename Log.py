import Stockage
from File import *
from Produit import *

class Log:
    def __init__(self, size: int, stock: Stockage):
        self.stock = stock
        self.log = File()
        self.LOG_SIZE = size
    
    def ajoutLog(self,message:str):
        if self.log.size()>=self.LOG_SIZE:
            self.gererLog()
        self.log.enfiler(message)
        
    def afficherLog(self):
        self.log.print()
        print("-----------------------------")
    
    def isLogPlein(self)->bool:
        return self.log.size()==self.LOG_SIZE
    
    def viderLog(self):
        self.log.vider()
        
    def gererLog(self):
        pass
#         for i in range(self.log.size()-1):
#             log=self.log.defiler()
#             id: str = log.split(" ")[1]
#             produit: Produit = Produit(id[0], id[1])
#             self.stock.ajouterProduit(produit)