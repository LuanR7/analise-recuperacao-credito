
import pandas as pd
import random

random.seed(42)

clientes = []

for cliente_id in range(1, 1001):
    valor_divida = random.randint(500, 15000)
    dias_atraso = random.randint(1, 360)

    taxa_base = max(0.10, 0.60 - dias_atraso / 700)
    taxa_recuperacao = random.uniform(taxa_base * 0.5, taxa_base * 1.2)

    valor_recuperado = round(valor_divida * taxa_recuperacao, 2)

    clientes.append({
        "cliente_id": cliente_id,
        "valor_divida": valor_divida,
        "dias_atraso": dias_atraso,
        "valor_recuperado": valor_recuperado
    })

df = pd.DataFrame(clientes)

df.to_csv("carteira_npl.csv", index=False)

print("Base com 1.000 clientes criada!")
print(df.head())
