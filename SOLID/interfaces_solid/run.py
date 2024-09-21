from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangulo import TerrenoRetangular
from engenheiro import Engenheiro

engenheiro = Engenheiro('Max')
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangular(2,3)

engenheiro.medir_area(terrenoQuadrado)
engenheiro.medir_perimetro(terrenoQuadrado)

engenheiro.medir_area(terrenoRetangular)
engenheiro.medir_perimetro(terrenoRetangular)

# Interface Segregation Principle (Princípio de Segregação de Interface)

#Uma interface deve ser dividida em interfaces menores e mais específicas.
#Uma classe não deve ser forçada a implementar uma interface que não precisa.

