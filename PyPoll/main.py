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

    candidates_list = []
    candidate_votes = {}

    total_votes = 0

    for row in csv_reader:
        total_votes += 1

        candidate_name = (row[2])

        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

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

