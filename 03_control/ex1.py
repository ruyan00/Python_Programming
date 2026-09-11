# 제어문 : if문, match문

age = 17

if age >= 18:
    print("성년")
else:
    print("미성년")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

# match문
grade = "A"

match grade:
    case "A":
        print("우수")  # break가 자동으로 실행
    case "B":
        print("양호")
    case "C" | "D":
        print("보통")
    case _:  # default에 해당
        print("알 수 없음")
