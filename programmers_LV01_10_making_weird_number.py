# 내 풀이

def solution(s):
    answer = ''
    idx = 1
    
    for i in range(0, len(s)):
        if s[i] == " ":
            idx = 1
            answer += " "
        elif s[i] != " " and idx % 2 == 1:
            idx += 1
            answer += s[i].upper()
        else:
            idx += 1
            answer += s[i].lower()
    
    return answer

print(solution("try hello world "))
