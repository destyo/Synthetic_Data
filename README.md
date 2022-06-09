# Métodos para la generación y evaluación de datos sintéticos

**Máster universitario en Ciencia de Datos (MUCD) - CUNEF**    

**Autor: Antonio Tello Gómez**  
**Tutor: Diego J. Bodas Sagi**  
**Fecha:  06/2022**

![cunef](https://live.staticflickr.com/2588/4171571040_bab4a40acf_z.jpg)

Este repositorio contiene el código y los resultados de la parte de demostración de mi Trabajo de Fin de Máster _"Métodos para la generación y evaluación de datos sintéticos"_

El repositorio está formado por cuatro proyectos individuales para cuatro conjuntos de datos distintos.
- Iris
- Diamonds
- NCDB
- Lending Club

## Esquema del sistema empleado
[![Image from Gyazo](https://i.gyazo.com/8acf2a714d7996daa97d3d5f66580180.png)](https://github.com/destyo/Synthetic_Data)


<br>

## ¿Qué son los datos sintéticos?

Entendemos por datos sintéticos aquellos que no provienen de eventos en la realidad si no que han sido generados de manera artificial replicando las propiedades estadísticas de datos reales. Sin embargo, a diferencia de estos no contienen información que permita identificar a personas reales, garantizando así la protección de la privacidad.






## Estructura del Proyecto

```bash

├── 1_0_iris
│   ├── data
│   ├── models
│   ├── notebooks
│   │   └── 1.0-iris-demo.ipynb
│   └── src
├── 2_0_diamonds
│   ├── data
│   ├── models
│   ├── notebooks
│   │   └── 2.0-diamonds-demo.ipynb
│   └── src
├── 3_0_ncdb
│   ├── data
│   │   ├── processed
│   │   │   ├── test.parquet
│   │   │   ├── train.parquet
│   │   │   ├── xtest.parquet
│   │   │   ├── xtrain.parquet
│   │   │   ├── ytest.parquet
│   │   │   └── ytrain.parquet
│   │   ├── raw
│   │   │   └── NCDB_1999_to_2014.csv
│   │   └── synth
│   │       ├── synth_ctgan.parquet
│   │       └── synth_tvae.parquet
│   ├── models
│   │   ├── ctgan.pkl
│   │   ├── gaussian_copula.pkl
│   │   ├── lightgbm_ctgan.joblib
│   │   ├── lightgbm.joblib
│   │   └── tvae.pkl
│   ├── notebooks
│   │   ├── Full_Evaluation_CTGAN.ipynb
│   │   ├── Full_Evaluation_TVAE.ipynb
│   │   └── Machine_Learning_Efficacy.ipynb
│   └── src
│       ├── auxiliar
│       │   ├── aux_func.py
│       │   ├── Constants.py
│       │   └── metadata.py
│       ├── generators
│       │   ├── COPGAN_generator.py
│       │   ├── CTGAN_generator.py
│       │   ├── GC_generator.py
│       │   └── TVAE_generator.py
│       └── original project
│           ├── predict.py
│           ├── preprocessing.py
│           └── train.py
├── 4_0_lending_club
│   ├── data
│   │   ├── andres
│   │   │   ├── synth_data_full.parquet
│   │   │   ├── test.parquet
│   │   │   └── train.parquet
│   │   ├── processed
│   │   │   ├── test.parquet
│   │   │   └── train.parquet
│   │   ├── raw
│   │   │   ├── Loan_test_set.csv
│   │   │   ├── Loan_training_set_1_4.csv
│   │   │   ├── Loan_training_set_2_4.csv
│   │   │   ├── Loan_training_set_3_4.csv
│   │   │   └── Loan_training_set_4_4.csv
│   │   └── synth
│   │       ├── synth_ctgan.parquet
│   │       └── synth_tvae.parquet
│   ├── models
│   │   ├── ctgan.pkl
│   │   └── tvae.pkl
│   ├── notebooks
│   │   ├── collaboration_project.ipynb
│   │   ├── Full_Evaluation_CTGAN.ipynb
│   │   ├── Full_Evaluation_TVAE.ipynb
│   │   └── test.ipynb
│   ├── reports
│   └── src
│       ├── auxiliar
│       │   ├── aux_func.py
│       │   ├── Constants.py
│       │   └── metadata.py
│       ├── generators
│       │   ├── COPGAN_generator.py
│       │   ├── CTGAN_generator.py
│       │   ├── GC_generator.py
│       │   └── TVAE_generator.py
│       └── original project
│           └── Preprocessing.py
├── LICENSE
├── README.md
├── synth_linux.yml
└── synth_windows.yml

```

## Reproducibilidad

En el repositorio podemos encontrar dos ficheros .yml para recrear los entornos, tanto para Windows como para Linux. Para recrear los resultados es preferible utilizar el entorno Linux en un equipo con GPU y CUDA



## Contacto

Antonio Tello Gómez - atelloengland@gmail.com

Project Link: [https://github.com/destyo](https://github.com/destyo/Synthetic_Data)


## Agradecimientos


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

<p align="right">(<a href="#top">back to top</a>)</p>
