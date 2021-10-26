i = 0
total = 0
while i<=9999:
    combination = str(i)
    one = combination[0]
    if len(combination) < 2:
        two = 0
    else:
        two = combination[1]
    if len(combination)< 3:
        three = 0
    else:
        three = combination[2]
    if len(combination) < 4:
        four = 0
    else:
        four = combination[3]
    if int(one) + int(two) + int(three) + int(four) == 10:
        total = total  + 1
    i = i + 1
print(total)
    