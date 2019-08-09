import os
import csv



def main():
    poll_csv = os.path.join("PyPoll","Resources", "election_data.csv")

    election_results = {}

    #loop through file and count all votes for each candidate
    with open(poll_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        next(csv_reader)

        for row in csv_reader:
            if row[2] in election_results:
                election_results[row[2]] = election_results[row[2]] + 1
            else:
                election_results[row[2]] = 1       
        
    total_votes = sum(value for value in election_results.values())
    max_votes = max(value for value in election_results.values())

    # format final output
    final_output = []
    final_output.append("Election Results")
    final_output.append("-------------------------")
    final_output.append(f"Total Votes: {total_votes:,}")
    final_output.append("-------------------------")

    for candidate, vote_count in election_results.items():
        final_output.append(f"{candidate}: {(vote_count/ total_votes) * 100:,.3f}% ({vote_count:,} votes)")
        if vote_count == max_votes:
            winner = candidate

    final_output.append("-------------------------")
    final_output.append(f"Winner: {winner}")
    final_output.append("-------------------------")

    #write results to a file
    with open("pyPoll_Results.txt","w") as results_file:
        for row in final_output:
            results_file.write(row + "\n")

            
    #this sweet little statement will print each item in my "final output" list on a new line
    print("""{}""".format("\n".join(final_output[0:])))


if __name__ == "__main__":
    main()

