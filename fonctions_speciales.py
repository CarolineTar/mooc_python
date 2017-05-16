class Protege:
    def __init__(self):
        self.a="mister"
        self.b="blake"
    def __getattr__(self, nom):
        print("il faut bien que j'essaye !", self.a, self.b, nom)
    def __repr__(self):
        return("c'est donc toi {} {}".format(self.a, self.b))
