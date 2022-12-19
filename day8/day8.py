from pprint import pprint as pp
with open("day8/day8e.txt", "r") as file:
    lines = [line.rstrip() for line in file]


#                   
#visibility(data,     move y,   move x)
def visibility(data, move_y, move_x):
    prev = data[move_y][move_x]
    vis = False
    #pp(prev)
    
    # down
    for y in range(move_y+1, len(data)):
        if prev > data[y][move_x]:
            prev=data[y][move_x]
            vis = True
        else:
            vis = False
            break
            
    if vis:
        return vis
    
    #up
    for y in range(move_y-1, 0, -1):
        if prev > data[y][move_x]:
            prev=data[y][move_x]
            vis = True
        else:
            vis = False
            break

    if vis:
        return vis

    #left
    for x in range(move_x-1, 0, -1):

        if prev > data[move_y][x]:
            prev=data[move_y][x]
            vis = True
        else:
            vis = False
            break
    
    if vis:
        return vis

    # right
    for x in range(move_x+1, len(data[0])):
        if prev > data[move_y][x]:
            prev=data[move_y][x]
            vis = True
        else:
            vis = False
            break
    return vis



lines2 = []
for i in lines:
    lines2.append([int(x) for x in i])  

count= 0
score =0
for i, line in enumerate(lines2):   
    if i == len(lines2[0])-2: break 
    #print(i)
    for k in range(1, len(lines)-1):
        print(i+1, "   ", k)
        print(visibility(lines2, k+1, i))
        if visibility(lines2, k+1, i):
            score +=1
        count+=1



#score+=2*(len(lines)-1)     #added right and left
#score+=2*(len(lines[0])-1)    #added top and bottom

print(score)