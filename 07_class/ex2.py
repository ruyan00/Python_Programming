# 2. 상속 (Inheritance)

# ===========================================================
#  1. 상속이란?
#  - ( 부모 클래스 )의 속성과 메소드를 ( 자식 클래스 )가 물려받는 것
#
#  - 부모 클래스 = 상위 클래스 = 슈퍼 클래스 = 기반 클래스
#  - 자식 클래스 = 하위 클래스 = 서브 클래스 = 파생 클래스
#
#  - 관계 표현: ( is-a 관계 )
#    예) 강아지는 동물이다 (Dog is-a Animal)
#        학생은 사람이다 (Student is-a Person)
# ===========================================================


# ===========================================================
#  2. 상속이 필요한 이유
# ===========================================================


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}이(가) 밥을 먹습니다.")

    def bark(self):
        print(f"{self.name} 멍멍")


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}이(가) 밥을 먹습니다.")

    def meow(self):
        print(f"{self.name} 야옹")


# 위 코드의 문제점은?
# - ( 중복 코드 ) -> 유지 보수가 어려워짐
# - 공통 부분은 부모 클래스에 한 번만 작성하고, 자식들이 물려받자!

# ===========================================================
#  상속의 장점
#  - ( 코드 재사용 ) : 공통 코드를 부모에 한 번만 작성
#  - ( 유지보수 편리 ) : 부모만 고치면 모든 자식에 반영됨
#  - ( 확장성 ) : 새로운 자식 클래스를 쉽게 추가할 수 있음
# ===========================================================


# ===========================================================
#  3. 상속 구현하기
#  - 형식) class 자식클래스(부모클래스):
#  - 공통 부분을 Animal 부모 클래스로 분리
# ===========================================================


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}이(가) 밥을 먹습니다.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} 멍멍")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} 야옹")


# 부모의 속성/메소드를 그대로 물려받음
# 자식만의 새로운 속성/메소드 추가 가능
d = Dog("멍멍이", 5)  # Animal.__init__() 호출
print(d.name, d.age)
d.eat()
d.bark()

c = Cat("야옹이", 3)
print(c.name, c.age)
c.eat()
c.meow()

# 어떤 클래스의 객체인지 확인하기
print(isinstance(d, Dog))
print(isinstance(c, Cat))
print(isinstance(d, Animal))
print(isinstance(d, Cat))

# 상속 관계 확인하기
print(issubclass(Dog, Animal))
print(issubclass(Dog, Cat))

# 부모 클래스 확인
print(Dog.__bases__)
print(Animal.__bases__)

# 모든 클래스는 최상위 부모인 ( object ) 클래스를 자동으로 상속받는다.
print(object.__bases__)

# ===========================================================
#  4. super()
#  - super(): 부모 클래스의 ( 메소드 )를 호출할 수 있게 해주는 함수 -> super().메소드명()
#  - 자식 클래스에서 생성자를 만들면 부모의 생성자를 자동으로 실행하지 않는다.
#  - 부모의 생성자를 실행하려면 super().__init__()을 직접 호출해야 한다. -> self 넘기지 않음
# ===========================================================


# 자식 클래스의 생성자에서 부모 클래스의 생성자를 호출하지 않을 경우
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} ({self.breed}): 멍멍")


d = Dog("멍멍이", 5, "스피츠")
print(d.name, d.age, d.breed)

d.eat()
d.bark()

# ===========================================================
#  5. 메소드 오버라이딩 (Method Overriding)
#  - 부모 클래스에 있는 메소드를 자식 클래스에서 ( 같은 이름 )으로 ( 재정의 )하는 것
#  - ( 상속 ) 관계에서만 발생하고, 메소드 ( 이름 )이 동일해야 한다.
#  - 오버라이딩된 메소드는 부모 메소드가 아닌 ( 자식 메소드 )가 실행된다.
# ===========================================================


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}: ...")


class Dog(Animal):
    def speak(self):  # 메소드 오버라이딩
        print(f"{self.name}: 멍멍")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: 야옹")


class Fish(Animal):
    pass


Dog("멍멍이").speak()
Cat("야옹이").speak()
Fish("니모").speak()

# 자식 클래스에서 부모 클래스의 메소드를 오버라이딩 시
# 부모 클래스의 기능이 필요한 경우 super().메소드명()으로 호출


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"이름: {self.name}, 나이: {self.age}")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show_info(self):
        super().show_info()
        print(f"품종: {self.breed}")


Dog("멍멍이", 5, "푸들").show_info()


# 메소드 탐색 순서 : 객체 자신의 클래스 → 부모 클래스 → 그 위 부모 → ... → object
print(Dog.mro())  # Method Resolution Order

# =========================================================
#  🔥 실습 문제
# =========================================================


# SchoolMember 부모 클래스 작성하기
class SchoolMember:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show_info(self):
        print(f"이름: {self.name}, 전화번호: {self.phone}")


# Student 자식 클래스 작성하기
class Student(SchoolMember):
    def __init__(self, name, phone, grade):
        super().__init__(name, phone)
        self.grade = grade

    def show_info(self):
        print(f"학년: {self.grade}학년")

    def learn(self, teacher):
        print(f"{self.name}가 {teacher.name}에게 {teacher.subject} 과목을 배웁니다.")


# Teacher 자식 클래스 작성하기
class Teacher(SchoolMember):
    def __init__(self, name, phone, subject):
        super().__init__(name, phone)
        self.subject = subject

    def show_info(self):
        print(f"과목: {self.subject}")

    def teach(self, student):
        print(f"{self.name}이 {student.name}에게 {self.subject} 과목을 가르칩니다.")


# 1️⃣ 부모 클래스 인스턴스 변수: name(이름), phone(연락처) -> 생성자 구현


# 2️⃣ 자식 클래스 인스턴스 변수 -> 생성자 구현
# - Student 클래스: grade(학년)
# - Teacher 클래스: subject(과목)


# 3️⃣ 자식 객체 생성: 생성자 호출

s = Student("뽀로로", "111-1111", 1)
t = Teacher("크롱선생님", "222-2222", "파이썬")


# 4️⃣ 인스턴스 및 상속 관계 확인

print(isinstance(s, SchoolMember))  # True
print(isinstance(t, SchoolMember))  # True
print(isinstance(s, Student))  # True
print(isinstance(t, Teacher))  # True

print(issubclass(Student, SchoolMember))  # True
print(issubclass(Teacher, SchoolMember))  # True
print(issubclass(Student, Teacher))  # False


# 5️⃣ 인스턴스 메소드 구현
# - SchoolMember 클래스: show_info() 메소드 구현
# - Student, Teacher 클래스: show_info() 메소드 오버라이딩

s.show_info()  # 이름: 뽀로로, 전화번호: 111-1111
# 학년: 1학년
t.show_info()  # 이름: 크롱선생님, 전화번호: 222-2222
# 과목: 파이썬


# 6️⃣ Student 클래스: learn() 메소드 구현
s.learn(t)  # 뽀로로가 크롱선생님에게 파이썬 과목을 배웁니다.


# 7️⃣ Teacher 클래스: teach() 메소드 구현
t.teach(s)  # 크롱선생님이 뽀로로에게 파이썬 과목을 가르칩니다.
