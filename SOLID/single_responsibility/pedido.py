class Pedido:
    def __init__(self, itens, total):
        self.itens = itens
        self.total = total

class Calcular_Total:
    def calcular_total(self):
        # calcular o total do pedido
        return sum(item['preco'] * item['quantidade'] for item in self.itens)

class Aplicar_Desconto:
    def aplicar_desconto(self, desconto):
        # aplicar um desconto no total do pedido
        return self.total * (1 - desconto / 100)

class Gerar_Fatura:
    def gerar_fatura(self):
        # gerar uma fatura para o pedido
        print("Gerando fatura...")
        print("Itens:")
        for item in self.itens:
            print(f"{item['nome']} x {item['quantidade']} = {item['preco'] * item['quantidade']}")
        print(f"Total: {self.total}")
        print(f"Desconto: {self.aplicar_desconto(10)}")

class Enviar_Fatura:
    def enviar_fatura_por_email(self):
        # enviar a fatura por email
        print("Enviando fatura por email...")