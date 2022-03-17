# create a csv file from scikit

# imports
from sklearn.datasets import fetch_california_housing
import pandas as pd

# vars
path_to_file = '/home/superuser/data/'

# create csv
california_housing = fetch_california_housing(as_frame=True)
pd.DataFrame(california_housing.frame).to_csv(path_to_file +'california_housing.csv')

