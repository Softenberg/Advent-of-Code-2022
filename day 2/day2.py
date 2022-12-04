f = open("day 2/example_data.txt", "r")
score = 0
ABC=["A", "B", "C"]
XYZ=["X", "Y", "Z"]

for line in f:
    opp = line[0]
    outcome = line[2]
    opp=ABC.index(opp)
    
    if outcome == "Y":
        me = opp
    elif outcome == "X":
        me = opp + 1
        if me == 3:
            me =0
    else:
        me = opp - 1
        if me == -1:
            me =2
    
    
    
       
    if me == opp + 1 or (me ==0 and opp ==2):
        score += 6
    elif me == opp:
        score += 3

    score = score + me + 1

print(score)    

# A = rock
# B = paper
# C = Scissors

# X = Win
# Y = Draw
# Z = Loss

