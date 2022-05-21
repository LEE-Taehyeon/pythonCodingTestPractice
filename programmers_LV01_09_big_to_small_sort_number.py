# 내 풀이

def solution(n):
    list = [num for num in str(n)]
    print(type(list))
    list.sort()
    list.reverse()
    
    return int("".join(list)) # 리스트를 문자열로 만들기

print(solution(118372))

# 다른사람 풀이
def solution(n):
    list1 = list(str(n)) # 문자열 하나하나씩 리스트 값으로 넣기.
    print(type(list1))
    list1.sort(reverse = True) # reverse sorting
    
    return int("".join(list1))

print(solution(118372))