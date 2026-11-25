
import sqlite3
import pandas as pd

# Ler a base CSV
df = pd.read_csv("carteira_npl.csv")

# Criar conexão com o banco
conexao = sqlite3.connect("carteira.db")

# Enviar os dados para uma tabela SQL
df.to_sql(
    "carteira",
    conexao,
    if_exists="replace",
    index=False
)

print("Banco de dados criado com sucesso!")

# Fechar conexão
conexao.close()
  