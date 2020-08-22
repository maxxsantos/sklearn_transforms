from sklearn.base import BaseEstimator, TransformerMixin
from imblearn.combine import SMOTEENN 

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class Balance(SMOTEENN):
    def __init__(self, sampling_strategy='auto', random_state=None, smote=None, enn=None, n_jobs=1, ratio=None):
        self = self
    def fit_resample(self, X, y):
        smote_enn = SMOTEEN(random_state=0)
        return smote_enn.fit_resample(X, y)
