lst = [1, 4, 7, 8, 11, 15, 20, 25]
element = 25

low = 0
high = len(lst)-1

while low <= high:
    
    mid = (low + high)//2
    if element == lst[mid]:
        print(element,"is present at", mid)
        break
    elif element < lst[mid]:
        high = mid-1
    else:
        low = mid+1