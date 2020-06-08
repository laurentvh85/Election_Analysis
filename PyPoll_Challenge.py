import csv
import os  
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize all variables

#total vote count 
total_votes = 0 
# candidate and vote options
candidate_options = []
candidate_votes = {}
# Winning Candidate and count 
winning_candidate =""
winning_count = 0 
winning_percentage = 0
#county list
county_options = []
county_votes = {}
# largest county turn out 
largest_county =""
turnout_vote = 0 


# Open the election results and read the file
with open(file_to_load) as election_data:
# Read the file object with teh reader function. 
    file_reader = csv.reader(election_data)
# Print the header row. 
    headers = next(file_reader)  
# Print each row
    for row in file_reader:
        #  total vote count 
        total_votes += 1
    
        # candidate name for each row 
        candidate_name = row[2]
        # If statement to add to list
        if candidate_name not in candidate_options:
        # Add candidate to candidate list 
            candidate_options.append(candidate_name)
        # Begin tracking vote count 
            candidate_votes[candidate_name] = 0
        # Increase candidate vote count 
        candidate_votes[candidate_name] += 1 
        
        # Print county name
        county_name = row[1]
        # If county name not in list add county name 
        if county_name not in county_options:
            # Add county 
            county_options.append(county_name)
            # track county vote count
            county_votes[county_name] = 0
        # Increase county vote 
        county_votes[county_name] += 1 

    # with statement to save file as a text file.
with open(file_to_save, "w") as txt_file:
    # Print and write election results.
    election_results =(
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes : {total_votes:,}\n"
            f"-------------------------\n")
    print(election_results,end="")
    txt_file.write(election_results)

    # Create county header
    county_header = (
        f"\n"
        f"County Votes:"
        f"\n"
        )
    # Print on screen and write to text file 
    print(county_header)
    txt_file.write(county_header)

    # Calculate county vote percentage
    for county in county_votes :
        county_total = county_votes[county]
        county_percentage = int(county_total)/int(total_votes)*100
        # Create election results per county 
        county_results =(f"{county} : {county_percentage:.1f}% ({county_total:,})\n")
        # Print and save to text file 
        print(county_results)
        txt_file.write(county_results)

        # Determine lagest turn out county 
        if (county_total>turnout_vote) :
            # Set largest county turnout
            turnout_vote = county_total
            largest_county = county
            # Print largest county turn out result
            county_turnout_result = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout : {county}\n"
            f"-------------------------\n" 
            )
    print( county_turnout_result)
    txt_file.write(county_turnout_result)

    # Calculate candidate's vote percentage    
    # Iterate through the candidate list    
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
          # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
     # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)