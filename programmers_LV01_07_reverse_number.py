# 내 풀이

def solution(n):
    answer = []
    
    while n > 0:
        answer.append(n % 10)
        n = n // 10 # 정수의 몫
    return answer

print(solution(12345))

# 다른사람 풀이
# 1. str(int형 변수) 사용하여 for 문
def solution(n):
    answer = []
    for num in str(n):
        answer.append(int(num))
    
    answer.reverse()
    return answer

print(solution(12345))

# 2. 
def solution(n):
    return [int(i) for i in str(n)[::-1]] # [::-1] 문자열 역순으로 리스트 저장

print(solution(12345))
