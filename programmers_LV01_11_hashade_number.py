# 내 풀이

def solution(x):
    return x % sum([int(num) for num in list(str(x))]) == 0

print(solution(181))

# 다른사람 풀이
def solution(x):
    return x % sum([int(num) for num in str(x)]) == 0 # 문자열을 굳이 list 로 변환하지 않아도 된다.

print(solution(11))


def solution(x):
    sum = 0
    st = str(x)
    
    for i in range(0, len(str(x))):
        sum += int(st[i])
        
    return x % sum == 0

print(solution(11))
