with open("day6/day6.txt", "r") as file:
    lines = [line.rstrip() for line in file]

def mess(win):
    for i in range(len(lines[0])-win):
        if len(set(lines[0][i:i+win])) == win:
            return(i+win)
        
#p1
print("p1: ", mess(4))
#p2
print("p2: ", mess(14))

    
    

    