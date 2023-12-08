import sys
from collections import OrderedDict

file = sys.argv[1]

with open(file,"r") as f:
    lines = [line.split() for line in f.readlines()]

high_cards_conversion = { 'J':'U', 'Q':'V', 'K':'W', 'A':'X' }

hand_type_ranking = [ (1,1,1,1,1) , (1,1,1,2) , (1,2,2) , (1,1,3) , (2,3) , (1,4) , (5,) ]

for line in lines:

    for k,v in high_cards_conversion.items():

        line[0] = line[0].replace(k,v)

rankings = [[] for i in range(len(hand_type_ranking))]

for line in lines:

    hand,bid = line

    hand_type = [ hand.count(s) for s in "".join(OrderedDict.fromkeys(hand)) ]

    hand_type.sort()

    hand_type = tuple(hand_type)

    ranking = hand_type_ranking.index(hand_type)

    rankings[ranking].append((hand,int(bid)))

for r in rankings:

    r.sort()

solution = 0

rank = 1

for r in rankings:

    if not r:

        continue

    for i in r:

        hand,bid = i

        solution = solution + (rank * bid) 

        rank = rank + 1

print(solution)
