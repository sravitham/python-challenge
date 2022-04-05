# Import the necessary dependencies for os.path.join()
import os
import csv

# Read in a .csv file
csv_path_input = "PyPoll/Resources/election_data.csv"
path_output = "analysis/election_analysis_2.txt"

with open(csv_path_input) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    
    #creating indexed list to contain unique candidates
    candidates_list = []
    #create a dictionary that contains the total votes for each candidate
    candidate_votes = {}
    #intialize variables
    total_votes = 0

#readind through each row in the csv file
    for row in csv_reader:
        #add a vote for each new row
        total_votes += 1
        #get first candidate name in the dataset
        candidate_name = (row[2])
        #check whether the candiate is in the list before appending and initialize the vote count
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #add a vote count for each candidate
        candidate_votes[candidate_name] += 1

#print analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]
    vote_percentage = (votes / total_votes) * 100
    vote_percentage = round(vote_percentage, 3)


    voter_stats = (f"{candidate_name} : {vote_percentage}% ({votes})")
    print(voter_stats)
print("-------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
print("Winner:",winner)

#print output file to text file
with open('PyPoll\Analysis\Analysis.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("-------------------------\n")
    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]
        vote_percentage = (votes / total_votes) * 100
        vote_percentage = round(vote_percentage, 3)


        voter_stats = (f"{candidate_name} : {vote_percentage}% ({votes})")
        text.write(f"{voter_stats}\n")
    text.write("-------------------------\n")
    winner = max(candidate_votes, key=candidate_votes.get)
    text.write(f"Winner: {winner}")

