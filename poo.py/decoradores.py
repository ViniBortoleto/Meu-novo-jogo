def decorador(func):
    def wrapper():
        print("Antes do decorador")
        func()
        print("depois do decorador")
    return wrapper


@decorador    
def funcao():
    print("Chamando funcao")

funcao()

class DecoradorDeClasse:
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        print("Antes do decorador funcionar")
        self.func()
        print("Depois do decorador funcionar")

@DecoradorDeClasse    
def outra_funcao():
    print("Segunda funcao funcionando")

outra_funcao()
