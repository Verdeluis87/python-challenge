#PyPoll
# Import the CSv reader and os
import os
import csv
from collections import Counter
# Create the Path to read the resources and open the file
csvpath = os.path.join('Resources', 'election_data.csv')

data = Counter()
# Read every line in the file and get the number of voters
with open(csvpath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        candidate = row['Candidate']
        data[candidate] += 1 

#sum the rows to get the number of voters
total = sum(data.values())
# Get the max value
maximum = max(data.values())
# Determine the winer
winners = [k for k, v in data.items() if v == maximum]

# Create a funtion to print the results
def print_line(file_obj, line):
        file_obj.write(line + "\n")
        print(line)

with open("results.txt","w") as f: #create add file in write mode
    print_line(f,'Election Results')
    print_line(f,'-------------------------')
    print_line(f,f'Total Votes: {total}')
    print_line(f,'-------------------------')
    for candidate, votes in data.items():
        percentage = (votes / total) * 100
        print_line(f,f'{candidate}: {percentage:.3f}% ({votes})')
    print_line(f,'-------------------------')
    print_line(f,f'Winner: {winners}')
    print_line(f,'-------------------------')