with open("day5/day5.txt", "r") as file:
    lines = [line.rstrip() for line in file]

listslist=[]
for i in range(9):
    templist =[]
    listslist.append(templist)    

for line in lines:
    for i in range(1,40,2): 
        try:
            if line[i] == " ":
                continue
            else:
                if i == 1:
                    listslist[0].append(line[i])
                else:
                    listslist[round((i-1)/4)].append(line[i])    
        except IndexError:
            continue
    
    if line[-1] == "9":
        break

for i in listslist:
    i.reverse()


for line in lines:
    if line[0] == "m":
        #print(line)    
        amount=int(line[5:7])
        fro = int(line[12:14])-1
        to = int(line [17:19])-1
        print(amount, fro, to)
        print(listslist)
        templist = listslist[fro][-amount:len(listslist[fro])]
        listslist[fro]=listslist[fro][0:-amount]
        print(templist)
        for i in templist:
            listslist[to].append(i)
    
final_string=""    
for i in listslist:
    final_string+=i.pop(-1)

print(final_string)