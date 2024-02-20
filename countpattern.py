#function to count the number of times the pattern appears in  the list

def count_pattern(pattern, mylist):
    count = 0
    #finding the maximum possible number of times the pattern can appear in the list
    for j in range(len(mylist) - len(pattern) + 1):
        if mylist[j:j+len(pattern)] == pattern:
            count += 1
    return count

#User input list, parameter for the list
lst = input('Enter list: ')

#User input pattern, parameter for the pattern
pat = input('Enter pattern: ')

#Pass our arguments for the pattern and the list to our functon
print(count_pattern(pat, lst))
