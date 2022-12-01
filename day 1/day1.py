f = open("day 1/day1.txt", "r")
counter = 0
values = 0
value_list = []

for line in f: 
    counter = counter + 1
    if len(line) > 1:
        counter = counter+1
        values = values + int(line)
    else:
        value_list.append(values)
        counter = 0
        values = 0

print(max(value_list))
##uppgift 2

top_three = 0 

for i in range(1,4):
    value_list.sort()   
    top_three = top_three+value_list[-i]

    
print(top_three)