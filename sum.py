def find_sum(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
call_sum=find_sum(50)
print("sum of number is:",call_sum)