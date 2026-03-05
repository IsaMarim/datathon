import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from utils import DropFeatures, MinMax, OneHotEncodingNames
import joblib
from joblib import load
import numpy as np
from sklearn.impute import SimpleImputer

# Import da base já tratada
dados = pd.read_csv('bases/fat_datathon_tratado.csv')

# Título
st.write("# Datathon")

st.markdown("<br>", unsafe_allow_html=True)
st.write("Isabela Marim Mayerhoffer Pereira - RM 362023")
st.write("Lucas Constantino Silva - RM 364620")
st.write("Pedro Bugui Garcia - RM 360783")
st.write("Sophia Yeshua Senra - RM 362887")

st.markdown("<br>", unsafe_allow_html=True)
st.write("## Modelo Preditivo - Risco de Defasagem")
st.markdown("<br>", unsafe_allow_html=True)


# Formulário
st.write('### Dados do Aluno')

st.markdown("<br>", unsafe_allow_html=True)
input_iaa = float(st.slider('IAA do aluno', 0.0, 10.0))

st.markdown("<br>", unsafe_allow_html=True)
input_ida = float(st.slider('IDA do aluno', 0.0, 10.0))

st.markdown("<br>", unsafe_allow_html=True)
input_ieg = float(st.slider('IEG do aluno', 0.0, 10.0))

st.markdown("<br>", unsafe_allow_html=True)
input_ipp = float(st.slider('IPP do aluno', 0.0, 10.0))

st.markdown("<br>", unsafe_allow_html=True)
input_ian = st.selectbox("IAN do aluno",options=[2.5, 5.0, 10.0])

st.markdown("<br>", unsafe_allow_html=True)
input_ips = float(st.slider('IPS do aluno', 0.0, 10.0))

st.markdown("<br>", unsafe_allow_html=True)
input_ipv = float(st.slider('IPV do aluno', 0.0, 10.0))

st.markdown("<br>", unsafe_allow_html=True)
input_inde = float(st.slider('INDE do aluno', 0.0, 10.0))

st.markdown("<br>", unsafe_allow_html=True)
input_pv = st.radio('Aluno atingiu o PV?', ['Não', 'Sim'])

st.markdown("<br>", unsafe_allow_html=True)
input_defasagem = float(st.slider('Defasagem do aluno', -5, 2))

st.markdown("<br>", unsafe_allow_html=True)

# Lista de todas as variáveis: 
novo_registro = ["RA-0", # RA
                    input_iaa,
                    input_ida,
                    input_ieg,
                    input_ipp,
                    input_ian,
                    input_ips,
                    input_ipv,
                    input_inde,
                    "Não avaliado", # Requer psicologia
                    input_pv,
                    input_defasagem,
                    2024, # ano do arquivo
                    np.nan # risco - target
                    ]


def preparar_dados(df, target='risco', ano_teste=2024, modo="producao"):

    df = df.sort_values(by=["ra", "ano_arquivo"]).copy()

    # Comportamento diferente por modo

    if modo == "producao":
        # Remove rótulo do ano teste
        df.loc[df["ano_arquivo"] == ano_teste, target] = np.nan

    # Split temporal

    df_train = df[df["ano_arquivo"] < ano_teste].copy()
    df_test  = df[df["ano_arquivo"] == ano_teste].copy()

    df_train = df_train.dropna(subset=[target])

    # Adicionando novo registro
    registro = pd.DataFrame([novo_registro],columns=df_test.columns)

    # Concatenando novo registro ao dataframe dos dados de teste
    df_test = pd.concat([df_test,registro],ignore_index=True)

    # Separação X e y

    X_train = df_train.drop(columns=[target])
    y_train = df_train[target]

    if modo == "validacao":
        y_test = df_test[target]
        X_test = df_test.drop(columns=[target])
    else:
        y_test = None
        X_test = df_test.drop(columns=[target])

    # Imputação Numérica

    colunas_numericas = X_train.select_dtypes(include=["int64", "float64"]).columns

    colunas_validas = [
        col for col in colunas_numericas
        if not X_train[col].isna().all()
    ]

    imputer = SimpleImputer(strategy='median')

    X_train[colunas_validas] = imputer.fit_transform(X_train[colunas_validas])
    X_test[colunas_validas]  = imputer.transform(X_test[colunas_validas])

    # 5️⃣ Pipeline

    pipe = Pipeline([
        ('Drop_feature', DropFeatures()),
        ('OneHotEncoding', OneHotEncodingNames()),
        ('min_max_scaler', MinMax())
    ])

    df_train_pipe = pd.concat([X_train, y_train], axis=1)
    df_train_transformed = pipe.fit_transform(df_train_pipe)

    df_test_transformed = pipe.transform(X_test)

    # 6️⃣ Separação final

    X_train_final = df_train_transformed.drop(columns=[target])
    y_train_final = df_train_transformed[target]

    X_test_final = df_test_transformed.copy()

    if modo == "validacao":
        X_train_final = X_train_final.drop(columns=['ipp_psicopedagogicos'])
        X_test_final = X_test_final.drop(columns=['ipp_psicopedagogicos'])

    return X_train_final, X_test_final, y_train_final, y_test, pipe


X_treino_prev, X_teste_prev, y_treino_prev, y_teste_prev, pipe_prev = preparar_dados(
    dados,
    ano_teste=2024,
    modo="producao"
)

def prever_risco(modelo):

    modelo.fit(X_treino_prev, y_treino_prev)

    prob_predic = modelo.predict_proba(X_teste_prev)[:, 1]

    df_resultado = X_teste_prev.copy()
    df_resultado["prob_risco"] = prob_predic

    return df_resultado

# Rodar modelo ao apertar o botão de enviar
if st.button('Enviar Formulário'):

    model = joblib.load('modelo_rl.joblib')
    resultado = prever_risco(model)

    st.markdown("<br>", unsafe_allow_html=True)
    valor = resultado["prob_risco"].iloc[-1]
    

    # Classificação do risco
    if 0 <= valor <= 0.25:
        classificacao = "Muito Baixo"
    elif 0.25 < valor <= 0.5:
        classificacao = "Baixo"
    elif 0.5 < valor <= 0.75:
        classificacao = "Alto"
    else:
        classificacao = "Muito Alto"

    # Exibição formatada
    st.write("#### Resultado da Análise de Risco")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(f"##### Probabilidade estimada: {valor*100:.2f}%")
    st.write(f"##### Classificação: {classificacao}")