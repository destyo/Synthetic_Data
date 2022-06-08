##################################
# Misellanous Auxiliar functions #
##################################
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy.stats import skew,kurtosis
import scipy.stats as stats







def qqploter(real_data,synthetic_data,variable,dist1=stats.pareto(3),dist2=stats.lognorm(3)):
  # standardize the observation
    z1 = (real_data[variable]-np.mean(real_data[variable]))/np.std(real_data[variable])
    z2 = (synthetic_data[variable]-np.mean(synthetic_data[variable]))/np.std(synthetic_data[variable])

    # QQ plot experiment 
    f, ([[ax1, ax2], [ax3, ax4]]) = plt.subplots(nrows=2, ncols=2, figsize=(24,12), dpi=90)
    stats.probplot(z2, dist=dist1, plot=ax2)
    stats.probplot(z1, dist=dist1, plot=ax1)
    stats.probplot(z1, dist=dist2, plot=ax3)
    stats.probplot(z2, dist=dist2, plot=ax4)
    ax1.set_title(f"QQ Plot 1 for Real Data")
    ax2.set_title(f"QQ Plot 1 for Synthetic Data")
    ax3.set_title(f"QQ Plot 2 for Real Data")
    ax4.set_title(f"QQ Plot 2 for Synthetic Data")
    plt.show()  



def var_comparative(real_data, synthetic_data, variable):
    """
    Returns some statistics of the selected variable for real and synth data
    """
    print('Real Data Mean :', np.mean((real_data[variable])).round(2))
    print('Real Data Median :', np.median((real_data[variable])).round(2))
    print('Real Data Max :',round((max(real_data[variable])),2))
    print('Syntehtic Data Mean :', np.mean((synthetic_data[variable])).round(2))
    print('Syntehtic Data Median :', np.median((synthetic_data[variable])).round(2))
    print('Syntehtic Data Max :', round((max(synthetic_data[variable])),2))

    print('--------------------------------')
    print('Real Data Skewness :', round((skew(real_data[variable])),2))
    print('Real Data Kurtosis :',round((kurtosis(real_data[variable])),2))
    print('Synthetic Data Skewness :',round((skew(synthetic_data[variable])),2))
    print('Synthetic Data Kurtosis :',round((kurtosis(synthetic_data[variable])),2))



def get_deviation_of_mean_perc(df, list_var_continuous, target, multiplier):
    """
    Devuelve el porcentaje de valores que exceden del intervalo de confianza
    :type series:
    :param multiplier:
    :return: df
    """
    pd_final = pd.DataFrame()
    
    for i in list_var_continuous:
        
        series_mean = df[i].mean()
        series_std = df[i].std()
        std_amp = multiplier * series_std
        left = series_mean - std_amp
        right = series_mean + std_amp
        size_s = df[i].size
        
        perc_goods = df[i][(df[i] >= left) & (df[i] <= right)].size/size_s
        perc_excess = df[i][(df[i] < left) | (df[i] > right)].size/size_s
        
        if perc_excess>0:    
            pd_concat_percent = pd.DataFrame(df[target][(df[i] < left) | (df[i] > right)]\
                                            .value_counts(normalize=True).reset_index()).T
            pd_concat_percent.columns = [pd_concat_percent.iloc[0,0], 
                                         pd_concat_percent.iloc[0,1], 
                                         pd_concat_percent.iloc[0,2]]
            pd_concat_percent = pd_concat_percent.drop('index',axis=0)
            pd_concat_percent['variable'] = i
            pd_concat_percent['sum_outlier_values'] = df[i][(df[i] < left) | (df[i] > right)].size
            pd_concat_percent['porcentaje_sum_outliers_values'] = perc_excess
            pd_final = pd.concat([pd_final, pd_concat_percent], axis=0).reset_index(drop=True)
            
    if pd_final.empty:
        print('No existen variables con valores nulos')
        
    return pd_final



def histogram_wo_outliers(real_data,synthetic_data,variable, multiplier, discrete=False):
    
    Q1r = real_data[variable].quantile(0.25)
    Q3r = real_data[variable].quantile(0.75)
    IQRr = Q3r - Q1r
    
    Q1s = synthetic_data[variable].quantile(0.25)
    Q3s = synthetic_data[variable].quantile(0.75)
    IQRs = Q3s - Q1s
    real_var = real_data[variable][~((real_data[variable] < (Q1 - multiplier * IQR)) |(real_data[variable] > (Q3 + multiplier * IQR)))]
    synth_var = synthetic_data[variable][~((synthetic_data[variable] < (Q1 - multiplier * IQR)) |(synthetic_data[variable] > (Q3 + multiplier * IQR)))]
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20,6), dpi=90)
    ax1.set_title(f"Real Data")
    ax2.set_title(f"Synthetic Data")
    sns.histplot(data=real_var, ax=ax1, discrete=discrete)
    sns.histplot(data=synth_var, ax=ax2, discrete=discrete)