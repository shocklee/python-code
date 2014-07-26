def nested_sum(intList):
    return sum(intList)

def add_all(t):
    total = 0
    for i in range(len(t)):
        if(type(t[i]) == list):
            total += nested_sum(t[i])
        elif(type(t[i]) == tuple):
            print t[i], 'is type tuple'
        elif(type(t[i]) == int):
            total += t[i]
        else:
            print t[i], 'is', type(t[i])
    print 'The total is', total

sample_list = [1, 2, 3, [1, 2, 3], (1, 2, 3), 'a']
add_all(sample_list)
