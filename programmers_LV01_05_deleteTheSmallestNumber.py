# 내 풀이
def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    else:
        return arr.sort()[1:].reverse()
    
print(solution([4,6,2,3,8,1]))