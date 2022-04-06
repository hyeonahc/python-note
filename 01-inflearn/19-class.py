# 19. class 

# 클래스란
# 클래스는 오브젝트를 만들기위한 템플릿이다
# 여기서 클래스를 사용해 만든 오브젝트를 인스턴스라고 한다
# 인스턴스는 클래스에 있는 속성과 함수를 상속받는다
# 클래스에 있는 속성을 프로퍼티, 함수를 메소드라고 한다
# 파이썬에 있는 모든 데이터는 오브젝트이므로 클래스도 오브젝트이다
# 모든 클래스는 오브젝트를 상속받는다
# class Name(object):

# 클래스를 사용하는 이유
# 비슷한 속성과 함수를 가지고 있는 오브젝트를 쉽게 만들기 위해서

# 객체 vs 인스턴스
# a = Name()일때 a는 객체이다 그리고 a 객체는 Name의 인스턴스이다
# 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Name)의 객체인지를 관계 위주로 설명할 때 사용한다
# "a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며 "a는 Name의 객체"보다는 "a는 Name의 인스턴스"라는 표현이 훨씬 잘 어울린다

# 객체 지향 프로그램(OOP: Object Oriented Programming)
# 객체 지향을 사용하는 이유
# 절차지향 프로그램의 단점을 보완, 재사용 극대화 (생산성 향상), 유지보수 용이

# ------------------------------------------------------------

# 클래스와 인스턴스 만들기

# 클래스 선언하기
class Cat:
  # 클래스 변수: 클래스로 직접 접근 가능, 공유하는 속성
  eyes = 2
  nose = 1
  mouse = 1

  # 인스턴스 변수: 객체마다 별도 존재
  def __init__(self, name, color):
    self.name = name
    self.color = color

# 클래스 정보 출력하기
print(Cat)
# <class '__main__.Cat'>

# ------------------------------------------------------------

# 선언한 클래스로 인스턴스 만들기
# 인스턴스: 클래스를 상속해서 만든 새로운 객체
# 인스턴스 만드는법
# 변수 = 클래스이름(클래스에 넘겨줄 값)
cat1 = Cat('Yattong', 'white, dark brown')
cat2 = Cat('Samsaek', 'white, yellow, dark brown')

# Cat이라는 템플릿을 가지고 인스턴스를 만들어 변수에 할당하면 메모리에 올라가고 각각 다른 id값을 가진다
# 인스턴스로 만든 객체는 각기 다른 객체, 안에 있는 내용물이 같아도 각기 다른 인스턴스다
# 즉 cat1과 cat2는 같지 않다
print(id(cat1), id(cat2))
# 4517477440 4517477344
print(id(cat1) == id(cat2))
# False

# ??? 네임 스페이스
# A namespace is a system that has a unique name for each and every object in Python.
print('cat1', cat1.__dict__)
print('cat2', cat2.__dict__)

# ------------------------------------------------------------

# 클래스 속성 확인
# 클래스의 변수는 모든 인스턴스에서 접근할 수 있다. (eyes, nose, mouse)
if cat1.eyes == 2:
  print('{} has {} eyes'.format(cat1.name, cat1.eyes))
# Yattong has 2 eyes

# 인스턴스 속성 확인
# 인스턴스의 속성은 객체마다 별도 존재하며 인스턴스를 선언할때  만들어진다
print("{}'s color is {}".format(cat2.name, cat2.color))
# Samsaek's color is white, yellow, dark brown

# ------------------------------------------------------------

# 클래스 메소드, 인스턴스 메소드 사용하기

# 메소드가 있는 클래스 만들기
class Test:
  # 클래스 메소드
  def func1():
    print('Func1 is called')
  # 인스턴스 메소드
  def func2(self):
    print('Func2 is called')

# 새로운 인스턴스 만들기
t = Test()

# 클래스 메소드 호출하는 방법
# 1) 클래스로 직접 호출한다
Test.func1()
# Func1 is called

# 인스턴스 메소드 호출하는 방법
# 1) 인스턴스로 호출하기
t.func2()
# Func2 is called
# 2) 클래스로 호출할때는 인스턴스를 인수(argument)로 넘겨준다
# Test.func2()
# TypeError: Test.func2() missing 1 required positional argument: 'self'
Test.func2('hi')
# Func2 is called

# dir() 함수
# 해당 오브젝트의 모든 프로퍼티(value값은 제외)와 메소드를 출력하는 함수
# The dir() function returns all properties and methods of the specified object, without the values
print(dir(t))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'func1', 'func2']

# ------------------------------------------------------------

# 클래스 변수, 인스턴스 변수 사용하기

class Ikea:
  # 클래스 변수: 이 클래스를 사용해서 만든 모든 인스턴스가 공유하는 변수
  stockNum = 0

  # 생성자(초기화 메소드): 객체가 처음 생길때 자동으로 가지게 되는 메소드
  def __init__(self, name):
    # 인스턴스 변수
    self.name = name
    Ikea.stockNum += 1

  # 소멸자(del 메소드): 객체가 없어질때 자동으로 호출되는 메소드
  def __del__(self):
    Ikea.stockNum -= 1

# Ikea의 인스턴스 2개 생성
stock1 = Ikea('chair')
stock2 = Ikea('couch')

# Ikea의 인스턴스 이름 출력
print(stock1.name)
# chair

print(stock2.name)
# couch

# 클래스 Ikea의 stockNum 출력
# 클래스 Ikea의 stockNum는 인스턴스가 추가될때마다 1씩 늘어난다
# 위 코드에서 Ikea의 인스턴스를 두번 만들었으므로 stockNum는 2
print(Ikea.stockNum)
# 2
del stock1
# Ikea의 인스턴스를 하나 지웠으므로 stockNum는 1
print(Ikea.stockNum)
# 1

# ------------------------------------------------------------

class Tiger:
  dad = 'Taeho'
  mom = 'gungon'
  home = 'tiger valley'

  def __init__(self, name):
    self.name = name

  def info(self):
    return '{} lives in {}'.format(self.name, Tiger.home)

  def growl(self, sound):
    return '{}: {}'.format(self.name, sound)

tiger1 = Tiger('Woori')
print(tiger1.info())
# Woori lives in tiger valley

tiger2 = Tiger('Nara')
print(tiger2.info())
# Nara lives in tiger valley

print(tiger2.growl('grrr...'))
# Nara: grrr...


