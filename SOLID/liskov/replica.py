class Veiculo:
    def acelerar(self):
        print("Acelerando...")

class Carro(Veiculo): 
    def acelerar(self):
        print("Acelerando como um carro...")

def programa(veiculo: Veiculo):
    veiculo.acelerar()

carro = Carro()
programa(carro)

# Carro herda de veiculo suas propriedades sendo capaz de ser usado como parametro em uma função onde espera um veiculo
# Este é o principio da substituição de liskov