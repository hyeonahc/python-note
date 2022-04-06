# True로 취급되는 값
# 0이 아닌 수
x = 1
print(bool(x))
# True

# "문자열"
x = "hello"
print(bool(x))
# True

# 데이터가 담겨있는 리스트 [data...]
x = [1, 2, 3]
print(bool(x))
# True

# 데이터가 담겨있는 튜플 (data...)
x = (1, 2, 3)
print(bool(x))
# True

# 데이터가 담겨있는 딕셔너리 {'key': 'value'}
x = {
  'name': 'pooh'
}
print(bool(x))
# True

# 데이터가 담겨져있는 집합 {data...}
x = {1, 2, 3}
print(bool(x))
# True

# ------------------------------------------------------------

# False로 취급되는 값
# 0
y = 0
print(bool(y))
# False

# 빈문자열: "", str()
y = ""
print(bool(y))
# False

y = str()
print(bool(y))
# False

# 빈리스트: [], list()
y = []
print(bool(y))
# False

y = list()
print(bool(y))
# False

# 빈튜플: () tuple()
y = ()
print(bool(y))
# False

y = tuple()
print(bool(y))
# False

# 빈딕셔너리: {} dict()
y = {}
print(bool(y))
# False

y = dict()
print(bool(y))
# False

# 빈집합: {} set()
y = set()
print(bool(y))
# False

# ------------------------------------------------------------

# if문

# if문이 True일때 하위 구문이 실행된다
if True:
  print('if condition is true, this paragraph will be displayed')

# if문이 False일때 하위 구문이 실행되지 않는다
if False:
  print('if condition is true, this paragraph will be displayed')

# True or False를 대신할 수 있는 데이터
# True로 간주
if 'data': 
  print('if condition is true, this paragraph will be displayed')

# False로 간주
if '':
  print('if condition is true, this paragraph will be displayed')

# ------------------------------------------------------------

# if else문
# if문이 True이면 하위 구문이 실행되고 False면 else의 하위 구문이 실행된다
if True:
  print(1)
else:
  print(2)
# 1

if False:
  print(1)
else:
  print(2)
# 2

# ------------------------------------------------------------

# 다중 조건문
# elif가 여러개 있는 형태

num = 90

if num >= 90:
  print('A')
elif num >= 80:
  print('B')
elif num >= 70:
  print('C')
else:
  print('Failed')

# ------------------------------------------------------------

# 중첩 조건문
# if문 안에 if문이 있는 형태

num = 15

if num >= 0:
  if num == 0:
    print("Zero")
  else:
    print("Positive number")
else:
  print("Negative number")