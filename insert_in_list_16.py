ipl = ['CSK','MI','KKR','LSG','PBKS']

user = input("enter index and your favourite ipl team")
new_ipl = ipl.copy()

input_split = user.split(',')
index = int(input_split[0])
new_ipl.insert(index, input_split[1])

print(ipl)
print(len(ipl))
print(new_ipl)
print(len(new_ipl))

