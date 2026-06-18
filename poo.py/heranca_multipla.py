
class bicho:
    def __init__(self, nome):
        self.nome = nome

    def sons(self):
        pass

class mamiferos(bicho):
    def amamentar(self):
        return f"{self.nome} esta amamentando."
    
class voadores(bicho):
    def voar(self):
        return f"{self.nome} esta voando."
    
class Morcego(mamiferos, voadores):
    def sons(self):
         return "Morcego emite sons ultrassonicos"
    
morcego = Morcego(nome="Sonar")

# Acessando tipos de classe com a base "Animal"
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.sons())

# Acessando as classes mamiferos voadores
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())
    