# 내 풀이

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arrCopy = arr.copy()
        arrCopy.sort()
        min = arrCopy[0]
        arr.remove(min)
        
        return arr
    
print(solution([4,6,2,3,8]))

# 다른사람 풀이
# 1. min() 이용
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        
        return arr
    
print(solution([4,6,2,3,8]))

# 2. for 문과 if문 한문장으로
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        return [num for num in arr if num > min(arr)]
    
print(solution([10]))