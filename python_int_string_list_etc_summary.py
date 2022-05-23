# 변수에 if 문 사용
select_value = True if True else False

# for 문에 문자열 가능
for s in str("string"):
    print(s)

# list
# 1. 빈 리스트 선언
empty_list1 = []
empty_list2 = list()

# 2. 자료형 리스트 선언
# 1) int 형 리스트 선언
int_list1 = [1,6,4,68,23,5,4,12]
# 2) mix 리스트 선언
mix_list1 = [2, "string", True]
# 3) range 를 이용해서 선언
range_list1 = list(range(0, 10))

# 3. 리스트 추가 제거
int_list1.append(10) # 뒤에 해당 요소들 추가
int_list1.remove(6) # 가장 앞에서 해당하는 요소 제거, 해당하는 요소 없으면 에러 발생

# 4. 리스트 정렬
int_list1.sort() # 오름차순 정렬
int_list1.sort(reverse=True) # 내림차순 정렬
int_list1.reverse() # 내림차순 정렬

# 5. 리스트 슬라이싱
list_slicing = int_list1[0:3]
print(list_slicing)


# 문자열을 리스트로 저장
str_to_list1 = [str for str in "string123"[0:]]
str_to_list_reverse1 = [str for str in "string123"[::-1]]
str_to_list2 = sorted("string123")
str_to_list_reverse2 = sorted("string123", reverse=True)
print(str_to_list1)
'''
    sort(리스트) 와 sorted(리스트, 문자열) 의 차이 - sort() 는 본체의 리스트를 정렬해서 반환 / sorted() 는 정렬한 새로운 리스트 반환
'''


# 리스트를 문자열로 저장
list_str = "".join(str_to_list1)
print(list_str)




















