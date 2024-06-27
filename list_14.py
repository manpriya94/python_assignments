ipl = ['CSK','MI','KKR','LSG','PBKS']

user = input("enter index and your favourite ipl team")

newiplteam = user.split(',')
print(newiplteam)
ipl[int(newiplteam[0])] = newiplteam[1]

print(ipl)





