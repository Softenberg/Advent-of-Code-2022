from pprint import pprint as pp
import numpy as np

with open("day 11/day11.txt", "r") as file:
    lines = [line.rstrip() for line in file]

monkey_list = []

#shitty syntax for splitting stuff
def strip_split_list(li, stripee):
    li=li.split(" ")
    for j, k in enumerate(li):
        li[j] = k.strip(stripee)
    return li

# prep
for i, line in enumerate(lines):
    if "Monkey" in line:
        items = strip_split_list(lines[i+1], ",")[4:]
        operation = strip_split_list(lines[i+2], " ")[6:]
        test_div = strip_split_list(lines[i+3], " ")[-1]
        true = lines[i+4][-1]
        false = lines[i+5][-1]
        monkey_list.append([items, operation, test_div, true, false, 0])


def calc_worry(monkeys, monkey_i):
    for i, ba in enumerate(monkeys[monkey_i][0]):
        item =int(monkeys[monkey_i][0][i])
        old = monkeys[monkey_i][1][1]
        div = int(monkeys[monkey_i][2])
        instruction = monkeys[monkey_i][1][0]
        throw_t = int(monkeys[monkey_i][2][0])
        throw_f = int(monkeys[monkey_i][2][0])

        if old == "old":
            old = item
        else:
            old = int(old)

        if instruction == "*":
            item=(item * old)//3
        if instruction == "+":
            item=(item + old)//3

        monkeys[monkey_i][0][i] = item
        monkeys[monkey_i][5] += 1

    
def throw(monkeys, monkey_i):
    for i in range(len(monkeys[monkey_i][0])):
        item =int(monkeys[monkey_i][0][0])
        div = int(monkeys[monkey_i][2])
        throw_t = int(monkeys[monkey_i][3][0])
        throw_f = int(monkeys[monkey_i][4][0])
        print(div)
        #print(monkeys[throw_t][0])
        if item % div == 0:
            monkeys[throw_t][0].append(monkeys[monkey_i][0].pop(0))  
        else:
            monkeys[throw_f][0].append(monkeys[monkey_i][0].pop(0))
        
    
     

for round in range(20):
    for i, monkey in enumerate(monkey_list):
        calc_worry(monkey_list, i)
        throw(monkey_list, i)


big_list = []
for i, monkey in enumerate(monkey_list):
    print(monkey)
    big_list.append(monkey[5])

big_list.sort()
print(big_list)
print(big_list[-1]*big_list[-2])



