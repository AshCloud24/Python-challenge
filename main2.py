import os
import csv
main2_csv = os.path.join ("..", "C:/Users/ashyg/OneDrive/Documents/GitHub/Python-challenge/PyPoll/Resources", "election_data.csv")
print(main2_csv)

with open(main2_csv) as main_file:
    data = csv.reader(main_file, delimiter= ",")
    next(data)
    ###### container

    num_candidates = {}
    Id = []


    for row in data:
        ##containers
        Id.append(row[0])
        candidates = row[2]
        ##count votes 
        total_votes = len(Id)
        print(total_votes)
        ##itemise
        num_candidates[candidates] = num_candidates.get(candidates,0) + 1
        
        
voted= []
for candidates, votes in num_candidates.items():
    percentage = (votes/total_votes)*100
    print(percentage)
    voted.append((candidates, percentage, votes))

won = max(voted, key=lambda x: x[2])
print(won)

##final 
print("Election Results")
print(f"total number of votes {total_votes}")
for canditates, percentage, votes in voted:
    print(f"{candidates}: {percentage:.2f}% ({votes})")
print(f"winner is: {won[0]} ")
