ipl = ['CSK','MI','KKR','LSG','PBKS']

user = input("enter your favourite ipl team")

# 1st way
for i,team in enumerate(ipl):
    if team == user:
        print(ipl[i:])

# 2nd way
i = ipl.index(user)
print(ipl[i:])



