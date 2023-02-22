lst = [1,4,7,12,47,3,10]
element = 7

#search
flag = 0
for i in range(len(lst)):
    print(lst[i],",", element)
    if lst[i] == element:
        flag = 1
        x = i
        break
        
if flag == 1:
    print("True")
    print(x)
else:
    print("False")