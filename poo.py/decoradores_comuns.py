# @classmethod
# @staticmethod

class NovaClasse:
    valor = 7 # Atributo da classe

    def __init__(self, nome):
        self.nome = nome # atributo da instancia
        
    # Requer instancia para ser chamado    
    def instancia(self):
        return f"Metodo de instancia Chamado para {self.nome}"
    
    @classmethod
    def classe(cls):
        return f"Metodo de classe chamado para valor {cls.valor}"
    
    @staticmethod
    def estatico():
        return "Modo estatico chamado"

    
obj = NovaClasse(nome="Cavaleiro")
print(obj.instancia())
print(NovaClasse.valor)
print(NovaClasse.classe())
print(NovaClasse.estatico())


class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def montar_carro(cls, config):
        marca, modelo, ano = config.split(",")
        return cls(marca, modelo, int(ano))


config1 = "Toyota,Supra,2002"
carro1 = carro.montar_carro(config1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno {carro1.ano}")

class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b
print(Matematica.somar(a=37, b=48))