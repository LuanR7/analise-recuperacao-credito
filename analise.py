
import pandas as pd

# Ler a base de dados
df = pd.read_csv("carteira_npl.csv")

# Calcular indicadores
total_dividas = df["valor_divida"].sum()
total_recuperado = df["valor_recuperado"].sum()

saldo_devedor = total_dividas - total_recuperado

taxa_recuperacao = (
    total_recuperado / total_dividas
) * 100

# Exibir resultados
print("ANÁLISE DA CARTEIRA NPL")
print("-----------------------")

print(f"Total das dívidas: R$ {total_dividas:,.2f}")
print(f"Total recuperado: R$ {total_recuperado:,.2f}")
print(f"Saldo devedor: R$ {saldo_devedor:,.2f}")

print(f"Taxa de recuperação: {taxa_recuperacao:.2f}%")


# Criar uma coluna com a taxa de recuperação por cliente
df["taxa_recuperacao"] = (
    df["valor_recuperado"] / df["valor_divida"]
) * 100

# Ordenar os clientes pelo tempo de atraso
df_ordenado = df.sort_values(
    by="dias_atraso"
)

print("\nRECUPERAÇÃO POR CLIENTE")
print("-----------------------")

print(
    df_ordenado[
        [
            "cliente_id",
            "dias_atraso",
            "taxa_recuperacao"
        ]
    ].to_string(index=False)
)

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.bar(
    df_ordenado["dias_atraso"],
    df_ordenado["taxa_recuperacao"]
)

plt.title("Taxa de Recuperação por Dias de Atraso")
plt.xlabel("Dias de atraso")
plt.ylabel("Taxa de recuperação (%)")

plt.tight_layout()
plt.savefig("grafico_recuperacao.png", dpi=300, bbox_inches="tight") 
plt.show()
