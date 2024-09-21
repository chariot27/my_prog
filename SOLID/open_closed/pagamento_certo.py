class Pagamento:
    def __init__(self):
        pass

    def processar_pagamento(self):
        raise NotImplementedError("Deve ser implementado pela subclasse")

class PagamentoCartao:
    def processar_pagamento(self):
        return "Processando pagamento com cartão de crédito"

class PagamentoBoleto:
    def processar_pagamento(self):
        return "Processando pagamento com boleto"

class PagamentoPaypal:
    def processar_pagamento(self):
        return "Processando pagamento com PayPal"

cartao = PagamentoCartao()
boleto = PagamentoBoleto()
paypal = PagamentoPaypal()

print(cartao.processar_pagamento())
print(boleto.processar_pagamento())
print(paypal.processar_pagamento())