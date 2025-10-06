def evaluar_estado(valor, analito):
    if valor < analito.valor_minimo:
        return 'bajo'
    elif valor > analito.valor_maximo:
        return 'alto'
    return 'normal'
