import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
class Dataclean():
    """
    
    """
    def __init__(self, x):
        self.x=x
    def null(self):

        if type(self.x)==np.ndarray:
            df=self.x.flatten()
            x = df[np.logical_not(np.isnan(df))]
            df= np.nan_to_num(df,copy =True,nan=x.mean())

        elif type(self.x)==pd.core.frame.DataFrame:
            df=self.x
            num_f = [feature for feature in df.columns if df[feature].dtypes != 'O']
            for x in num_f:
                if df[x].isnull().sum() > 0:
                    df[x] = df[x].mean()
   
        return df

    def standardize(self):
        if type(self.x) == np.ndarray:
            df = self.x.flatten()
            scaler = StandardScaler()
            df = scaler.fit_transform(df)
        elif type(self.x)==pd.core.frame.DataFrame:
            df=self.x
            scaler = StandardScaler()
            df1 = pd.DataFrame(scaler.fit_transform(df), columns = df.columns) 
        return df1

#VIF
    def vif(self):
        df=self.x
        vif_df = pd.DataFrame()
        x = df.iloc[:,1:]
        #y = df.iloc[:,0]
        vif_df['vif'] = [variance_inflation_factor(df,i) for i in range(df.shape[1])]
        vif_df['feature']  = x.columns
        return vif_df