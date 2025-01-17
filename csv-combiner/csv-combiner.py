# Challenge done using Python instead of PHP

# Run command can be found in the README

# import necessary modules 
# pandas used for data manipulation / dataframe access, sys to get command line args, os to get basename
import pandas as pd
import sys
import os
# function that takes in a list of csv files and outupts the resulting combined file
def combine_csv(input_files):
    
    # define a list to store the data frames with the additional column 'filename'
    data_list = []

    # read data frame from each csv file and append to data_list
    for i in input_files:
        df = pd.read_csv(i)
        df['filename'] = os.path.basename(i) # add filename column to data frame
        data_list.append(df);

    # combine the csv files and convert to csv
    combined = pd.concat(data_list)
    combined.to_csv(sys.stdout, index=False)
    


# get the list of csv files from command line arguments
input_files = sys.argv[1:]


combine_csv(input_files)





