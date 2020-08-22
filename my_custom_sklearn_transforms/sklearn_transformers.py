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
    def __init__(self):
        self = SMOTEENN(random_state=0) 
    def fit(self, X, y):
        X_resampled, y_resampled = self.fit_resample(X, y)
    def transform(self, X):
        return X_resampled