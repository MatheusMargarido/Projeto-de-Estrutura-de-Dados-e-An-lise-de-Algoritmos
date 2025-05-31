from datetime import datetime

hora_partida = datetime.strptime("08:00", "%H:%M")
preco_diesel = 6.00

hora_limite_inicial = datetime.strptime("08:00", "%H:%M").time()
hora_limite_final = datetime.strptime("19:00", "%H:%M").time()
