# 함수 선언
# def functionName(par):
#   <execute code>

# 함수 실행
# functionName(arg);

# ------------------------------------------------------------

# 예제1: 함수에 파라미터가 있을때

# 함수 선언
def funcBasic(name):
  print('Hello', name)

# funcBasic()이라는 함수에 전달해줄 값 설정
python = 'Python'

# 함수 실행
funcBasic(python)
# Hello Python

# 잘못된 함수 실행 (에러 발생)
# funcBasic()
# funcBasic()함수는 파라미터를 가지는 함수이기 때문에 반드시 전달해줄 값과 함께 실행되어야 한다

# ------------------------------------------------------------

# 예제 2: 함수에 return이 있을때

# 함수 선언
def funcReturn(name):
  value = 'Hello ' + name
  return value

# 함수 실행후 변수안에 리턴된 값을 받기
i = funcReturn('Django')
print(i)
# Hello Django

# ------------------------------------------------------------

# 예제3: 다중반환하는 함수를 다중변수로 받을때

def funcMul(x):
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return y1, y2, y3

# funcMul()함수에서 3개의 값이 리턴되기 때문에 리턴값을 받는 변수도 3개여야 한다
a, b, c = funcMul(10)
print(a, b, c)
# 100 200 300

# ------------------------------------------------------------

# 예제4: 다중반환하는 함수를 변수 하나로 받을때

def funcMul(x):
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return y1, y2, y3

# 반환하는 값이 여러개인 함수를 변수로 하나로 받을 경우에는 tuple형태로 들어간다
result = funcMul(10)
print(result, type(result))
# (100, 200, 300) <class 'tuple'>

# 튜플로 받아온 값을 다른 데이터 형태로 바꿔줄수도 있다
print(list(result), type(list(result)))
# [100, 200, 300] <class 'list'>

# ------------------------------------------------------------

# 예제5: 리턴문에 다른형이 있는 경우에는 해당 데이터형이 리턴된다

# 리스트로 리턴
def funcMul(x):
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return [y1, y2, y3]

result = funcMul(10)
print(result, type(result))
# [100, 200, 300] <class 'list'>

# 딕셔너리로 리턴
def funcMul(x):
  y1 = x * 10
  y2 = x * 20
  y3 = x * 30
  return {'v1': y1, 'v2': y2, 'v3': y3}

result = funcMul(10)
print(result, type(result))
# {'v1': 100, 'v2': 200, 'v3': 300} <class 'dict'>

# 다양한 딕셔너리 함수를 사용해서 값을 출력
print(result.get('v1'), result.items(), result.keys())
# 100 dict_items([('v1', 100), ('v2', 200), ('v3', 300)]) dict_keys(['v1', 'v2', 'v3'])

# ------------------------------------------------------------

# 예제6: 함수안에 함수가 있는 중첩함수

def nestedFunc(num):
  def funcInFunc(num):
    print(num + 100)
  funcInFunc(num)

nestedFunc(100)
# 200

# funcInFunc(100)
# NameError: name 'funcInFunc' is not defined
# 내부에 있는 함수는 밖에 있는 함수가 호출되어야만 메모리에 올라가기 때문에 밖에서 호출할 수 없다

# ------------------------------------------------------------

# enumerate()함수로 for 루프 돌리기

# enurmate() 함수
# for index, value in enumerate(iterable data):
#   <execute code>
# 1) 반복할 수 있는 데이터를 enumerate()함수 안에 파라미터로 넣는다
# 2) index, value값을 차례대로 가져온다 
# 3) 코드를 실행한다

# unpacking: 묶여있는 데이터를 푸는 과정
# args: 함수에서 여러 인자를 받을 때 사용
def funcArgs(args):
  for i, v in enumerate(args):
    print('Result: {}'.format(i), v)

funcArgs('Amy')
# Result: 0 A
# Result: 1 m
# Result: 2 y

