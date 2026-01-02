from File import *

class FileProduits(File):
    def __init__(self, id:str):
        super().__init__()
        self.id:str=id

    def __str__(self):
        return str((self.id,self.size()))