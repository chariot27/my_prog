class Forma:
    def __init__(self, tipo):
        self.tipo = tipo

    def area(self):
        if self.tipo == 'circulo':
            return 3.14 * (5 ** 2)
        elif self.tipo == 'retangulo':
            return 4 * 5
        elif self.tipo == 'triangulo':
            return 0.5 * 3 * 4
        else:
            raise ValueError("Tipo de forma não suportado")

# Criação de objetos
circulo = Forma('circulo')
retangulo = Forma('retangulo')
triangulo = Forma('triangulo')

# Cálculo da área
print(circulo.area())
print(retangulo.area())
print(triangulo.area())