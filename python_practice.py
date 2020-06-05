# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#total vote count
total_votes = 0
candidate_options = []
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        print(total_votes)

        #print candidate name
        candidate_name = row [2]
        if candidate_name not in candidate_options:
            #add candidate name
            candidate_options.append(candidate_name)

            #track candidate vote
            candidate_votes[candidate_name] = 0


#print candidate list
print(candidate_votes)


