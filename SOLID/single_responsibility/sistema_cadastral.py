class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome,idade):
            self.__armazenar_dados(nome,idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_dados(self, nome: str, idade: int) -> None:
        print('acessando banco de dados...')
        print('Cadastrar o Usuario {}, Idade {}'.format(nome, idade))

    def __indicar_erro(self):
        print('dados invalidos')