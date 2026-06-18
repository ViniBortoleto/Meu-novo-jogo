#POO


# Classes
class Humano:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return(f"Ola o meu nome é {self.nome} e eu tenho {self.idade} anos")

# Objetos
pessoa1 = Humano("Glauber", 27)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Humano("Giren", 47)
mensagem = pessoa2.saudacao()
print(mensagem)