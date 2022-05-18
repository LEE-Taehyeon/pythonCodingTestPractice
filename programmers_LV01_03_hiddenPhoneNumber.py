# 내 풀이

def solution(phone_number):
    length = len(phone_number) - 4
    answer = str("*" * length + phone_number[length:])
    return answer

print(solution("01012345678"))