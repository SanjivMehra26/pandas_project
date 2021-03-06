# %load q04_get_match_specific_df/build.py
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
def get_match_specific_df (match_code):
    filterData = ipl_df[[Filterspecific(row,match_code) for row in ipl_df['match_code']]]
    return filterData

def Filterspecific (row,match_code):
    return row == match_code



