# Datathon – Case Passos Mágicos

Isabela Marim Mayerhoffer Pereira - RM 362023

Lucas Constantino Silva - RM 364620

Pedro Bugui Garcia - RM 360783

Sophia Yeshua Senra - RM 362887

Link da apresentação: 


## Introdução

...

## Estrutura do Projeto

```
📁 Datathon/
│
├── 📂 bases/
│   ├── fat_datathon.xlsx           # Base de dados
│   └── fat_datathon_tratado.csv    # Base de dados limpa e tratada para uso no modelo
|
├── 📂 notebooks/
│   ├── tc5_tratamento_dados.ipynb  # Notebook de tratamento das bases iniciais
│   ├── tc5_indicadores.ipynb       # Notebook de resolução dos indicadores 1-8 e 10
│   └── tc5_indicador_9.ipynb       # Notebook de modelo para resolução do indicador 9
│
├── 📄 app.py                       # Aplicação principal em Streamlit
│                                   Responsável pela interface interativa e predição do nível de risco
│
├── 📄 modelo_xgb.joblib            # Modelo Random Forest treinado e exportado
│                                   Carregado pelo app Streamlit para realizar previsões em tempo real
│
├── 📄 requirements.txt             # Lista de dependências e versões utilizadas no projeto
│                                   Permite recriar o ambiente necessário para execução
|
├── 📄 utils.py                     # Arquivo de funções auxiliares e pipeline
│                                   Inclui:
│                                     - Pré-processamento dos dados de entrada
│                                     - Normalização de variáveis quantitativas
│                                     - Codificação de variáveis categóricas
│
└── 📄 README.md                    # Documentação do projeto

```

## Conclusão

...

