# Author: Joshua White
#
# This file will take a csv file, shuffle the rows, and outputs a test data set and a training set based.  
# This script does not change the origional file. 
# The size of the test set can be tuned as a percentage of the initial data set. 

import pandas as pd 

# Tuning knobs here, edit as needed:
test_set_percentage = .2 # % of the overall data set you would like the test set to be. 
headers = True # True if your file has heads, false otherwise
filename = 'C:\\Users\\Joshua\\Google Drive\\CSCE 623 - Machine Learning\\Project\\Code\\nyc-jobs-cleaned.csv' # the csv filename you would like to manipulate
test_filename_helper = 'C:\\Users\\Joshua\\Google Drive\\CSCE 623 - Machine Learning\\Project\\Code\\test_data_nyc-jobs'
training_filename_helper = 'C:\\Users\\Joshua\\Google Drive\\CSCE 623 - Machine Learning\\Project\\Code\\training_data_nyc-jobs'

# Load the file into a pandas dataframe
if headers:
    DFrame = pd.read_csv(filename)
else:
    DFrame = pd.read_csv(filename, header = None)

# Shuffle all rows and reset the index of the data frame, the frac = 1
# is to have it shuffle the whole df, the random_state makes the random shuffle
# reproduceable, and the reset_index(drop = true) resets the indexes of the dataframe.
# Source: https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
DFrame = DFrame.sample(frac = 1, random_state = 42).reset_index(drop = True)

# Some set up of variables here to split the data set
num_rows = len(DFrame.index)
test_set_size = num_rows // (1 / test_set_percentage) # Use floor division here

# Check to make sure numbers look right
print('Total number of rows in the input file: ' + str(num_rows))
print('Total number of rows in the output test set: ' + str(test_set_size))

# Create data frames for the test and training sets here:
test_set = DFrame.loc[ 0 : (test_set_size - 1) ]
training_set = DFrame.loc[ test_set_size : (num_rows-1) ]

# Set up the file name
test_filename = test_filename_helper + '.csv'
train_filename = training_filename_helper + '.csv'

# Now output the files
print("Generating files now.")
test_set.to_csv(test_filename, index = False, header = True)
training_set.to_csv(train_filename, index = False, header = True)