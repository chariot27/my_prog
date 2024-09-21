class Veiculo:
    def acelerar(self):
        print("Acelerando...")

class Carro(Veiculo):
    def acelerar(self):
        print("Acelerando como um carro...")

def programa(veiculo: Veiculo):
    veiculo.acelerar()

carro = Carro()
programa(carro)  # Deve imprimir "Acelerando como um carro..."