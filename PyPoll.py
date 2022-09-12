# Data retrieving using Python


import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign variable for the file to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Opening the election analysis results file to the read the file
with open(file_to_load) as election_data:
    
# Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #for row in file_reader:
        #print(row)
    headers = next(file_reader)
    print(headers)    
# Using the open() function with the "w" mode we will write data to the file
   # with open(file_to_save, "w") as txt_file:

       

# 1. Total number of votes cast
# 2. A complete lost of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candiadte won
# 5. The winner of the election based on popular vote

