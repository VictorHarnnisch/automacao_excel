import pandas as pd

# Definir os nomes dos arquivos Excel
arquivo_vendas = 'vendas.xlsx'
arquivo_produtos = 'produtos.xlsx'
arquivo_relatorio = 'relatorio_vendas_produtos.xlsx'

# Ler as tabelas Excel para DataFrames do pandas
try:
    df_vendas = pd.read_excel(arquivo_vendas)
    df_produtos = pd.read_excel(arquivo_produtos)
except FileNotFoundError as e:
    print(f"Erro: Um dos arquivos não foi encontrado: {e}")
    exit()

# Exibir as primeiras linhas dos DataFrames para verificar a leitura (opcional)
print("DataFrame de Vendas:")
print(df_vendas.head())
print("\nDataFrame de Produtos:")
print(df_produtos.head())

# Realizar o merge (junção) das tabelas com base na coluna 'ID_Produto'
df_relatorio = pd.merge(df_vendas, df_produtos, on='ID_Produto', how='left')
# 'on='ID_Produto'' especifica a coluna de junção
# 'how='left'' garante que todas as vendas sejam mantidas, e as informações dos produtos correspondentes sejam adicionadas.

# Exibir as primeiras linhas do DataFrame resultante (relatório)
print("\nDataFrame do Relatório:")
print(df_relatorio.head())

# Calcular o valor total da venda (opcional)
df_relatorio['Valor_Total'] = df_relatorio['Quantidade'] * df_relatorio['Valor_Unitario']

# Salvar o DataFrame do relatório em um novo arquivo Excel
try:
    df_relatorio.to_excel(arquivo_relatorio, index=False) # index=False evita que o índice do DataFrame seja escrito no arquivo
    print(f"\nRelatório '{arquivo_relatorio}' gerado com sucesso!")
except Exception as e:
    print(f"Erro ao salvar o relatório: {e}")