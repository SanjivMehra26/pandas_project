# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Solution
import pandas as pd
def get_match_innings_runs ():
    var = pd.DataFrame(ipl_df[['match_code','inning','runs']])
    return var.groupby(['match_code','inning']).agg(['sum'])


get_match_innings_runs()


