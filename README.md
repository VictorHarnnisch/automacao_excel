# automacao_excel
Sistema simples de Automação no Excel com 2 ou mais tabelas
# 📊 Automação de Excel com Python e Pandas

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Openpyxl](https://img.shields.io/badge/Openpyxl-%23007944.svg?style=for-the-badge&logo=openpyxl&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## ✨ Visão Geral do Projeto

Este projeto consiste em um conjunto de scripts Python desenvolvidos para automatizar tarefas de manipulação de dados em arquivos Excel. O foco principal é ler dados de duas ou mais tabelas, realizar operações de combinação e transformação utilizando a poderosa biblioteca Pandas, e gerar um relatório consolidado. Este relatório pode, posteriormente, servir como base para a criação de dashboards para visualização e análise de dados.

## ⚙️ Funcionalidades Principais

* **Leitura de dados:** Capacidade de ler dados de arquivos Excel (`.xlsx`) utilizando a biblioteca Pandas.
* **Geração de dados de teste:** Script dedicado para criar arquivos Excel de exemplo (`vendas.xlsx` e `produtos.xlsx`) para testes e desenvolvimento.
* **Merge de tabelas:** Utiliza a função `pd.merge()` do Pandas para combinar dados de diferentes tabelas com base em colunas em comum (por exemplo, `ID_Produto`).
* **Cálculo de métricas:** Exemplo de cálculo do valor total da venda, demonstrando a capacidade de criar novas colunas e realizar operações com os dados.
* **Geração de relatório:** Salva o DataFrame resultante (o relatório combinado) em um novo arquivo Excel (`relatorio_vendas_produtos.xlsx`).
* **Flexibilidade:** A estrutura do código permite fácil adaptação para diferentes cenários de combinação e transformação de dados, dependendo das suas necessidades específicas.

## 🛠️ Pré-requisitos

Antes de executar os scripts, certifique-se de ter o seguinte instalado no seu sistema:

* **Python:** Versão 3.7 ou superior. Você pode baixar o Python em [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **Bibliotecas Python:** As seguintes bibliotecas são necessárias e podem ser instaladas usando o `pip`:
    ```bash
    pip install pandas openpyxl numpy
    ```
    * `pandas`: Para manipulação e análise de dados tabulares.
    * `openpyxl`: Necessário para ler e escrever arquivos Excel no formato `.xlsx`.
    * `numpy`: Usado para geração de dados aleatórios no script de teste.

## 💾 Instalação

1.  **Clone o repositório (se aplicável):** Se você estiver usando o GitHub, clone o repositório para o seu computador:
    ```bash
    git clone [https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd [nome do diretório do projeto]
    ```
3.  **Instale as dependências:** Caso ainda não tenha feito, instale as bibliotecas Python necessárias:
    ```bash
    pip install -r requirements.txt  # Se você tiver um arquivo requirements.txt
    # Ou instale individualmente:
    pip install pandas openpyxl numpy
    ```

## 🚀 Como Usar

1.  **Gerar dados de teste (opcional):**
    * Execute o script `gerar_dados.py` para criar os arquivos `vendas.xlsx` e `produtos.xlsx` com dados de exemplo.
        ```bash
        python gerar_dados.py
        ```
    * Esses arquivos serão criados no mesmo diretório onde o script `gerar_dados.py` está localizado.

2.  **Executar a automação:**
    * Execute o script `automacao_excel.py` para ler os arquivos de vendas e produtos, realizar o merge e gerar o relatório.
        ```bash
        python automacao_excel.py
        ```
    * O arquivo de relatório `relatorio_vendas_produtos.xlsx` será salvo no local especificado na variável `arquivo_relatorio` dentro do script `automacao_excel.py`. Por padrão, ele salva na pasta `relatorio_excel` na unidade `B:`.

## 📂 Estrutura de Arquivos

Markdown

# 📊 Automação de Excel com Python e Pandas

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Openpyxl](https://img.shields.io/badge/Openpyxl-%23007944.svg?style=for-the-badge&logo=openpyxl&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## ✨ Visão Geral do Projeto

Este projeto consiste em um conjunto de scripts Python desenvolvidos para automatizar tarefas de manipulação de dados em arquivos Excel. O foco principal é ler dados de duas ou mais tabelas, realizar operações de combinação e transformação utilizando a poderosa biblioteca Pandas, e gerar um relatório consolidado. Este relatório pode, posteriormente, servir como base para a criação de dashboards para visualização e análise de dados.

## ⚙️ Funcionalidades Principais

* **Leitura de dados:** Capacidade de ler dados de arquivos Excel (`.xlsx`) utilizando a biblioteca Pandas.
* **Geração de dados de teste:** Script dedicado para criar arquivos Excel de exemplo (`vendas.xlsx` e `produtos.xlsx`) para testes e desenvolvimento.
* **Merge de tabelas:** Utiliza a função `pd.merge()` do Pandas para combinar dados de diferentes tabelas com base em colunas em comum (por exemplo, `ID_Produto`).
* **Cálculo de métricas:** Exemplo de cálculo do valor total da venda, demonstrando a capacidade de criar novas colunas e realizar operações com os dados.
* **Geração de relatório:** Salva o DataFrame resultante (o relatório combinado) em um novo arquivo Excel (`relatorio_vendas_produtos.xlsx`).
* **Flexibilidade:** A estrutura do código permite fácil adaptação para diferentes cenários de combinação e transformação de dados, dependendo das suas necessidades específicas.

## 🛠️ Pré-requisitos

Antes de executar os scripts, certifique-se de ter o seguinte instalado no seu sistema:

* **Python:** Versão 3.7 ou superior. Você pode baixar o Python em [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **Bibliotecas Python:** As seguintes bibliotecas são necessárias e podem ser instaladas usando o `pip`:
    ```bash
    pip install pandas openpyxl numpy
    ```
    * `pandas`: Para manipulação e análise de dados tabulares.
    * `openpyxl`: Necessário para ler e escrever arquivos Excel no formato `.xlsx`.
    * `numpy`: Usado para geração de dados aleatórios no script de teste.

## 💾 Instalação

1.  **Clone o repositório (se aplicável):** Se você estiver usando o GitHub, clone o repositório para o seu computador:
    ```bash
    git clone [https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)
    ```
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd [nome do diretório do projeto]
    ```
3.  **Instale as dependências:** Caso ainda não tenha feito, instale as bibliotecas Python necessárias:
    ```bash
    pip install -r requirements.txt  # Se você tiver um arquivo requirements.txt
    # Ou instale individualmente:
    pip install pandas openpyxl numpy
    ```

## 🚀 Como Usar

1.  **Gerar dados de teste (opcional):**
    * Execute o script `gerar_dados.py` para criar os arquivos `vendas.xlsx` e `produtos.xlsx` com dados de exemplo.
        ```bash
        python gerar_dados.py
        ```
    * Esses arquivos serão criados no mesmo diretório onde o script `gerar_dados.py` está localizado.

2.  **Executar a automação:**
    * Execute o script `automacao_excel.py` para ler os arquivos de vendas e produtos, realizar o merge e gerar o relatório.
        ```bash
        python automacao_excel.py
        ```
    * O arquivo de relatório `relatorio_vendas_produtos.xlsx` será salvo no local especificado na variável `arquivo_relatorio` dentro do script `automacao_excel.py`. Por padrão, ele salva na pasta `relatorio_excel` na unidade `B:`.

## 📂 Estrutura de Arquivos

.
├── gerar_dados.py               #Script para gerar arquivos Excel de teste (vendas.xlsx, produtos.xlsx)<br/>
├── automacao_excel.py           # Script principal para realizar a automação e gerar o relatório<br/>
├── relatorio_excel/             # Pasta onde o relatório é salvo (configurado no script)<br/>
│ └── relatorio_vendas_produtos.xlsx<br/>
├── vendas.xlsx                  # Arquivo de dados de vendas (gerado por gerar_dados.py)<br/>
├── produtos.xlsx                # Arquivo de dados de produtos (gerado por gerar_dados.py)<br/>
└── README.md                    # Este arquivo com a descrição do projeto<br/>


## 💡 Próximos Passos e Contribuições

Este projeto pode ser expandido com diversas funcionalidades, como:

* **Leitura de múltiplos arquivos:** Permitir a leitura de dados de várias planilhas ou arquivos Excel.
* **Transformações de dados mais complexas:** Implementar filtros, agregações, cálculos personalizados e outras manipulações de dados.
* **Formatação do relatório:** Adicionar formatação condicional, estilos de células e gráficos ao arquivo de relatório.
* **Integração com outras fontes de dados:** Ler dados de bancos de dados, arquivos CSV, etc.
* **Criação de dashboards:** Utilizar bibliotecas como `plotly Dash` ou `Streamlit` para criar dashboards interativos a partir dos dados gerados.

Contribuições são bem-vindas! Se você tiver ideias para melhorias ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## ✍️ Autor

* harnisch, Victor

---
