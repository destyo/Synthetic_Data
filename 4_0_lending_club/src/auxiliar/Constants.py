##############
# Constants  #
##############

field_types=  {
                "term": {
                    "type": "categorical"
                            }, 
                "int_rate": {
                    "type":"numerical",
                    "subtype":"float"
                            },                
                "subgrade":  {
                    "type": "categorical"
                    },                
                "emp_length": {
                    "type" : "numerical",
                    "subtype" : "integer"
                    },                
                "home_ownership":  {
                    "type": "categorical"
                    },                
                "annual_inc": {
                    "type":"numerical",
                    "subtype":"float"
                            },                
                "verification_status": {
                    "type": "boolean"
                            },    
                "purpose":  {
                    "type": "categorical"
                    },                
                "addr_state":  {
                    "type": "categorical"
                    },                
                "dti": {
                    "type":"numerical",
                    "subtype":"float"
                            },                    
                "delinq_2yrs": {
                    "type":"numerical",
                    "subtype":"float"
                            },                    
                "earliest_cr_line":  {
                    "type": "categorical"
                    },                   
                "fico_range_low": {
                    "type":"numerical",
                    "subtype":"float"
                            },                            
                "open_acc": {
                    "type":"numerical",
                    "subtype":"float"
                            },                            
                "pub_rec": {
                    "type":"numerical",
                    "subtype":"float"
                            },                            
                "revol_bal": {
                    "type":"numerical",
                    "subtype":"float"
                            },                            
                "revol_util": {
                    "type":"numerical",
                    "subtype":"float"
                            },                            
                "total_acc": {
                    "type":"numerical",
                    "subtype":"float"
                            },                            
                "initial_list_status": {
                    "type": "boolean"
                            },
                "application_type": {
                    "type": "boolean"
                            },                   
                "acc_open_past_24mths": {
                    "type":"numerical",
                    "subtype":"float"
                            },  
                "mort_acc": {
                    "type":"numerical",
                    "subtype":"float"
                            },  
                "pub_rec_bankruptcies": {
                    "type":"numerical",
                    "subtype":"float"
                            },  
                "tax_liens": {
                    "type":"numerical",
                    "subtype":"float"
                            },  
                "disbursement_method": {
                    "type": "boolean"
                            },   
                "issue_month":  {
                    "type": "categorical"
                    },                         
                "issue_year": {
                    "type" : "numerical",
                    "subtype" : "integer"                
                    },                   
                "earliest_cr_year": {
                    "type" : "numerical",
                    "subtype" : "integer"                
                    },
                "loan_status": {
                    "type": "boolean"
                            }
}


field_transformers = {}

