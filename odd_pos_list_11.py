list1 = [1,2,3,4,5,6,7,8]
newlist = []
for i in range(len(list1)):
    if i%2 != 0:
        newlist.append(list1[i])

print("my new list is : ", newlist)
