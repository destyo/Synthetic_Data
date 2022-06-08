import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy as np; print("NumPy", np.__version__)
import scipy; print("SciPy", scipy.__version__)
import os
import pandas as pd
from joblib import load

import warnings
warnings.filterwarnings('ignore')

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def predict():

    dirpath = os.getcwd()
    print("dirpath = ", dirpath, "\n")
    output_path = os.path.join(dirpath,'output.xlsx')
    print(output_path,"\n")

    xtest = pd.read_parquet('xtest.parquet')
    ytest = pd.read_csv('ytest.csv')

    # Cargamos el modelo
    clf = load('lightgbm.joblib')

    print("Model score and classification:")
    print(clf.predict(xtest))
    print(clf.predict_proba(xtest)[:,1])

    print(pd.DataFrame(clf.predict_proba(xtest)[:,1]))
    pd.DataFrame(clf.predict_proba(xtest)[:,1]).to_excel(output_path)

if __name__ == '__main__':
    predict()