from pprint import pp 

with open("day13/day13e.txt", "r") as file:
    lines_in = [line.rstrip() for line in file]

#prolly right but we need a while loop isntead so we can manipulate i
def parse(line):
    line_list = []
    for i, l in enumerate(line[1:]):
        if l == "[":
            li, i = parse(line[i+1:])
            line_list.append(li)
        elif l == "]":
            return line_list, i
        else:
            try:
                line_list.append(int(l))
            except:
                continue
        
i=1
def parse2(line, i):
    #print(line)
    line_list = []
    #print(len(line[1:]))
    while i < len(line):
        if line[i] == "[":
            li, i = parse2(line, i+1)
            line_list.append(li)
        elif line[i] == "]":
            #print(line[i], i)
            return line_list, i+1
        elif line[i] == ",":
            i+=1
            continue    
        else:
            line_list.append(int(line[i]))
            i+=1
            #if i == :
            #    #print(line[i], i)
            #    return line_list
            


line1 = parse2(lines_in[3], i)[0]
line2 = parse2(lines_in[4], i)[0]

print(line1)
print(line2)
pairs_r = []

if not isinstance(line2[1], list):
    print("ye")



print(pairs_r)
        
        