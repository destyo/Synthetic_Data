####################
#  TVAE GENERATOR #
####################

# Libaries
import pandas as pd
from sdv.tabular import TVAE
from Constants import field_types, field_transformers
import time
start_time = time.time()

#Load Train Data
train = pd.read_parquet("data/processed/train.parquet")

# Fitting and Saving Generator
tvae = TVAE(field_types=field_types, 
              cuda=True)

tvae.fit(train)
print("--- %s seconds ---" % (time.time() - start_time))
tvae.save('models/tvae.pkl')

# 1ª TIME: 
# 2 TIME: 