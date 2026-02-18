import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, OrdinalEncoder
from imblearn.over_sampling import SMOTE

class DropFeatures(BaseEstimator, TransformerMixin):
  def __init__(self, feature_to_drop=['ra', 'ano_arquivo', 'requer_psicologia']):
    self.feature_to_drop = feature_to_drop

  def fit(self, df):
    return self

  def transform(self, df):
    if (set(self.feature_to_drop).issubset(df.columns)):
      df.drop(self.feature_to_drop, axis=1, inplace=True)
      return df
    else:
      print('Uma ou mais features não estão no DataFrame 1')
      return df


colunas_quantitativas = ['iaa_autoavaliacao', 'ida_desempenho_academico', 'ieg_engajamento_atividades',
                         'ipp_psicopedagogicos', 'ian_adequacao_nivel', 'ips_aspectos_psicossociais',
                         'ipv_ponto_virada', 'inde_indice_desen_educacional', 'defasagem']

class MinMax(BaseEstimator, TransformerMixin):
    def __init__(self, min_max_scaler = colunas_quantitativas):
        self.min_max_scaler = min_max_scaler
        self.scaler = MinMaxScaler()

    def fit(self, df):
        if set(self.min_max_scaler).issubset(df.columns):
            self.scaler.fit(df[self.min_max_scaler])
        else:
            print("Uma ou mais features não estão no DataFrame")
        return self

    def transform(self, df):
        if set(self.min_max_scaler).issubset(df.columns):
            df[self.min_max_scaler] = self.scaler.transform(df[self.min_max_scaler])
            return df
        else:
            print("Uma ou mais features não estão no DataFrame")
            return df
        
class OneHotEncodingNames(BaseEstimator, TransformerMixin):
    def __init__(self, OneHotEncoding=['atingiu_pv']):
        self.OneHotEncoding = OneHotEncoding
        self.encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

    def fit(self, df, y=None):
        # Fit apenas nas colunas categóricas
        self.encoder.fit(df[self.OneHotEncoding])
        return self

    def transform(self, df):
        if not set(self.OneHotEncoding).issubset(df.columns):
            print('Uma ou mais features não estão no DataFrame')
            return df

        # Transform sem refazer fit
        onehot_array = self.encoder.transform(df[self.OneHotEncoding])
        feature_names = self.encoder.get_feature_names_out(self.OneHotEncoding)

        df_onehot = pd.DataFrame(onehot_array, columns=feature_names, index=df.index)

        # Mantém colunas que não foram one-hot
        outras_features = df.drop(columns=self.OneHotEncoding)

        # Concatena
        df_final = pd.concat([df_onehot, outras_features], axis=1)

        return df_final