####################
#  CTGAN GENERATOR #
####################

# Libaries
import pandas as pd
from sdv.tabular import CTGAN
from Constants import field_types, field_transformers

import time
start_time = time.time()

#Load Train Data
train = pd.read_parquet("data/interim/train.parquet")
# Fitting and Saving Generator
ctgan = CTGAN(verbose=True,
              field_types=field_types, 
              field_transformers=field_transformers,
              cuda=True)

ctgan.fit(train)
print("--- %s seconds ---" % (time.time() - start_time))
ctgan.save('models/ctgan.pkl')

# 1º TIME: 
# 2 TIME: 