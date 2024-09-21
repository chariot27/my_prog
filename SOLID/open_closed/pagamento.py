class Pagamento:
    def __init__(self, tipo_pagamento):
        self.tipo_pagamento = tipo_pagamento

    def processar_pagamento(self):
        if self.tipo_pagamento == 'cartao_de_credito':
            return "Processando pagamento com cartão de crédito"
        elif self.tipo_pagamento == 'boleto':
            return "Processando pagamento com boleto"
        elif self.tipo_pagamento == 'paypal':
            return "Processando pagamento com PayPal"
        else:
            raise ValueError("Tipo de pagamento não suportado")

# Criação de objetos
pagamento_cartao = Pagamento('cartao_de_credito')
pagamento_boleto = Pagamento('boleto')
pagamento_paypal = Pagamento('paypal')

# Processamento de pagamento
print(pagamento_cartao.processar_pagamento())
print(pagamento_boleto.processar_pagamento())
print(pagamento_paypal.processar_pagamento())