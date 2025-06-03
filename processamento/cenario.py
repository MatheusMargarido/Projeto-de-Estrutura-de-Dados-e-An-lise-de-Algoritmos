from utils.veiculo import escolher_veiculo
from utils.calculos import calcular_custo, calcular_chegada
from utils.grafo import dijkstra
from data.constantes import hora_partida, preco_diesel, hora_limite_inicial, hora_limite_final
from data.entradas import cds, veiculos

def processar_cenario(nome_cenario, dados_cenario, graph):
    print("\n" + "=" * 80)
    print(f"{nome_cenario.center(80)}")
    print("=" * 80)

    carga = dados_cenario["carga_t"]
    destinos = dados_cenario["destinos"]
    pedagios = dados_cenario["pedagios"]
    valor_pedagio = dados_cenario["valor_pedagio"]
    rota_descricao = dados_cenario["rota_descricao"]
    data_saida = dados_cenario["data_saida"]
    dias_uteis = dados_cenario["dias_uteis"]

    veiculo = escolher_veiculo(veiculos, carga)
    if veiculo is None:
        print(f"Nenhum veículo comporta a carga de {carga} toneladas.")
        return

    melhor_cd = None
    menor_custo_total = float('inf')
    melhor_rota_geral = []
    melhor_total_km = 0
    melhor_total_horas = 0

    for cd in cds:
        custo_total_cd = 0
        total_km = 0
        total_horas = 0
        rota_composta = []
        origem_atual = cd
        rota_valida = True

        for destino in destinos:
            distancia, duracao, path = dijkstra(graph, origem_atual, destino)
            if distancia is None:
                rota_valida = False
                break
            custo = calcular_custo(distancia, veiculo["consumo"], preco_diesel)
            custo_total_cd += custo
            total_km += distancia
            total_horas += duracao
            rota_composta.extend(path)
            origem_atual = destino

        if rota_valida and total_horas <= veiculo["max_operating_hours"]:
            if custo_total_cd < menor_custo_total:
                menor_custo_total = custo_total_cd
                melhor_cd = cd
                melhor_rota_geral = rota_composta
                melhor_total_km = total_km
                melhor_total_horas = total_horas

    if melhor_cd is None:
        print("Nenhum Centro de Distribuição gerou uma rota válida para este cenário.")
        return

    print(f"  ➤ Carga: {carga}t")
    print(f"  ➤ Veículo indicado: {veiculo['tipo']} ({veiculo['capacidade']}t)")
    print(f"  ➤ CD selecionado: {melhor_cd}")
    print(f"  ➤ Rota utilizada: {rota_descricao}")
    print(f"  ➤ Data e horário de saída: {data_saida} às 8h")
    print(f"  ➤ Prazo: {dias_uteis} dia(s) útil(is) para entregar até às 19h")
    print(f"  ➤ Consumo: {veiculo['consumo']} km/L | Custo por km: R$ {preco_diesel / veiculo['consumo']:.2f} | Preço diesel/L: R$ {preco_diesel:.2f}")

    hora_atual = hora_partida
    for origem, destino, dist_seg, dur_seg in melhor_rota_geral:
        chegada = calcular_chegada(hora_atual, dur_seg)
        custo_seg = calcular_custo(dist_seg, veiculo["consumo"], preco_diesel)
        print(f"\n  - Rota: {origem} → {destino}")
        print(f"    Distância: {dist_seg} km")
        print(f"    Horário de chegada: {chegada.strftime('%H:%M')}")
        print(f"    Duração: {dur_seg}h")
        print(f"    Custo de combustível: R$ {custo_seg:.2f}")
        hora_atual = chegada

    total_pedagio = pedagios * valor_pedagio
    custo_total_com_pedagio = menor_custo_total + total_pedagio

    print(f"\n  ➤ Total percorrido: {melhor_total_km} km")
    print(f"  ➤ Tempo total de viagem: {melhor_total_horas} horas")
    print(f"  ➤ Custo total de combustível: R$ {menor_custo_total:.2f}")

    print(f"\n  ➤ Pedágios:")
    print(f"    - Quantidade de pedágios: {pedagios}")
    print(f"    - Valor unitário de cada pedágio: R$ {valor_pedagio:.2f}")
    print(f"    - Total de pedágios: R$ {total_pedagio:.2f}")

    print(f"\n  ➤ Custo total (combustível + pedágios): R$ {custo_total_com_pedagio:.2f}")

    hora_chegada_final = hora_atual.time()
    if hora_chegada_final < hora_limite_inicial or hora_chegada_final > hora_limite_final:
        print(f"\n  ➤ Prazo NÃO cumprido! Última chegada às {hora_atual.strftime('%H:%M')}.")
    else:
        print(f"\n  ➤ Prazo de entrega cumprido! Última chegada às {hora_atual.strftime('%H:%M')} dentro do horário permitido.")

