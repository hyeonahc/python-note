# 숫자형 데이터의 종류 
# 숫자형 데이터는 정수, 실수 복소수형이 있다.

# 1. init (정수형)
# 1, 2, 3, 4처럼 소수점이 없는 숫자. 정수에는 양의 정수, 0, 음의 정수가 있다. 즉 -1, 0, 1 모두 정수형이다.
a = 1
print(type(a))
# <class 'int'>

# 2. float (실수형)
# 정수와 달리 소수점이 포함된 숫자 (분수도 가능). 3.14, 1.65등 소수점을 포함한 숫자가 실수형이다.
a = 3.14
print(type(a))
# <class 'float'>
b = 1 / 2
print(type(b))
# <class 'float'>

# 3. complex (복소수형)
# 실수와 허수의 합으로 이루어지는 수. 복소수형은 실수 + 허수j 또는 실수 + 허수J로 쓴다.
a = 1 + 2j
print(type(a))
# <class 'complex'>

# ------------------------------------------------------------

# 숫자형 데이터의 연산자

# 사칙연산자
# + 더하기, - 빼기, * 곱하기, / 나누기
a = 1 + 1
print(a)
# 2
b = 2 - 1
print(b)
# 1
c = 2 * 8
print(c)
# 16
d = 8 / 2
print(d)
# 4.0
# 나눗셈은 정수가 아닌 실수를 반환한다

# // 몫, % 나머지
# 나눗셈을 한 후 몫과 나머지
a = 17 // 8
print(a)
# 2
# 17을 8로 나누면 몫은 2
b = 17 % 8
print(b)
# 1
# 17을 8로 나누면 나머지는 1

# x의  y제곱
# x ** y
a = 2 ** 3
print(a)
# 8
# 2를 3번 곱하면 8이다

# ------------------------------------------------------------

# 번외: 숫자형 데이터에서 유용하게 쓰이는 함수들
# 1. abs(x)
# 절댓값을 리턴하는 함수. 마이너스 값을 무조건 플러스값으로 리턴해준다
a = abs(-3.141592)
print(a)
# 3.141592

# 2. pow(x, y)
# x의 y제곱을 리턴하는 함수. x ** y와 같은 결과를 리턴한다.
a = pow(2, 3)
print(a)
# 8
# 2를 3번 곱한값을 리턴한다

# 3. a, b = divmod(x, y)
# x를 y로 나눈 후 그 몫과 나머지를 변수 a, b에 각각 할당하는 함수.
a, b = divmod(100, 7)
print(a, b)
# 14 2
# 몫이 14고 나머지 첫번째자리 수가 2다

# ------------------------------------------------------------

# 연산자 활용

# 서로 다른 형 계산
# 서로 다른 형을 가진 데이터끼리 연산을하면 형변환이 자동으로 이루어진다. 정수와 실수를 연산하면 실수가 최종값으로 리턴된다.
print(1 + 1.0)
# 2.0
print(2 - 1.0)
# 1.0
print(2 * 2.0)
# 4.0
print(4 / 2.0)
# 2.0
print(1.0 + 1)
# 2.0
print(2.0 - 1)
# 1.0
print(2.0 * 2)
# 4.0
print(4.0 / 2)
# 2.0
print(17.0 // 8)
# 2.0
print(17.0 % 8)
# 1.0
print(2.0 ** 3)
# 8.0

# 실수에서 0 생략
a = 7.
# 7.0
# 0 생략
b = 7
c = .7
# 0.7
# 0 생략

# ------------------------------------------------------------

# 형을 변환하는 함수

# 1. int()
# 소수점 자리를 절삭하고 정수 부분만 리턴하는 함수
a = int(.1)
print(a)
# 0
# 소수점자리 숫자인 1을 절삭하고 정수부분인 0만 리턴한다
b = int(1.1)
print(b)
# 1
# 소수점자리 숫자인 1을 절삭하고 정수부분인 1만 리턴한다

# 2. float()
# 다른 숫자형 데이터를 실수로 만들어 리턴하는 함수. 정수를 실수로 바꿨을때 소수점은 첫째자리까지 나온다.
a = float(1)
print(a)
# 1.0
b = float(20)  
print(b)
# 20.0
c = float(3.14)  
print(c)
# 3.14

# 3. complex()
# 다른 숫자형 데이터를 복소수로 만들어 리턴하는 함수.
a = complex(1)
print(a)
# (1+0j)

# ------------------------------------------------------------

# True와 False의 형변화
# bool의 값인 True와 False는 숫자로 치환했을때 각각 1과 0로 바뀐다

a = int(True)
print(a)
# 1

b = int(False)
print(b)
# 0

# ------------------------------------------------------------

# 외부 모듈 사용
# 간단한 사칙연산 외에 숫자형 데이터를 복잡한 처리과정을 거쳐야할때 외부 모듈 이용

import math
# 외부 모듈을 가져오고 싶을때는 예약어 import 사용

print(math.pi) 
# 3.141592653589793
# pi값 출력

print(math.ceil(5.1)) 
# 6
# 올림