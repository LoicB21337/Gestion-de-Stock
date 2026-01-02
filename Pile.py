class Pile:
    def __init__(self):
        self.pile=[]
    def isEmpty(self):
        return self.pile == []
    def size(self):
        return len(self.pile)
    def print(self):
        self.pile.reverse()
        for e in self.pile:
            print(e)
        self.pile.reverse()
    def empiler(self, n):
        self.pile.append(n)
    def depiler(self):
        if not self.isEmpty():
            return self.pile.pop(-1)
        else:
            return None