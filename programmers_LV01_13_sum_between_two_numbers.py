# 내 풀이

def solution(a, b):
    answer = 0
    
    if a == b:
        return a
    elif a < b:
        answer = sum_between_two_nums(a, b)
    else:
        answer = sum_between_two_nums(b, a)
        
    return answer

def sum_between_two_nums(num1, num2):
    return sum(num for num in range(num1, num2+1))

print(solution(5, 3))

# 다른사람 풀이
def solution(a, b):
    return sum(range(min(a, b), max(a, b)+1))

print(solution(5, 3))