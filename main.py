from utils.grafo import build_graph
from processamento.cenario import processar_cenario
from data.entradas import distancias, entregas

def main():
    graph = build_graph(distancias)
    for nome_cenario, dados in entregas.items():
        processar_cenario(nome_cenario, dados, graph)

if __name__ == "__main__":
    main()
