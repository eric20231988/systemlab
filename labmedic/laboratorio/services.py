from resultados_analitos.models import ResultadoAnalito

def validar_resultado(valor, analito):
    if valor < analito.valor_minimo or valor > analito.valor_maximo:
        return 'Fuera de rango'
    return 'Normal'

def registrar_resultado(registro_examen, analito, valor):
    estado = validar_resultado(valor, analito)
    resultado = ResultadoAnalito.objects.create(
        registro_examen=registro_examen,
        analito=analito,
        valor=valor,
        estado=estado
    )
    return resultado
