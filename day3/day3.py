
with open("day3/day3.txt", "r") as file:
    lines = [line.rstrip() for line in file]
i = 0

common_list =[]
badge_list = []

for i,line in enumerate(lines):
    line1 = line[:int((len(line))/2)]
    line2 = line[int((len(line))/2):]
    for char in line1:
        if char in line2:
            common_list.append(char)
            break

    
    if (i)%3== 0:
        for char in line:
            if char in lines[i+1] and char in lines[i+2]:
                badge_list.append(char)
                break
        
map="0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = 0
values2 =0

for a in common_list:
   values+=map.index(a)

for a in badge_list:
       values2+=map.index(a)

   
print(values2)


# DAY 3
