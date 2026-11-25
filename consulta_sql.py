
import sqlite3
import pandas as pd

conexao = sqlite3.connect("carteira.db")

consulta = """
SELECT
    CASE
        WHEN dias_atraso <= 30 THEN '0 a 30 dias'
        WHEN dias_atraso <= 60 THEN '31 a 60 dias'
        WHEN dias_atraso <= 90 THEN '61 a 90 dias'
        ELSE 'Mais de 90 dias'
    END AS faixa_atraso,

    COUNT(*) AS quantidade_clientes,
    SUM(valor_divida) AS divida_total,
    SUM(valor_recuperado) AS total_recuperado,

    ROUND(
        SUM(valor_recuperado) * 100.0 / SUM(valor_divida), 2
    ) AS taxa_recuperacao

FROM carteira
GROUP BY faixa_atraso
ORDER BY MIN(dias_atraso);
"""

df = pd.read_sql_query(consulta, conexao)

print(df)

conexao.close()
