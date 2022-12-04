with open("day4/day4.txt", "r") as file:
    lines = [line.rstrip() for line in file]

contains_counter=0
counter2 = 0 

for i, line in enumerate(lines):
    
    fir_elf=line[:line.index(",")]
    sec_elf=line[line.index(",")+1:]
    
    #create range
    r1 = int(fir_elf[:fir_elf.index("-")])
    r2 = int(fir_elf[fir_elf.index("-")+1:])
    r3 = int(sec_elf[:sec_elf.index("-")])
    r4 = int(sec_elf[sec_elf.index("-")+1:])
    
    if r1 >= r3 and r2 <= r4:
        contains_counter+=1
    elif r3 >= r1 and r4 <= r2:
        contains_counter += 1

    #part2
    for k in range(r1,r2+1):
        if k in range(r3,r4+1):
            counter2+=1
            break
    
        
print("part1: ",contains_counter)    
print("part2: ",counter2)    


    