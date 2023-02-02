# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')

result = int(data[0])

print(result, end='')

for i in range(1, len(data)):
    num = int(data[i])
    
    if num <= 1 or result <= 1:
        result += num
        print('+ ' + str(num), end='')
    else:
        result *= num
        print('* ' + str(num), end='')
        
print(' = ' + str(result))