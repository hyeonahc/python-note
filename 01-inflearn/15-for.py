# for문

# 기본문법
# for 변수 in <collection>
#   <loop body>

# <collection>: 연속적으로 나열된 iterable(반복할 수 있는) 데이터 형태
# 문자열 "", 리스트 [], 튜플 (), 딕셔너리 {}
# <collection>의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 <loop body>를 실행한다

# 문자열
stringType = "hello"
for s in stringType:
  print(s)
# h
# e
# l
# l
# o
print()

# 리스트
listType = ['Pooh', 1921, ['Parsley', 'Mint', 'Rosemary']]
for l in listType:
  print(l)
# Pooh
# 1921
# ['Parsley', 'Mint', 'Rosemary']
print()

# 튜플
tupleType = ('dogs', 'cats', 'penguins', 'tigers')
for t in tupleType:
  print(t)
# dogs
# cats
# penguins
# tigers
print()

# 딕셔너리
dictionaryType = {
  'name': 'Pooh',
  'birthday': 'August 21, 1921',
  'color': 'yellow'
}
for d in dictionaryType:
  print(d)
# name
# birthday
# color
print()

for d in dictionaryType:
  print(dictionaryType[d])
# Pooh
# August 21, 1921
# yellow
print()

for d in dictionaryType:
  print(dictionaryType.get(d))
# Pooh
# August 21, 1921
# yellow

# ------------------------------------------------------------

# range()
# range()함수는 연속된 숫자를 리턴한다

# for 변수 in range(x):
#   실행문
# 변수에 0부터 x-1까지의 정수가 들어간다

for v in range(5):
  print(v)
# 0
# 1
# 2
# 3
# 4
print()

# for 변수 in range(start, stop):
#   실행문
# 변수에 start부터 stop-1까지 정수값이 들어간다

for v in range(5, 10):
  print(v)
# 5
# 6
# 7
# 8
# 9
print()

# for 변수 in range(start, stop, step):
#   실행문
# 변수에 start부터 stop-1까지 step만큼 건너뛴 정수값이 들어간다

for v in range(0, 10, 2):
  print(v)
# 0
# 2
# 4
# 6
# 8
print()

# ------------------------------------------------------------

# 1부터 10까지의 합 구하는 방법 1
x = 0
for y in range(1, 11):
  x += y
print(x)
# 55

# y에는 1부터 10까지의 값이 담겨있음
# 변수 x에 y의 값을 누적시켜 모두 더해준다
# 1부터 10까지의 합이 변수 x에 할당된다

# 1부터 10까지의 합 구하는 방법 2
print(sum(range(1, 11)))
# 55

# range(1, 11)은 숫자 1부터 10까지를 의미한다
# sum()은 모든 값을 더해주는 함수이므로
# 숫자 1부터 10까지를 모두 더해 프린트해준다

# sum(iterable, start)
# 모든 값을 더하는 함수
# iterable: 숫자형데이터가 들어있는 list, tuple, dictionary
# start: 리턴된 값에서 추가적으로 더할 데이터

# ------------------------------------------------------------

# if문과 for문의 혼용

# isupper()
# 문자열이 대문자인지 확인하는 함수
# True, False 리턴

# upper()
# 문자열에 있는 단어를 대문자로 바꿔주는 함수

city = 'weLCoM tO SeoUL'

for c in city:
  if c.isupper():
    print(c)
  else:
    print(c.upper())
# W
# E
# L
# C
# O
# M
#
# T
# O
# 
# S
# E
# O
# U
# L

# 변수 c에는 문자열 'weLCoM tO SeoUL'가 한문자씩 들어있다
# c에 들어있는 문자열중에 대문자가 있으면 pint함수로 출력하고
# 대문자가 아니라면 upper() 함수로 대문자로 바꾸고 print함수로 출력한다
# 결과적으로 문자열에 있는 모든 문자는 대문자로 순서대로 한문자씩 출력된다

# ------------------------------------------------------------

# break문
# for문을 강제종료시키는 키워드
numbers = [ 8, 56, 49, 32, 7, 22, 12, 98, 465 ]

for num in numbers:
  if num == 32:
    print('Found', num)
    break
  else:
    print('Not Found', num)
# Not Found 8
# Not Found 56
# Not Found 49
# Found 32

# 변수 num에는 리스트 numbers 안에 있는 모든 값을 차례대로 가져온다
# num의 값이 32일 경우에만 print() 함수로 Found와 현재 num의 값을 출력하고 반복문을 종료시킨다
# num의 값이 32가 아니면 print() 함수로 Not Found와 현재 num의 값을 출력하고 반복문을 계속 실행시킨다

# ------------------------------------------------------------

# continue문
# 조건에 맞는 값을 건너뛰고 for문 처음으로 돌아가는 키워드
container = ['1', 3.14, 'Tiglet', False, complex(7)]

for c in container:
  if type(c) is bool:
    continue
  print(c, type(c))
# 1 <class 'str'>
# 3.14 <class 'float'>
# Tiglet <class 'str'>
# (7+0j) <class 'complex'>

# 변수 c에는 리스트 container안에 있는 모든 값을 차례대로 가져온다
# 변수 c에 담긴 값이 True 또는 False 값을 가진 bool타입이면 continue를 실행한다
# continue를 실행하면 for문 처음으로 돌아가 반복문을 계속 실행시킨다

# ------------------------------------------------------------

# 구구단 출력
for i in range(2, 10):
  for j in range(1, 10):
    print('{:4d}'.format(i * j), end='')
  print()
#   2   4   6   8  10  12  14  16  18
#   3   6   9  12  15  18  21  24  27
#   4   8  12  16  20  24  28  32  36
#   5  10  15  20  25  30  35  40  45
#   6  12  18  24  30  36  42  48  54
#   7  14  21  28  35  42  49  56  63
#   8  16  24  32  40  48  56  64  72
#   9  18  27  36  45  54  63  72  8

# ------------------------------------------------------------

# reversed() 함수
# sequence 형태의 데이터를 거꾸로 만들어 리턴하는 함수

city = 'Seoul'

print(reversed(city))
# <reversed object at 0x109c74760>

print(list(reversed(city)))
# ['l', 'u', 'o', 'e', 'S']

print(tuple(reversed(city)))
# ('l', 'u', 'o', 'e', 'S')

print(set(reversed(city))) 
# {'l', 'o', 'S', 'u', 'e'}
# 집합은 순서가 없다