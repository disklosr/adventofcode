def get_num_possible_passwords(start, end):
    counter = 0

    for x1 in range(0,10):
        for x2 in range(x1,10):
            for x3 in range(x2, 10):
                for x4 in range(x3, 10):
                    for x5 in range(x4, 10):
                        for x6 in range(x5, 10):
                            if(x1==x2 or x2 == x3 or x3 == x4 or x4 == x5 or x5 == x6):
                                number = int("%d%d%d%d%d%d" %(x1,x2,x3,x4,x5, x6))
                                if(number >= start and number <= end):
                                    if(is_valid([x1,x2,x3,x4,x5,x6])):
                                        counter += 1

    return counter

def is_valid(digits):
    count = {}
    lastdigit = -1
    for digit in digits:
        if lastdigit == digit:
            count[digit] += 1
        else:
            count[digit] = 1
            lastdigit = digit

    if 2 in count.values():
        return True
    else: 
        return False

count = get_num_possible_passwords(359282, 820401)
print(count)