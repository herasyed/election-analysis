# The data we need to retrieve
# 1. The total number of votes cast
# 2. A completelist of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.

# # Close the file.
# election_data.close()

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
#   # Write three counties to the file.
#   txt_file.write("Arapahoe\nDenver\nJefferson")

# # Close the file
# outfile.close()

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # # Write three counties to the file.
    #  txt_file.write("Arapahoe\nDenver\nJefferson")

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

        # Print each row in the CSV file.
        for row in file_reader:
            print(row)

#Close the file. It is important that you close the file after you read and write in order to save the new data.
election_data.close()