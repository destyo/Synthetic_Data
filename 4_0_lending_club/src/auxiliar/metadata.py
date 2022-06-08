#####################
# Metadata Creation #
#####################
import sdv
from sdv.tabular import GaussianCopula, CTGAN
from auxiliar.Constants import field_types, field_transformers


generator = CTGAN.load('../models/ctgan.pkl')
#Metadata
table_metadata = generator.get_metadata().to_dict()
table_metadata['name'] = 'lending'
table_metadata['target'] = 'loan_status'
#table_metadata['primary_key'] = 
metadata = {'tables': 
    {'lending_club': table_metadata}}
print(metadata)
metadata = sdv.metadata.dataset.Metadata(metadata)