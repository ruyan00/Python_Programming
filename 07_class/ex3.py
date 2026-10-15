# 3. 다형성 (Polymorphism)

# ===========================================================
#  1. 다형성이란?
#  - 같은 이름의 메소드를 호출해도, 객체의 종류에 따라 ( 서로 다르게 ) 동작하는 성질
#  - 전자제품의 "전원" 버튼 : TV, 에어컨, 세탁기에 있는 전원버튼은 같지만 실제 동작은 모두 다르다.
#  - 일반적으로 ( 상속 ) + ( 메소드 오버라이딩 )으로 다형성을 구현한다. (파이썬은 같은 이름의 메소드만 있으면 다형성 성립)
# ===========================================================

# 이미 우리가 쓰고 있던 다형성 기능
print(1 + 2)
print("1" + "2")
print([1] + [2])

# ===========================================================
#  2. 다형성 없이 구현한다면?
# ===========================================================


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name}: 멍멍")


class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name}: 야옹")


def make_sound(animal):
    if isinstance(animal, Dog):
        animal.bark()
    elif isinstance(animal, Cat):
        animal.meow()


make_sound(Dog("멍멍이"))
make_sound(Cat("야옹이"))

# ===========================================================
#  3. 다형성 구현 (상속 + 오버라이딩)
# ===========================================================


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: ...")


class Dog(Animal):
    def speak(self):
        print(f"{self.name}: 멍멍")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 야옹")


class Cow(Animal):
    def speak(self):
        print(f"{self.name}: 음메")


# 새로운 클래스를 추가해도 make_sound2()는 그대로 사용 가능
# 확장에는 열려있고, 수정에는 닫혀있다.
def make_sound2(animal):
    animal.speak()


make_sound2(Dog("멍멍이"))
make_sound2(Cat("야옹이"))
make_sound2(Cow("얼룩이"))

# 자식 객체 리스트 생성
animals = [Dog("멍멍이"), Cat("야옹이"), Cow("얼룩이")]

for a in animals:
    a.speak()

# (참고) 덕 타이핑(Duck typing)
# - 파이썬은 함수 호출 시 객체의 타입을 검사하지 않음 (실행 시 메소드만 확인)
# - 따라서, 같은 이름의 메소드만 있으면 다형성을 구현할 수 있음
# - 파이썬에서는 상속이 다형성의 필수 조건은 아니지만 메소드가 없으면 에러가 나므로 주의!


class Duck:
    def speak(self):
        print("꽥꽥")


class Robot:
    def speak(self):
        print("삐빅")


for x in [Duck(), Robot()]:
    x.speak()

# =========================================================
#  🔥 실습 문제 : 도형 넓이 계산
# =========================================================


# Shape 부모 클래스 작성하기
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0


# Rectangle 자식 클래스 작성하기
class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__("직사각형")
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


# Circle 자식 클래스 작성하기
class Circle(Shape):
    def __init__(self, r):
        super().__init__("원")
        self.r = r

    def area(self):
        return self.r * self.r * 3.14


# Triangle 자식 클래스 작성하기
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("삼각형")
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


# 1️⃣ 부모 클래스 작성
# - 인스턴스 변수: name(도형 이름)
# - 인스턴스 메소드: area() 작성 (return 0 작성)


# 2️⃣ 자식 클래스 작성
# - Rectangle 인스턴스 변수: w(가로), h(세로)
# - Circle 인스턴스 변수: r(반지름)
# - Triangle 인스턴스 변수: base(밑변), height(높이)
# - 인스턴스 메소드: area() 작성


# 3️⃣ 자식 객체 리스트 생성
shapes = [Rectangle(3, 4), Circle(5), Triangle(6, 3)]


# 4️⃣ 도형 넓이 출력 (반복문 사용)
# total = 0
# 사각형 넓이: 12cm
# 원 넓이: 78.5cm
# 삼각형 넓이: 9.0cm

total = 0
for shape in shapes:
    area = shape.area()
    print(f"{shape.name} 넓이: {area}cm^2")
    total += area

print(f"전체 넓이: {total}cm^2")  # 전체 넓이: 99.5cm
