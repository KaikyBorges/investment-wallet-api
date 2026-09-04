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


def calcular_resumo_carteira(transacoes, precos_atuais):
    """
    transacoes: lista de TransacaoDB do usuário (todas, todos os tickers)
    precos_atuais: dict {ticker: preco} com os preços atuais cadastrados

    Retorna: patrimonio_total, total_investido, resultado, rentabilidade (%)
    """
    grupos = {}
    for t in transacoes:
        grupos.setdefault(t.ticker, []).append(t)

    patrimonio_total = 0.0
    total_investido = 0.0

    for ticker, transacoes_do_ticker in grupos.items():
        quantidade, preco_medio = calcular_preco_medio(transacoes_do_ticker)

        if quantidade <= 0:
            continue

        preco_atual = precos_atuais.get(ticker)
        if preco_atual is None:
            continue  # ignora ativos sem preço atual cadastrado

        patrimonio_total += quantidade * preco_atual
        total_investido += quantidade * preco_medio

    resultado = patrimonio_total - total_investido
    rentabilidade = (resultado / total_investido * 100) if total_investido > 0 else 0.0

    return {
        "patrimonio_total": round(patrimonio_total, 2),
        "total_investido": round(total_investido, 2),
        "resultado": round(resultado, 2),
        "rentabilidade_percentual": round(rentabilidade, 2)
    }