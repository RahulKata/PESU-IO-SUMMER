length = int(input("Enter the length of the desired list you want to create: "))
num_list = [int(input("Enter a number: ")) for i in range(0,length)]
print(num_list)
num_list.sort()
print("Sorted list is: ",num_list)
search = int(input("Enter the number you want to search for: "))


def binarySearch(list,item,upper):
    lower = 0
    pos = 0
    found = False
    while(lower <= upper and not found):
        mid = (upper + lower)//2
        if list[mid] == item:
            found = True
            pos = mid
        else:
            if item < list[mid]:
                upper = mid-1
            else:
                lower = mid + 1
    return found,pos


srh,pos = binarySearch(num_list,search,length)
if(srh):
    print(search," found at ", pos+1)
else:
    print(search," is not present in the list!")

