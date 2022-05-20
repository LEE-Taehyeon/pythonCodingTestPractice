# 내 풀이

a, b = map(int, input().strip().split(' '))
star = ""
for i in range(b):
    for j in range(a):
        star += "*"
    star += "\n"

print(star)



# 다른사람 풀이 참고
# 1. *와 \n(개행, 줄바꿈) 을 자유자재로 사용.
answer = ("*" * a + "\n") * b
print(answer)

# 2. for 문 사용.
for _ in range(b):
    print("*"*a)