#User imput
n = int(input("Enter a positive integer: "))

#Function to check whether the input is positive, else compute its factorial
if (n <=0):
    raise Exception('Input must not be negative')
else:
    fac = 1
    for j in range(1,n+1):
        # multiplying the integer with every positive integer less than itself
        fac = fac*j

print(fac)