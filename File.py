class File:
    def __init__(self):
        self.file = []
        
    def isEmpty(self):
        return self.file == []
    
    def vider(self):
        self.file = []
        
    def size(self):
        return len(self.file)
    
    def print(self):
        for e in self.file:
            print(e)
            
    def enfiler(self, n):
        self.file.append(n)
        
    def defiler(self):
        if not self.isEmpty():
            return self.file.pop(0)
        else:
            return None