# 내 풀이

def solution(n):
    return sum([int(num) for num in str(n)])

print(solution(987))

# 다른사람 풀이
# 1. 재귀함수 이용
def solution(n):
    if n < 10:
        return n
    return (n % 10) + solution(n // 10)

print(solution(987))