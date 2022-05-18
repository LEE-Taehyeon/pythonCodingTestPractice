def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

print(solution([1,2,3,4]))

# 평균 구하기
list = [1,2,3,4,5,6,7,8,9,10]

# 1. for 문 이용
sum = 0;
for num in list:
    sum += num

print(sum / len(list))