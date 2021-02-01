

number = int(input())
result = sum(map(lambda x: str(x).count('1'), range(1,number+1)))
print(result)

