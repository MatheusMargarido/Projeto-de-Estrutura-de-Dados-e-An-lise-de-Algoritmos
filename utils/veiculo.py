def escolher_veiculo(veiculos, carga):
    for tipo, info in veiculos.items():
        if carga <= info["capacidade_t"]:
            return {
                "tipo": tipo,
                "capacidade": info["capacidade_t"],
                "consumo": info["consumo_km_l"],
                "max_operating_hours": info["max_operating_hours"]
            }
    return None
