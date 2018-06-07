import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import preprocessing
from sklearn import tree
def predict_qual(fixedacid,criticacid,residualsugar,volatileacid,freesulpherdioxide,totalsulpherdioxide,chloride,density,ph,sulphate,alcohol):
    src = '/Users/AliAsgar BS/Desktop/winerama1/reviews/winequality.csv'
    wine = pd.read_csv(src)
    X = wine.drop('quality', axis = 1)
    y = wine['quality']
    test = np.array([fixedacid,criticacid,residualsugar,volatileacid,freesulpherdioxide,totalsulpherdioxide,chloride,density,ph,sulphate,alcohol])
    test = test.reshape(1,11)
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    test = sc.fit_transform(test)
    rfc = RandomForestClassifier(n_estimators=200)
    rfc.fit(X_train, y_train)
    pred_rfc = rfc.predict(test)
    return float(pred_rfc)
