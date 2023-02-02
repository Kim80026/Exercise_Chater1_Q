# Q2 Answer template
# Q2 (https://www.acmicpc.net/problem/1110)

N = int(input())
tmp = N  #첫번째 값과 비교하기위해 tmp에 N을 저장
tens = N // 10 #10의 자리값
ones = N % 10 #1의 자리값
count = 0

while 1:
    N = tens + ones #더한값 수 만들기
    count += 1
    tens = ones #주어진 수 가장오른쪽 자리 수
    ones = N % 10 #더한값 수 가장오른쪽 자리 수
    res = tens * 10 + ones # 새로 만들어진 수
    if res == tmp:
        break
    
print(count)
