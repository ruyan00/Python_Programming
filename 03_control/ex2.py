# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    # if i == 5:
    #     break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
i = 0

while i < 5:  # while len(i) < 5:
    if nums[i] == target:
        print(f"{target} found.")
        break
    i += 1
else:
    print(f"{target} not found")

# if not found:
# print(f"{target} not found")

# 1 ~ 10까지의 합
# sum = 55
i = 1
tot = 0

while i < 11:
    tot += i
    i += 1
else:
    print(f"sum = {tot}")

# 짝수만
i = 1
tot = 0
while i < 11:
    if i % 2 == 0:
        tot += i
        i += 1
    else:
        i += 1
else:
    print(f"sum = {tot}")

while i <= 10:
    i += 1
    if i % 2 == 1:
        continue
    tot += i

print(f"tot = {tot}")
