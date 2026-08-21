# 변수
a = 2
b = 3
print(a, b)

# a = 2, b = 3 (error)
# a = (2, b) = 3

a = 2
b = 3
a, b = 2, 3  # 권장
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 불가
# 예약어 금지
# 대소문자 구분

# name! = "뽀로로"
# 2name = "크롱"
_age = 23
# class = "클래스"

이름 = "뽀로로"  # 비권장
print(이름)

student_name = "크롱"  # snake
studentName = "크롱"  # camel

MAX_SCORE = 100
