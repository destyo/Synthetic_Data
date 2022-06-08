####################
#  Gaussian Copula #
####################
# Libaries
import pandas as pd
from sdv.tabular import GaussianCopula
from Constants import field_types, field_transformers
import time
start_time = time.time()

#Load Train Data
train = pd.read_parquet("data/interim/train.parquet")
# Fitting and Saving Generator
gaussian_copula = GaussianCopula(field_types=field_types, 
                               field_transformers=field_transformers)

gaussian_copula.fit(train)
print("--- %s seconds ---" % (time.time() - start_time))
gaussian_copula.save('models/gaussian_copula.pkl')

# 1º TIME: 
# 2 TIME: 

