class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

class Malabarista:
    def apresentar_show(self):
        print('\nmalabarista apresenta no seu show!')

class Palhaco:
    def apresentar_show(self):
        print('palhaço apresenta no seu show!')

class Domador:
    def apresentar_show(self):
        print('domador apresenta no seu show!')

circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
domador = Domador()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
circo.apresentar(domador)