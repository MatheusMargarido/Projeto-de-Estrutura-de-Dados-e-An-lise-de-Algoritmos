# 🚚 Otimização Logística com Múltiplos Centros de Distribuição

## 📋 Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação para **otimização logística**, utilizando **estruturas de dados e algoritmos eficientes**. O sistema calcula as melhores rotas de entrega a partir de múltiplos **Centros de Distribuição (CDs)**, respeitando restrições operacionais como capacidade dos veículos, limite de horas de operação e prazos de entrega.

O algoritmo central implementado é o **Dijkstra**, otimizado com **fila de prioridade (heap)**, garantindo eficiência na seleção das rotas de menor custo.

---

## 🚀 Funcionalidades

* Cálculo da **rota ótima** com base em distância, tempo e custos.
* **Seleção automática** do centro de distribuição mais próximo.
* Alocação do **veículo mais adequado** conforme capacidade e tempo máximo de operação.
* Análise de **cenários diversos**: melhor caso, caso médio e pior caso.
* Cálculo detalhado de custos: **combustível** e **pedágios**.
* Verificação do **cumprimento do prazo** de entrega.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* Estruturas de Dados: Lista de Adjacência, Fila de Prioridade (Heap), Dicionários, Listas.
* Bibliotecas padrão:

  * `heapq`
  * `datetime`

---

## 📂 Estrutura do Projeto

```
otimizacao_logistica/
├── main.py
├── utils/
│   ├── grafo.py
│   ├── calculos.py
│   └── veiculo.py
├── data/
│   ├── entradas.py
│   └── constantes.py
├── processamento/
│   └── cenario.py
├── README.md
```

---

## 🏁 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/MatheusMargarido/otimizacao_logistica
```

2. Acesse a pasta do projeto:

```bash
cd otimizacao_logistica
```

3. Execute a aplicação:

```bash
python -m main
```

> ✅ **Dica:** Execute sempre a partir da raiz do projeto, utilizando o modo `-m` para evitar problemas de importação.

---

## 📊 Cenários Testados

* **Melhor Caso:** 40 encomendas para Torres.
* **Caso Médio:** 100 encomendas, Osório e Tramandaí.
* **Pior Caso:** 300 encomendas, Porto Alegre e Rosário do Sul.

---
