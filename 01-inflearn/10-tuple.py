# 튜플
# 리스트와 유사한 특징을 가진 파이썬의 데이터 형식
# 튜플 자료형은 수정과 삭제가 불가하다
# 변경하고 싶지 않은 데이터를 튜플 자료형으로 사용한다

# ------------------------------------------------------------

# 튜플 선언

# 1. 소괄호로 묶는다
a = ()

# 2. 괄호가 없어도 여러 데이터가 있으면 튜플로 간주한다 (소괄호를 쓰는것이 권장된다)
a = 1, 2, 3

# 원소가 하나일때는 컴마로 끝나야 튜플로 인식한다
a = (1)
print(type(a))
# <class 'int'>

a = (1, )
print(type(a))
# <class 'tuple'>

# 두개 이상일때부터 튜플로 인식한다
a = (1, 2)
print(type(a))
# <class 'tuple'>

# 괄호가 없고 데이터가 하나만있을때 컴마와 함께 쓰면 튜플로 인식한다
a = 1,
print(type(a))
# <class 'tuple'>

# 중첩 튜플
# 튜플 안에 튜플 선언 가능
b = (1, 2, 3, 'alpha', 'gamma', 'delta')
c = (1, 2, 3, ('alpha', 'gamma', 'delta'))

# ------------------------------------------------------------

# 수정이 안되는 튜플

b = (1, 2, 3, 'alpha', 'gamma', 'delta')
# b[0] = 'new data'
# print(b)
# 'tuple' object does not support item assignment

# ------------------------------------------------------------

# 인덱싱

b = (1, 2, 3, 'alpha', 'gamma', 'delta')
c = (1, 2, 3, ('alpha', 'gamma', 'delta'))

print(b[0] + b[1] + b[2])
# 6
print(b[-1])
# delta
print(c[-1])
# ('alpha', 'gamma', 'delta')
print(c[-1][2])
# delta
print(list(c[-1][2]))
#  ['d', 'e', 'l', 't', 'a']

# ------------------------------------------------------------

# 슬라이싱

c = (1, 2, 3, ('alpha', 'gamma', 'delta'))

print(c[0:3])
# (1, 2, 3)
print(c[2:])
# (3, ('alpha', 'gamma', 'delta'))

# ------------------------------------------------------------

# 튜플의 연산
# 튜플의 원소값을 변경할 수는 없지만 사용할 수는 있다

b = (1, 2, 3, 'alpha', 'gamma', 'delta')
c = (1, 2, 3, ('alpha', 'gamma', 'delta'))

print(b + c)
print(c * 2)

# ------------------------------------------------------------

# 튜플에서 쓰이는 함수

# 1. index()
# 해당 데이터의 인덱스값을 리턴
x = (54, 21, 123, 87, 21, 3, 65, 35)
print(x.index(35))
# 7

# 2. count()
# 튜플 안에 있는 데이터의 개수를 리턴
x = (54, 21, 123, 87, 21, 3, 65, 35)
print(x.count(21))
# 2

# ------------------------------------------------------------

# 팩킹 언팩킹

# 팩킹
# 일반적인 튜플 선언을 팩킹이라고 한다
animals = ('dogs', 'cats', 'penguins', 'tigers')

# 언팩킹
# 튜플로 묶여있는 데이터를 풀어서 원소를 변수에 할당하는 것
(a1, a2, a3, a4) = animals
print(a1, a2, a3, a4)
# dogs cats penguins tigers
print(type(a1), type(a2), type(a3), type(a4))
# <class 'str'> <class 'str'> <class 'str'> <class 'str'>

# 괄호 없어도 작동하지만 관례상 써준다
a1, a2, a3, a4 = animals