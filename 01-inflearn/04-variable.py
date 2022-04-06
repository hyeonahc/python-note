# 변수란?
# 변수는 데이터를 저장하는 공간이다. 변수 안에 들어있는 데이터는 변경할 수 있다.

# 변수 선언하기
n = 100
# 변수 n에 정수 100을 할당한다
# 오른쪽에 있는 데이터를 왼쪽에 있는 변수에 할당한다

# 변수값 활용하기
print(n * 2)
# 200
# 정수 데이터 100이 들어있는 변수 n에 숫자 2를 곱한값을 출력한다

# ------------------------------------------------------------

# 변수 이름을 지을때 규칙
# 가능한 변수 이름
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 불가능한 변수 이름
# 1. 특수문자, 숫자로 시작하는 변수
# 숫자로 시작하는 변수
# 1age = 1

# 특수기호로 시작하는 변수
# %age = 2

# 2. 예약어(이미 파이썬에서 예약되어 쓰고 있는 이름)
# for = 3
# as = 4

# ------------------------------------------------------------

# 변수 동시 선언
# 여러 변수를 동시에 선언할 수 있다
x = y = z = 200
# 변수 x, y, z에 정수 200을 할당한다

print(x)
print(y)
print(z)
# 모두 정수 200을 출력한다

# ------------------------------------------------------------

# 변수값 재선언
# 변수안에 데이터를 할당한후 수정할 수 있다

# 변수 선언
value = 300
# 변수값 재선언
value = 'Change Value'
# 출력
print(value)
# Change Value

# ------------------------------------------------------------

# type() 함수
# type 함수는 데이터의 자료형을 알려준다

n = 100
print(type(n))
# <class 'int'>
# 변수 n에는 100이 할당되어있다
# 100은 정수(integer)이므로 <class 'int'>가 출력된다

# ------------------------------------------------------------

# id() 함수
# 아이디는 오브젝트의 메모리 주소
# 파이썬에 있는 모든 데이터는 아이디 값(메모리 주소)을 가지고 있는 객체이다
# 아이디는 오브젝트의 메모리 주소이기 때문에 프로그램을 실행할때마다 다른 아이디값이 나온다
# id()함수는 오브젝트의 아이디값을 리턴한다

# 다른 변수에 같은 값이 할당이 되었을때 같은 오브젝트를 참조 (같은 주소값을 가리킨다)
# 파이썬 엔진에서 id값은 효율성을 위해 하나만 만들어진다
a = 100
b = 100
print(id(a) == id(b))
# True

# ------------------------------------------------------------

# 객체 참조(Object Reference)
# 파이썬은 객체 지향 언어이다
# 파이썬에 있는 모든 데이터는 객체다
# 문자열, 정수, 함수도 파이썬에서는 객체이다
# 모든 오브젝트는 클래스에 속한다

print(400)
# 400이라는 정수값을 출력하려고 할때 일어나는 일
# 파이썬 엔진이 내부적으로 400이라는 정수를 만드는 함수 init()을 통해서 값을 생성하고 콘솔에 출력한다
# 즉 print(400)은 print(init(400))과 같다
# 파이썬에 있는 모든 데이터는 객체이므로. 출력하려는 정수 400도 객체다. 이 정수 객체를 만들기 위해 init()이라는 함수가 실행되었다

k = 1
j = k
print(k, j)
# 1 1

k = 2
print(k, j)
# 2 1

j = 3
print(k, j)
# 2 3

# 위의 예제에서 변수 k에 정수 1을 할당했다
# 파이썬에 있는 모든 데이터는 객체이므로 변수 k는 1을 가지고 있는 메모리에 직접 접근하는 것이 아니라 주소에 접근을 한다

