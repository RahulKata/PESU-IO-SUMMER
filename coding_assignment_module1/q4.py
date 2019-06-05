while(True):
    inp = int(input("Enter a number with more than 1 digit: "))
    if(inp>=10):
        break
sum = 0
while(inp>0):
    digit = inp %10
    sum += digit
    inp //= 10
print("Sum of digits is ", sum)
