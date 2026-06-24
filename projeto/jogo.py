import random
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
    
    def receber_dano(self, dano):
        self.__HP -= dano
        if self.__HP < 0:
            self.__HP = 0
    
    def ataque(self, alvo):
        dano = random.randint(self.get_nivel_de_luz() * 2, self.get_nivel_de_luz() * 4)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e deu {dano} de dano")
    
   
    
class Hunter(Personagem):
    def __init__(self, nome, nivel_de_luz, HP, Habilidade_Suprema):
        super().__init__(nome, nivel_de_luz, HP)
        self.__Habilidade_Suprema = Habilidade_Suprema
    
    def get_Habilidade_Suprema(self):
        return self.__Habilidade_Suprema
    
    def mais_detalhes(self):
        return f"{super().mais_detalhes()}\nHabilidade_Suprema: {self.get_Habilidade_Suprema()}\n"

    def Super(self, alvo):
        dano = random.randint(self.get_nivel_de_luz() * 4, self.get_nivel_de_luz()* 7) # Aumento de dano
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} usou o {self.get_Habilidade_Suprema()} no {alvo.get_nome()} e causou {dano} de dano")
    

class Cabal(Personagem):
    def __init__(self, nome, nivel_de_luz, HP, tipo):
        super().__init__(nome, nivel_de_luz, HP)
        self.__tipo = tipo

    def mais_detalhes(self):
        return f"{super().mais_detalhes()}\nTipo: {self.get_tipo()}\n"

    def get_tipo(self):
        return self.__tipo
    

Guardiao = Hunter(nome="Cacador", HP=200, nivel_de_luz=50, Habilidade_Suprema="Tiro certeiro")
print(Guardiao.mais_detalhes())
Inimigo = Cabal(nome="Cabal", HP=250, nivel_de_luz=25, tipo="Prismatico")
print(Inimigo.mais_detalhes())


# Classe orquestradora
class Jogo:

    def __init__(self):
        self.Guardiao = Hunter(nome="Cacador", HP=60, nivel_de_luz=5, Habilidade_Suprema="Tiro certeiro")
        self.Cabal = Cabal(nome="Cabal", HP=70, nivel_de_luz=4, tipo="Prismatico")
     
    def iniciar_assalto(self):
        print("Iniciando Assalto")
        while self.Guardiao.get_HP() > 0 and self.Cabal.get_HP() > 0:
            print("\nDetalhes dos Guardioes")
            print(self.Guardiao.mais_detalhes())
            print(self.Cabal.mais_detalhes())

            input("Precione enter para selecionar o Golpe desejado...")
            choice = input("Escolha (1- Ataque Basico, 2- Habilidade suprema): ")
        
            if choice == "1":
                self.Guardiao.ataque(self.Cabal)
            elif choice == "2":
                self.Guardiao.Super(self.Cabal)
            else:
                print("Escolha invalida, escolha novamente")

            if self.Cabal.get_HP() > 0:
                # Ataque do inimigo
                self.Cabal.ataque(self.Guardiao)

        if self.Guardiao.get_HP() > 0:
            print("Honrosa vitoria Guardiao")
        else:
            print("\nBater em retirada guardiao, perdemos a luta mas nao a batalha")

# Criando instancia para iniciar
jogo = Jogo()
jogo.iniciar_assalto()