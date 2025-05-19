import pandas as pd

arquivo = "clientes_novaconecta.xlsx"

df = pd.read_excel(arquivo)

df_paises = df[df['País'] == 'Brasil']

pd.set_option('display.max_rows', None)

print(df_paises)