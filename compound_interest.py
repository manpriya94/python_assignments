
principle = int(input("enter principle amount :"))
rate = float(input("enter rate :"))

total_amount = principle * ((1 + rate/100) ** 2)
print(total_amount)
