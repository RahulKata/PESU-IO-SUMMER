str = str(input("Enter comma seperated numbers: "))
list = str.split(",") 
print(list)
li = []
for i in list:
    li.append(int(i))
print("The List of numbers is: ",li)
tuple = tuple(li)
print("The Tuple of numbers is: ",tuple)