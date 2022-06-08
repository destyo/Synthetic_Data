##################
# Preprocessing  #
##################
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def preprocessing():
    #Read Data
    ruta_raw = "data/raw/"
    ruta_processed = "data/processed/"
    df1 = pd.read_csv(f'{ruta_raw}Loan_test_set.csv', skiprows=[0])
    df2 = pd.read_csv(f'{ruta_raw}Loan_training_set_1_4.csv', skiprows=[0])
    df3 = pd.read_csv(f'{ruta_raw}Loan_training_set_2_4.csv', skiprows=[0])
    df4 = pd.read_csv(f'{ruta_raw}Loan_training_set_3_4.csv', skiprows=[0])
    df5 = pd.read_csv(f'{ruta_raw}Loan_training_set_4_4.csv', skiprows=[0])
    df1['test_set'] = 1
    df2['test_set'] = 0
    df3['test_set'] = 0
    df4['test_set'] = 0
    df5['test_set'] = 0
    df = pd.concat([df1, df2, df3, df4, df5])
    
    # Select data with loan_status either Fully Paid or Charged Off 
    df = df.loc[(df['loan_status'].isin(['Fully Paid', 'Charged Off']))]
    
    # Delete columns with aprox 90% missing values
    missing_df = df.isnull().sum(axis = 0).sort_values().to_frame('missing_value').reset_index()
    miss_4000 = list(missing_df[missing_df.missing_value >= 400000]['index'])
    df.drop(miss_4000, axis = 1, inplace = True)
    
    # Delte constant features
    const_features = ['pymnt_plan', 'out_prncp', 'out_prncp_inv', 'policy_code', 'hardship_flag']
    df.drop(const_features, axis = 1, inplace = True)
    
    #Drop duplicate rows
    df.drop_duplicates(inplace= True)
    
    
    # Term feature
    df.term = df.term.str.replace('months', '').astype(np.int)
    
    #interest rate 
    df.int_rate = df.int_rate.str.replace('%', '').astype(np.float32)
    
    #emp_lenght
    df.emp_length.fillna(value=0,inplace=True)
    df['emp_length'].replace(to_replace='[^0-9]+', value='', inplace=True, regex=True)
    df['emp_length'] = df['emp_length'].astype(int)
    
    # Verification status 
    df.verification_status = df.verification_status.map(lambda x: 1 if x == 'Not Verified' else 0)
    
    #issue_d
    df['issue_month'] = pd.Series(df.issue_d).str.replace(r'-\d+', '')
    df['issue_year'] = pd.Series(df.issue_d).str.replace(r'\w+-', '').astype(np.int) 
    
    #loan status
    df.loan_status = df.loan_status.map(lambda x: 1 if x == 'Charged Off' else 0)
    
    # earliest_cr_line
    df['earliest_cr_year'] = df.earliest_cr_line.str.replace(r'\w+-', '').astype(np.int)
    df['credit_history'] = np.absolute(df['issue_year']- df['earliest_cr_year'])
    
    #revol_util
    df.revol_util = df.revol_util.str.replace('%', '').astype(np.float32)#
    
    #initial list stauts
    df.initial_list_status = df.initial_list_status.map(lambda x: 1 if x== 'w' else 0)
    
    # application type
    df.application_type = df.application_type.map(lambda x: 0 if x == 'Individual' else 1)
    
    # disbursement method
    df.disbursement_method = df.disbursement_method.map(lambda x: 0 if x == 'Cash' else 1)
    
    # debt_settlement_flag
    df.debt_settlement_flag = df.debt_settlement_flag.map(lambda x: 0 if x == 'N' else 1)
    
    #Drop additional features
    features_to_be_removed = ['loan_amnt','emp_title', 'id', 'url', 'title', 'zip_code', 'issue_d', 'mths_since_last_delinq', \
        'mths_since_last_record', 'inq_last_6mths', 'mths_since_last_delinq', 'mths_since_last_record', 'total_pymnt', 'total_pymnt_inv',\
        'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'last_pymnt_d', 'last_pymnt_amnt',\
        'last_credit_pull_d', 'last_fico_range_high', 'last_fico_range_low', 'collections_12_mths_ex_med', 'mths_since_last_major_derog',\
        'acc_now_delinq', 'tot_coll_amt', 'tot_cur_bal', 'total_rev_hi_lim', 'avg_cur_bal', 'bc_open_to_buy', 'bc_util', 'chargeoff_within_12_mths',\
        'delinq_amnt', 'mo_sin_old_il_acct', 'mo_sin_old_rev_tl_op', 'mo_sin_rcnt_rev_tl_op', 'mo_sin_rcnt_tl', 'mths_since_recent_bc', 'mths_since_recent_bc_dlq',\
        'mths_since_recent_inq', 'mths_since_recent_revol_delinq', 'num_accts_ever_120_pd', 'num_actv_bc_tl', 'num_actv_rev_tl', 'num_bc_sats', 'num_bc_tl',\
        'num_il_tl', 'num_op_rev_tl', 'num_rev_accts', 'num_rev_tl_bal_gt_0', 'num_sats', 'num_tl_120dpd_2m', 'num_tl_30dpd', 'num_tl_90g_dpd_24m',\
        'num_tl_op_past_12m', 'pct_tl_nvr_dlq', 'percent_bc_gt_75', 'tot_hi_cred_lim', 'total_bal_ex_mort', 'total_bc_limit', 'debt_settlement_flag', 'total_il_high_credit_limit']
    df.drop(features_to_be_removed, axis = 1, inplace = True)
    
    #Drop Nas
    df.dropna(inplace=True)
    
    #Drop highly correlated feat
    high_correlated_feat = ['funded_amnt','funded_amnt_inv', 'fico_range_high', 'grade', 'credit_history', 'installment']
    df.drop(high_correlated_feat, axis=1, inplace=True)
    
    # Move target to the right
    df.insert(29, "loan_status", df.pop("loan_status"))
    
    #Saving Processed train and test
    df[(df.test_set == 0)].drop(['test_set'], axis=1).to_parquet(f'{ruta_processed}train.parquet', index = False)
    df[(df.test_set == 1)].drop(['test_set'], axis=1).to_parquet(f'{ruta_processed}test.parquet', index = False)

if __name__ == '__main__':
    preprocessing()