# 코드해석
# 1) Amy라는 문자열을 넣고 funcArgs함수를 실행한다
# 2) funcArgs함수는 파라미터를 받고 enumerate함수에게 넘겨준다
# 3) enumerate함수는 받아온 파라미터 값을 분해해서 index, value값을 차례대로 가져와 변수 i에는 index값을, v에는 value값을 할당한다
# 4) 받아온 데이터를 print함수로 출력한다
# => Amy라는 묶여있는 데이터를 푸는 unpakcing 과정

print('--------------------')

# packing: 여러 데이터를 묶는 과정
# *args: 함수에서 여러인자를 튜플 형태로 묶어 받아올때 사용
def funcArgs(*args):
  for i, v in enumerate(args):
    print('Result: {}'.format(i), v)

funcArgs('Amy')
# Result: 0 Amy

funcArgs('Amy', 'dean')
# Result: 0 Amy
# Result: 1 dean

# 코드해석
# 1) Amy와 dean이라는 문자열을 넣고 funcArgs함수를 실행한다
# 2) 이때 funcArgs함수는 파라미터값으로 *가 포함된 args를 받는데 이 의미는 튜플로 여러 데이터를 받아 묶어준다는 의미다
# 3) funcArgs함수는 파라미터를 받고 enumerate함수에게 넘겨준다
# 4) enumerate함수는 받아온 파라미터 값을 분해해서 index, value값을 차례대로 가져와 변수 i에는 index값을, v에는 value값을 할당한다
# 5) 가져온 데이터는 ('Amy', 'Dean')이라는 튜플형태이므로 index 0번에는 'Amy'라는 값이 있고 index 1번에는 'Dean'이라는 값이 있다
# 6) 받아온 데이터를 print 함수로 출력한다
# => Amy, Dean이라는 두 문자열을 하나의 튜플데이터로 묶는 packing 과정

print('--------------------')

# 딕셔너리 형태 언팩킹
# **kwargs: 함수에서 key와 value값의 인자를 딕셔너리 형태로 묶어 받아올때 사용
def funcKwargs(**kwargs):
  for v in kwargs.keys():
    print('{}'.format(v), kwargs[v])

funcKwargs(name='Amy')
# name Amy

# 딕셔너리 안에 있는 key의 이름은 같으면 안된다
funcKwargs(name1='Amy', name2='Dean')
# name1 Amy
# name2 Dean

# 코드해석
# 1) Amy와 Dean이라는 문자열을 넣고 funcKwargs함수를 실행한다
# 2) 이때 funcArgs함수는 파라미터값으로 **kwargs를 받는데 이 의미는 딕셔너리 형태로 여러 데이터를 받아 묶어준다는 의미다
# 3) 변수 kwargs안에는 딕셔너리형태로 묶어준 데이터가 있다
# 4) keys()함수를 실행해 딕셔너리의 key값만 가져오고 그 값을 변수 v에 넣어준다
# 5) 받아온 데이터를 print 함수로 출력한다
# 6) kwargs[v]는 key값을 사용해 딕셔너리안에 있는 value를 가져오는 코드다

print('--------------------')

# arg, *args, **kwargs 혼합예제
def mixed(arg1, arg2, *args, **kwargs):
  print(arg1, arg2, args, kwargs)

mixed('alpha', 'beta', 'gamma', 'delta', 'epsilon', num1=1, num2=2, num3=3)
# alpha beta ('gamma', 'delta', 'epsilon') {'num1': 1, 'num2': 2, 'num3': 3}

# ------------------------------------------------------------

# 람다함수 

# lambda 매개변수 : 표현식
# 람다함수는 긴 함수를 한줄로 정리해주고 바로 실행해주는 즉시 실행함수이며 이름이 없는 익명함수다

# 일반함수 vs 람다함수

# 일반함수 선언
def funcBasic(x, y):
  return x * y

# 일반함수 출력
funcBasic(1, 2)

# 일반함수를 변수에 할당한 후 priint함수로 리턴값 출력
result = funcBasic(1, 2)
print(result)

# 람다함수 선언
lambda x, y: x * y

# 람다함수 호출
# 1. 변수에 담아서 호출
result = lambda x, y: x * y
print(result(1, 2))

# 2. 함수의 인자로 넘길 수 있음
def func(x, y, func):
  print(x * y * func(10, 10))

func(10, 20, lambda x, y: x * y)