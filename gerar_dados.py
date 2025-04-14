import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# --- Gerando dados para produtos.xlsx ---
num_produtos = 200
ids_produtos = [f'PROD_{i+1:03d}' for i in range(num_produtos)]
nomes_produtos = [f'Produto {i+1}' for i in range(num_produtos)]
categorias = ['Eletrônicos', 'Livros', 'Roupas', 'Alimentos', 'Ferramentas']
categorias_produtos = [random.choice(categorias) for _ in range(num_produtos)]

df_produtos = pd.DataFrame({
    'ID_Produto': ids_produtos,
    'Nome_Produto': nomes_produtos,
    'Categoria': categorias_produtos
})

# Salvar o DataFrame em produtos.xlsx
nome_arquivo_produtos = 'produtos.xlsx'
try:
    df_produtos.to_excel(nome_arquivo_produtos, index=False)
    print(f"Arquivo '{nome_arquivo_produtos}' criado com sucesso!")
except Exception as e:
    print(f"Erro ao salvar o arquivo '{nome_arquivo_produtos}': {e}")

# --- Gerando dados para vendas.xlsx ---
num_vendas = 200
# Vamos usar os mesmos IDs de produtos para simular vendas
ids_vendas = random.choices(ids_produtos, k=num_vendas)

# Gerar datas de venda aleatórias dentro de um período
data_inicio = datetime(2024, 1, 1)
data_fim = datetime(2024, 12, 31)
datas_vendas = [data_inicio + timedelta(days=random.randint(0, (data_fim - data_inicio).days)) for _ in range(num_vendas)]

quantidades = np.random.randint(1, 10, size=num_vendas)
valores_unitarios = np.random.uniform(10.0, 100.0, size=num_vendas).round(2)

df_vendas = pd.DataFrame({
    'ID_Produto': ids_vendas,
    'Data_Venda': datas_vendas,
    'Quantidade': quantidades,
    'Valor_Unitario': valores_unitarios
})

# Salvar o DataFrame em vendas.xlsx
nome_arquivo_vendas = 'vendas.xlsx'
try:
    df_vendas.to_excel(nome_arquivo_vendas, index=False)
    print(f"Arquivo '{nome_arquivo_vendas}' criado com sucesso!")
except Exception as e:
    print(f"Erro ao salvar o arquivo '{nome_arquivo_vendas}': {e}")

print("\nOs arquivos 'vendas.xlsx' e 'produtos.xlsx' foram criados com 200 registros cada.")
print("O arquivo 'relatorio_vendas_produtos.xlsx' será gerado quando rodarmos a automação de merge.")