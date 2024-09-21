class Forma:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("Deve ser implementado pela subclasse")

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return 0.5 * self.base * self.altura

# Criação de objetos
circulo = Circulo(5)
retangulo = Retangulo(4, 5)
triangulo = Triangulo(3, 4)

# Cálculo da área
print(circulo.area())
print(retangulo.area())
print(triangulo.area())