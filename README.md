# Datathon – Case Passos Mágicos

Isabela Marim Mayerhoffer Pereira - RM 362023

Lucas Constantino Silva - RM 364620

Pedro Bugui Garcia - RM 360783

Sophia Yeshua Senra - RM 362887

Link da apresentação: 


## Introdução

A Associação Passos Mágicos é uma organização social que há mais de três décadas atua na transformação da vida de crianças e jovens em situação de vulnerabilidade social, especialmente no município de Embu-Guaçu. Criada a partir de uma iniciativa que começou em 1992 dentro de orfanatos, a instituição ampliou sua atuação ao longo dos anos e, em 2016, consolidou-se como um projeto social e educacional estruturado, oferecendo educação de qualidade, apoio psicológico e psicopedagógico, além de estimular o protagonismo e ampliar a visão de mundo dos participantes.
 
Neste contexto, o presente projeto tem como objetivo analisar dados educacionais coletados entre 2022 e 2024 para compreender o impacto e a efetividade do programa na trajetória dos alunos atendidos. A partir da análise de indicadores e do uso de técnicas de data analytics, busca-se identificar padrões, avaliar resultados e descobrir oportunidades de melhoria nos processos atuais, contribuindo para decisões mais estratégicas e para o fortalecimento das ações que promovem o desenvolvimento educacional e social dos estudantes.


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
├── 📄 modelo_rl.joblib             # Modelo Regressão Logística treinado e exportado
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

