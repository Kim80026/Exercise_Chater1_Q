# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')

res = 0
for i in data:
    i = int(i)
    if i == 0:
        continue
    
    if res == 0:
        res += i
    else:
        res = res * i 
print(res)