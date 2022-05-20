# 내 풀이

def solution(x, n):
    idx = 1
    list = [x]
    while idx < n:
        list.append((1 + idx) * x)
        idx += 1
    answer = list
    return answer


# 다른사람 풀이 참고
# 1. for 문 간단하게
def solution(x, n):
    list = [(i + 1) * x for i in range(n)]
    return list

print(solution(-4, 5))


# 2. 내 풀이를 for 문으로
def solution(x, n):
    list = []
    for i in range(n):
        list.append(x * (i + 1))
        
    return list