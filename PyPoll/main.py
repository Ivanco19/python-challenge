# Import libraries
import csv, os

# Filepath of our database
file_path = os.path.join('.','PyPoll\Resources', 'election_data.csv')

with open(file_path) as my_file:
    csv_iterable = csv.reader(my_file)

    # We store the candidate names in a list 
    for candidates in csv_iterable:
        candidates_names = [fila[2] for fila in csv_iterable]

    # We create a dictionary to store number of votes per candidate
    votes_per_candidate = {}

    # It counts votes per candidate
    for candidate in set(candidates_names):
        votes = candidates_names.count(candidate)
        votes_per_candidate[candidate] = votes

    # Calculate total of votes
    total = sum(votes_per_candidate.values())

    # Print total votes
    print("Election Results")
    print("-------------------------")
    print("Total Votes:", total)
    print("-------------------------")

    # Print candidate, and votes per candidate (nuemeric and percentage)
    for candidate, votes in votes_per_candidate.items():
        print(f"{candidate}: {round((votes * 100/total),3)}% ({votes})")

    # Print winner
    winner = max(votes_per_candidate, key=votes_per_candidate.get)
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")


# This code exports the results to an txt file
with open('pypoll_results.txt', 'w') as my_writer:
    my_writer.write('Election Results \n')
    my_writer.write('------------------------- \n')
    my_writer.write(f'Total Votes: {total} \n')
    my_writer.write('------------------------- \n')
    for candidate, votes in votes_per_candidate.items():
        my_writer.write(f'{candidate}: {round((votes * 100/total),3)}% ({votes}) \n')
    my_writer.write('------------------------- \n')
    my_writer.write(f'Winner: {winner} \n')
    my_writer.write('------------------------- \n')
 