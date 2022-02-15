# Challenge done using Python instead of PHP

# import necessary modules 
# pandas used for data manipulation / dataframe access, sys to get command line args, os to get basename and current dir
import pandas as pd
import sys
import os
# function that takes in a list of csv files and a file name and outupts the resulting combined file
def combine_csv(csv_list, filename):
    
    # define a list to store the data frames with the additional column 'filename'
    data_list = []

    # read each data frame from every csv file and append to new_file
    for i in csv_list:
        df = pd.read_csv(i)
        df['filename'] = os.path.basename(i) # add filename column to data frame
        data_list.append(df);

    # combine the csv files and convert to csv
    combined = pd.concat(data_list)
    combined.to_csv(filename, index=False, encoding='utf-8-sig')
    


# get the list of csv files from command line arguments
inputs = sys.argv[1:]
all_files = []

# modify input to put full path with correct formatting
for i in inputs:
    path = os.getcwd() + i[1:]
    path = path.replace('/', '\\')
    all_files.append(path)

combined_file = os.getcwd() + '\\combined.csv'
if os.path.exists(combined_file):
    combine_csv(all_files, combined_file)





