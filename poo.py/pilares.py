

# Modulo 1. Heranca
print("\nTipos de heranca")
class animal:
    def __init__(self, nome):
        self.nome = nome

        def andar(self):
            print(f"O animal {self.nome} andou")
            return
        
        def sons(self):
            pass

# Polimorfismo
class Cachorro(animal):
    def sons(self):
        return "AU AU"
    
class Gato(animal):
    def sons(self):
        return "Miau Miau"
    

dog = Cachorro(nome= "Pitoco")
cat = Gato(nome= "Frajola")

print("\nTipos de polimorfismo")
animais = [dog, cat]
for animal in animais:
    print(f"{animal.nome} Faz: {animal.sons()}")

print("\n Tipos de encapsulamento:")
class ContaDoBanco:
    def __init__(self, saldo):
        self.__saldo = saldo #atributo unico
    
    def depositar(self, valor):
        if valor > 0:
           self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaDoBanco(saldo=3000)
print(f"Saldo da sua conta é: {conta.consultar_saldo()}")
conta.depositar(valor=300)
print(f"Saldo da sua conta é: {conta.consultar_saldo()}")
conta.sacar(valor=400)
print(f"Saldo da sua conta é: {conta.consultar_saldo()}")

# Abistracao
print("\nTipos de abstracao:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Voce desligou o carro"
    
class jetski(Veiculo):
    def __init__(self):
        pass

    def ligar(self):
        return "Voce pode andar no jetski"
    
    def desligar(self):
        return "Voce terminou a sua viagem"

peugeot_Prata = Carro()
print(peugeot_Prata.ligar())
print(peugeot_Prata.desligar())

kawasaki = jetski()
print(kawasaki.ligar())
print(kawasaki.desligar())