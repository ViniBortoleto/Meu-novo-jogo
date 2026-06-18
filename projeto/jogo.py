# Personagem: main class
# Hunter: usuario controla
# Cabal: controlado pelo usuario tambem

class Personagem:
    def __init__(self, nome, nivel_de_luz, HP):
        self.__nome = nome
        self.__nivel_de_luz = nivel_de_luz
        self.__HP = HP

    def get_nome(self):
        return self.__nome
    
    def get_nivel_de_luz(self):
        return self.__nivel_de_luz
    
    def get_HP(self):
        return self.__HP
    
    def mais_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_HP()}\nNivel de Luz: {self.get_nivel_de_luz()}"
    
class Hunter(Personagem):
    def __init__(self, nome, nivel_de_luz, HP, Habilidade_Suprema):
        super().__init__(nome, nivel_de_luz, HP)
        self.__Habilidade_Suprema = Habilidade_Suprema
    
    def get_Habilidade_Suprema(self):
        return self.__Habilidade_Suprema
    
    def mais_detalhes(self):
        return f"{super().mais_detalhes()}\nHabilidade_Suprema: {self.get_Habilidade_Suprema()}\n"
    

class Cabal(Personagem):
    def __init__(self, nome, nivel_de_luz, HP, tipo):
        super().__init__(nome, nivel_de_luz, HP)
        self.__tipo = tipo

    def mais_detalhes(self):
        return f"{super().mais_detalhes()}\nTipo: {self.get_tipo()}\n"

    def get_tipo(self):
        return self.__tipo
    
Guardiao = Hunter(nome="Cacador", HP=200, nivel_de_luz=100, Habilidade_Suprema="Tiro certeiro")
print(Guardiao.mais_detalhes())
Inimigo = Cabal(nome="Cabal", HP=250, nivel_de_luz=50, tipo="Prismatico")
print(Inimigo.mais_detalhes())