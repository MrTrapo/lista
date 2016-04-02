class Persona:
    def __init__(self,nom,ed,ciu):
        self.nombre=nom.capitalize()
        self.edad=ed
        self.ciudad=ciu.capitalize()

    def nom(self):      
        return self.nombre

    def ed(self):       
        return self.edad

    def ciu(self):    
        print ("\n")
        return self.ciudad
    

    
