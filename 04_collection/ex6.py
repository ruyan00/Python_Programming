# 딕셔너리 심화

# ===========================================================
#  딕셔너리에서 제공하는 메소드
# ===========================================================

d = {"name": "뽀로로", "age": 5}

d2 = {"age": 23, "city": "일산"}

d.update(d2)  # upsert
print(d)

print(d.pop("city"))
print(d)

d.clear()
print(d)

# ===========================================================
#  그 외
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80, "prog": 100}

# 딕셔너리 언패킹
print(*d)

a, *b, c = d
print(a, b, c)

print({**d})

d2 = {"eng": 90, "sci": 95}
print({**d, **d2})  # update와 동일하게 동작

# 위 딕셔너리를 key 리스트와 value 리스트로 만들기
print(list(d))
print(list(d.values()))

# 리스트를 다시 딕셔너리로 만들기
# zip 함수로 튜플을 먼저 만들고, dict()에서 튜플의 [0]값을 key로, [1]값을 value로 넣음
subjects = list(d)
scores = list(d.values())
print(dict(zip(subjects, scores)))

# ===========================================================
#  딕셔너리 Comprehension
# ===========================================================

# 1 ~ 10의 제곱수 딕셔너리 만들기
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25 .. }
result = {x: x**2 for x in range(1, 11)}
print(result)

# 1 ~ 10 중 홀수 제곱수로 된 딕셔너리 만들기
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
result = {x: x**2 for x in range(1, 11, 2)}
print(result)

# 위 result 딕셔너리의 키를 값으로, 값을 키로 바꾸기
# {1: 1, 9: 3, 25: 5, 49: 7, 81: 9}
result = {v: k for k, v in result.items()}
print(result)

# 점수 90 이상만 필터링하기
scores = {"국어": 90, "영어": 85, "수학": 95, "과학": 89}
result = {k: v for k, v in scores.items() if v >= 90}
print(result)

# =========================================================
#  🔥 실습 문제
# =========================================================

# 1️⃣ 바구니에 있는 과일의 단어 개수 세기
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# ✅ {'apple': 3, 'banana': 2, 'cherry': 1}
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

# 2️⃣ 60점 이상인 경우 합격 설정하기
scores = {"국어": 85, "영어": 50, "수학": 95, "과학": 40, "사회": 72}


# ✅ {'국어': '합격', '수학': '합격', '사회': '합격'}
print({k: "합격" for k, v in scores.items() if v >= 60})

# 3️⃣ 과목 리스트와 점수 리스트로 딕셔너리 만들기
subjects = ["국어", "영어", "수학"]
grades = [90, 80, 100]


# ✅ {'국어': 90, '영어': 80, '수학': 100}
print(dict(zip(subjects, grades)))

# 4️⃣ 기존 재고에 입고 내역을 합치기 (이미 있는 상품은 합산, 새 상품은 추가)
stock = {"연필": 10, "지우개": 5, "노트": 3}  # 기존 재고
incoming = {"지우개": 4, "노트": 7, "볼펜": 12}  # 입고 내역


# ✅ {'연필': 10, '지우개': 9, '노트': 10, '볼펜': 12}
stock.update({i: stock[i] + j if i in stock else j for i, j in incoming.items()})
print(stock)
