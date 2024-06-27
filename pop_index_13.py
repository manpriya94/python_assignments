ipl = ['CSK','MI','KKR','LSG','PBKS']

user = input("enter your favourite ipl team")

# 1st way
newipl = []
# 1st way
for i,team in enumerate(ipl):
    if team != user:
        newipl.append(team)
print(newipl)

# 2nd way
team_elements = ipl.copy()
team_elements.pop(ipl.index(user))
print(team_elements)
