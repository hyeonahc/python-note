# 1. number (숫자형)
# 1) init (정수형)
# 1, 2, 3, 4처럼 소수점이 없는 숫자. 정수에는 양의 정수, 0, 음의 정수가 있다. 즉 -1, 0, 1 모두 정수형이다.
a = 1
print(type(a))
# <class 'int'>

# 2) float (실수형)
# 정수와 달리 소수점이 포함된 숫자 (분수도 가능). 3.14, 1.65등 소수점을 포함한 숫자가 실수형이다.
a = 3.14
print(type(a))
# <class 'float'>

b = 1 / 2
print(type(b))
# <class 'float'>

# 3) complex (복소수형)
# 실수와 허수의 합으로 이루어지는 수. 복소수형은 실수 + 허수j 또는 실수 + 허수J로 쓴다.
a = 1 + 2j
print(type(a))
# <class 'complex'>

# ------------------------------------------------------------

# 2. string (문자열형)
# 문자로 이루어진 집합. 문자열은 ' '(작은 따옴표) " "(큰 따옴표)로 감싼다.

a = 'python'
print(type(a))
# <class 'str'>

# 숫자형 데이터를 ''나 ""로 감싸면 문자열 데이터가 된다
a = '1'
print(type(a))
# <class 'str'>

# ------------------------------------------------------------

# 3. bool (불형)
# True 또는 False의 값을 가지고 있는 데이터형. 값이 참이면 True, 거짓이면 False를 리턴한다. 파이썬에서 True, False는 대문자로 시작한다. 

a = True
print(type(a))
# <class 'bool'>

b = False
print(type(b))
# <class 'bool'>

# 소문자로 시작하는 true 또는 false는 파이썬에서 bool형 데이터가 아닌 변수로 인식한다
# 변수로 인식하기 때문에 true라는 이름의 변수가 정의되지 않았으면 에러메세지를 표시한다
# c = true
# print(type(c))
# NameError: name 'true' is not defined. Did you mean: 'True'?

# ------------------------------------------------------------

# 4. list (리스트형)
# [ ]로 여러개의 데이터가 감싸져있는 형태.

a = ['hi', '1960']
print(type(a))
# <class 'list'>

# ------------------------------------------------------------

# 5. dict (사전형)
# key와 value로 이루어진 여러 프로퍼티가 { }에 감싸져있는 형태

# 여기서 key는 "member1", "member2".. 이고 value는 "John Lennon", "Paul McCartney"이다
beatles = {
  "member1": "John Lennon",
  "member2": "Paul McCartney",
  "member3": "George Harrison",
  "member4": "Ringo Starr",
}
print(type(beatles))
# <class 'dict'>

# ------------------------------------------------------------

# 6. tuple (튜플형)
# () 안에 여러 데이터가 감싸져 있는 형태

a = (1, 2, 3)
print(type(a))
# <class 'tuple'>