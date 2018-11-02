import os
from collections import Counter

csvpath = os.path.join("election_data.csv") 

import csv
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

   #lists
    voterid = []
    county = []
    candidates = []
    
    for row in csvreader:
        voterid.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    can_set = set(candidates)    
    total_vote = len(voterid)
    cnt = Counter(candidates)

    can_names = []
    
    for row in can_set:  
        can_names.append(row)

    print("Election Results")
    print("----------------------------------------")
    print(f"The total number of votes is {total_vote}")
    print("----------------------------------------")

    dictionary_can = {}
    can_count = 0
    for row in can_names:
        candidate_name = str(can_names[can_count])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes / total_vote * 100, 2)
        dictionary_can.update({ candidate_name : votes})
        print(f"{candidate_name}: {percentage}%  ({votes} votes)" )
        can_count = can_count + 1

    import operator

    winner = max(dictionary_can, key=lambda key: dictionary_can[key])
    
    print("Winner: ", winner)