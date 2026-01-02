class Produit:
    def __init__(self, typeProduit:str, volume:int):
        self.typeProduit=typeProduit
        self.volume=volume
    
    def id(self)->str:
        return self.typeProduit + str(self.volume)
    
    def __str__(self)->str:
        return self.id()
    
    def getTypeProduit(self):
        return self.typeProduit
    
    def getVolume(self):
        return self.volume