def calcular_preco_medio(transacoes):
    quantidade_atual = 0
    preco_medio_atual = 0

    for transacao in transacoes:
        if transacao.tipo == "COMPRA":
            preco_medio_atual = (
                (quantidade_atual * preco_medio_atual) + (transacao.quantidade * transacao.preco)
            ) / (quantidade_atual + transacao.quantidade)
            quantidade_atual += transacao.quantidade
        else:  # VENDA
            quantidade_atual -= transacao.quantidade

    return quantidade_atual, preco_medio_atual