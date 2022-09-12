# Data retrieving using Python

import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign variable for the file to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Declare emoty dictionary to find votes by candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Opening the election analysis results file to the read the file
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # To read the header row    
    headers = next(file_reader)
       
    # print each row in the CSV file
    for row in file_reader:

        # Finding total vote count
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Adding candidate name from each row
            candidate_options.append(candidate_name)

            # Tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to candidate's count
        candidate_votes[candidate_name] +=1
# Saving election results on text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the output text file
    txt_file.write(election_results)

# Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Saving winning candidate's results to teh text file
    txt_file.write(winning_candidate_summary)

# Printing total votes 
print("Total votes", total_votes)

