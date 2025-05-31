cds = ["Belém", "Recife", "Brasília", "São Paulo", "Florianópolis"]

distancias = {
    ("São Paulo", "Torres"): (950, 12),
    ("Brasília", "Torres"): (1900, 24),
    ("Recife", "Torres"): (3600, 49),
    ("Belém", "Torres"): (3800, 50),
    ("Florianópolis", "Torres"): (280, 4),
    ("São Paulo", "Osório"): (1000, 13),
    ("Brasília", "Osório"): (2000, 25),
    ("Recife", "Osório"): (3700, 50),
    ("Belém", "Osório"): (3900, 51),
    ("Florianópolis", "Osório"): (360, 5),
    ("Osório", "Tramandaí"): (22, 0.5),
    ("São Paulo", "Porto Alegre"): (1150, 14),
    ("Brasília", "Porto Alegre"): (2100, 26),
    ("Recife", "Porto Alegre"): (3800, 51),
    ("Belém", "Porto Alegre"): (4000, 52),
    ("Florianópolis", "Porto Alegre"): (490, 6),
    ("Porto Alegre", "Rosário do Sul"): (400, 5),
}

veiculos = {
    "Furgão": {"capacidade_t": 2, "consumo_km_l": 9, "max_operating_hours": 11},
    "Caminhão Médio": {"capacidade_t": 6, "consumo_km_l": 5, "max_operating_hours": 11},
    "Caminhão Grande": {"capacidade_t": 10, "consumo_km_l": 3.5, "max_operating_hours": 11},
}

entregas = {
    "Melhor Caso = (40 Encomendas em Torres)": {
        "destinos": ["Torres"],
        "carga_t": 1.5,
        "pedagios": 5,
        "valor_pedagio": 4.50,
        "rota_descricao": "BR-101 de Florianópolis à Torres",
        "data_saida": "05/06/2025",
        "dias_uteis": 1,
    },
    "Caso Médio = 100 Encomendas sendo (50 em Osório > 50 em Tramandaí)": {
        "destinos": ["Osório", "Tramandaí"],
        "carga_t": 5,
        "pedagios": 6,
        "valor_pedagio": 7.50,
        "rota_descricao": "BR-101 de Florianópolis à Osório e RS-030 de Osório até Tramandaí",
        "data_saida": "15/06/2025",
        "dias_uteis": 1,
    },
    "Pior Caso = 300 Encomendas sendo (200 em Porto Alegre > 100 em Rosário do Sul)": {
        "destinos": ["Porto Alegre", "Rosário do Sul"],
        "carga_t": 9,
        "pedagios": 8,
        "valor_pedagio": 11.50,
        "rota_descricao": "BR-101 de Florianópolis à Porto Alegre e BR-290 de Porto Alegre até Rosário do Sul",
        "data_saida": "20/06/2025",
        "dias_uteis": 2,
    },
}
