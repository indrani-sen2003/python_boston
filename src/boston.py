import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle
def model_reg_boston(file):
    df=pd.read_csv(file)
    x=df.drop("MEDV",axis=1)
    y=df["MEDV"]
    x_tr,x_test,y_tr,y_test=train_test_split(x,y,test_size=0.2)
    model=LinearRegression().fit(x_tr,y_tr)
    p=model.predict(x_test)
    r2=r2_score(y_test,p)
    return r2
