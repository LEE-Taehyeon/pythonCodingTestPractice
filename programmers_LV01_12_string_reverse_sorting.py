# 내 풀이

def solution(s):
    answer = ''
    str_to_list = list(s)
    
    str_to_list.sort(reverse=True)
    for str in str_to_list:
        answer += str
    
    return answer

print(solution("Zbcdefg"))

# 다름사람 풀이
def solution(s):
    return "".join([str for str in s[::-1]])

print(solution("Zbcdefg"))

def solution(s):
    return "".join(sorted(s, reverse=True))

print(solution("Zbcdefg"))