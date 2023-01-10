import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class PrepareData(BaseEstimator, TransformerMixin):
    '''
    This class makes multiple transformations to the dataset
    - Include date information
    - Drop unnecessary columns    
    '''
    def __init__(self):
        pass

    def fit(self, X: pd.DataFrame, y=None):
        return self            

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        '''
        This function transform the column "water saturation" and "breakdown pressure" columns in boolean type,
        - Input:
            Dataframe
        - Output:
            Dataframe
        '''
        try:
            # Fill NaN values,  Impute binary method
            X['water saturation'] = X['water saturation'].apply(lambda x: 1 if x >= 0 else 0)
            X['breakdown pressure'] = X['breakdown pressure'].apply(lambda x: 1 if x >= 0 else 0)

            # Use date on production column to create new columns
            X['year on production'] = X['date on production'].apply(lambda x: x.year)
            X['month on production'] = X['date on production'].apply(lambda x: x.month)

            X = X.fillna(X.median(numeric_only=True))

            # Drop irrelevant columns to predictions
            X.drop(['date on production', 'footage lateral length', 'treatment company', 'operator'], 
                    axis=1, inplace=True)

            return X
        except:
            pass


