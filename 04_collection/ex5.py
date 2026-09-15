# 딕셔너리 기초

# ===========================================================
#  딕셔너리 (dict): 키와 값 쌍으로 저장하는 변경 가능한 자료형
#  딕셔너리의 특징
#  1. ( mutable, 변경 가능 )
#  2. ( iterable, 반복 가능 )
#  3. ( sequence X, 인덱싱과 슬라이싱 불가 )
#  4. ( 키는 중복 불가, 값은 중복 가능 )
# ===========================================================

# 딕셔너리 생성
a = {}
b = dict()
print(type(a), type(b))

d = {"id": 1404, "name": "김나연", "age": 17}
print(d)

# 키로 값 가져오기
print(d["name"])
# print(d["phone"])

# 에러가 안나게 하려면?
if "phone" in d:
    print(d["phone"])

print(d.get("phone"))
print(d.get("phone", "전화없음"))

# ===========================================================
# 1. 딕셔너리는 mutable하다. (변경 가능)
# ===========================================================

d["age"] += 1
print(d)

d["phone"] = "123-4567"
print(d)

del d["phone"]
print(d)

print(d.pop("age"))
print(d)

# ===========================================================
# 2. 딕셔너리는 iterable하다. (반복 가능)
# ===========================================================

# 딕셔너리 순회
for data in d:
    print(data, d[data])

for i, data in enumerate(d):
    print(i, data)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

print(d)
a = d.items()
d["key"] = 100
print(a)

# ===========================================================
# 3. 딕셔너리는 sequence 객체가 아니다. (인덱싱, 슬라이싱 불가)
# ===========================================================

d[0] = "python"  # 0은 인덱스가 아니라 key값임
print(d)

# ===========================================================
# 4. 딕셔너리는 키는 중복 불가, 값은 중복 가능하다.
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}

d["kor"] = 100
print(d)

d["sci"] = 80
print(d)

# 키로 가능한 것 : immutable 타입 (숫자형, 불리언, 문자열, 튜플) -> hashable type
# 키로 안되는 것 : mutable 타입 (리스트, 딕셔너리, 집합) -> unhashable type
# 키는 해시 가능(hashable) + 프로그램 실행 동안 hash값이 변하지 않아야 함

d[3.14] = 100
print(d)

# d[[1, 2]] = 10
# print(d)

d[(1, 2)] = 10
print(d)

# d[{"key1": 100}] = 10
# print(d)

# 딕셔너리가 저장되는 방식
# 1. 딕셔너리 데이터를 저장하기 위한 해시 테이블을 생성함
# 2. hash(key) 함수를 통해 hash값을 얻음
# 3. hash값을 테이블 크기로 압축하여 버킷 인덱스를 계산하고 해시 테이블에 저장함
# 4. key값으로 조회할 때에도 hash(key)로 hash값을 얻어낸 후(동일 hash값) 해당 인덱스로 가서 조회함

# 만약 key에 mutable 타입을 허용했다면?
# 1. hash(key) 함수로 hash값을 얻어 해시 테이블에 저장함
# 2. key 내용이 변경됨
# 3. 다시 hash(바뀐key)를 하면 새로운 hash값이 나옴
# 4. 새 hash값을 이용하여 버킷 인덱스를 계산하고 해시테이블에 조회를 하면 원래 데이터를 찾을 수 없음

print(hash(123))
print(hash("hi"))
print(hash("hi"))
print(hash((1, 2)))
print(hash((1, 2)))

# ===========================================================
#  파이썬 내장 함수
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}

print(len(d))
# print(sum(d))
print(sum(d.values()))
print(min(d), min(d.values()))
print(max(d), max(d.values()))

print(sorted(d))
print(sorted(d.items()))
print(dict(sorted(d.items(), reverse=True)))


# value 기준으로 정렬
def key(x):  # (key, value)
    return x[1]  # 정렬에 사용할 키를 리턴


print(dict(sorted(d.items(), key=key)))
print(dict(sorted(d.items(), key=key, reverse=True)))

# 정렬 기준 설정하기
# lambda: 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda 매개변수1, 매개변수2, ... : 표현식

print(dict(sorted(d.items(), key=lambda x: x[1])))

# 딕셔너리 합치기
# d2 = {"sci": 95, "prog": 100}
# print(d + d2)

# 딕셔너리 반복하기
# print(d * 2)

# 멤버십 연산자
print("kor" in d)
print("art" in d)
