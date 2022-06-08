#####################
# Metadata Creation #
#####################
import sdv
from sdv.tabular import GaussianCopula, CTGAN
from auxiliar.Constants import field_types, field_transformers


generator = CTGAN.load('../models/tvae.pkl')
#Metadata
table_metadata = generator.get_metadata().to_dict()
table_metadata['name'] = 'ncbd'
table_metadata['target'] = 'fatality'
#table_metadata['primary_key'] = 
metadata = {'tables': 
    {'ncbd': table_metadata}}
print(metadata)
metadata = sdv.metadata.dataset.Metadata(metadata)