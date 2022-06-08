import platform; print(platform.platform())
import sys; print("Python", sys.version)
import numpy; print("NumPy", numpy.__version__)
import scipy; print("SciPy", scipy.__version__)

import os
import numpy as np
from lightgbm import LGBMClassifier
import pandas as pd
from joblib import dump
import pickle
from category_encoders import TargetEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import GridSearchCV

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def train():
    xtrain = pd.read_parquet("../../data/interim/xtrain.parquet")
    ytrain = pd.read_parquet("../../data/interim/ytrain.parquet")['fatality']

    # Generamos el pipeline
    # Categoricas pequeñas para OHE
    few_cat = []
    for column in xtrain.columns:
        if (len(xtrain[column].unique())< 7):
            few_cat.append(column)



    # Categoricas grandes para ME
    many_cat = []
    for column in xtrain.columns[xtrain.dtypes=='object']:
        if (len(xtrain[column].unique()) > 7):
            many_cat.append(column)

    # numericas
    numeric = ['vehicle_age', 'passenger_age', 'vehicles_involved', 'year']

    print(f"Few Cat :{few_cat}")
    print(f"Many Cat :{many_cat}")
    print(f"Numeirc :{numeric}")


    numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])


    onehot_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value=np.nan)),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('target', TargetEncoder(handle_unknown='ignore'))])


    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric),
            ('fcat', onehot_transformer, few_cat),
            ('mcat', categorical_transformer, many_cat)])


    # Models training

    lightgbm = Pipeline(steps=[('preprocessor', preprocessor),
                            ('clasificador', LGBMClassifier())])

    # param grid

    param_grid = {
        'clasificador__is_unbalance': [True],
        'clasificador__max_depth': [-1],
        'clasificador__objective': ['binary'],
        'clasificador__learning_rate': [0.1, 0.05],
        'clasificador__n_estimators': [200, 300],
        'clasificador__importance_type': ['split', 'gain'],
        'clasificador__num_leaves': [50, 100]
    }
    print('Training model...')
    CV = GridSearchCV(lightgbm, param_grid, cv=3, n_jobs=4, scoring='roc_auc', verbose=1)
    CV.fit(xtrain,ytrain)
    print("done!")
    # Save model
    with open('../../models/lightgbm.joblib', 'wb') as f:
        pickle.dump(CV, f)

if __name__ == '__main__':
    train()
