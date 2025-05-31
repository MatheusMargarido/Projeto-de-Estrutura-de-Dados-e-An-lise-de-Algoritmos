from datetime import timedelta

def calcular_custo(distancia, consumo, preco_diesel):
    return (distancia / consumo) * preco_diesel

def calcular_chegada(hora_partida, horas_de_viagem):
    return hora_partida + timedelta(hours=horas_de_viagem)
