# 문자열 생성
# 변수 선언 후 문자형 데이터를 할당한다. 작은 따옴표, 큰 따옴표 모두 사용 가능하고 따옴표를 중첩해서 사용할 수도 있으나 권장하지 않는다.

str1 = 'peaches'
str2 = "strawberry"
str3 = '''fig'''
str4 = """banana"""

print(type(str1), type(str2), type(str3), type(str4))
# <class 'str'> <class 'str'> <class 'str'> <class 'str'>

# ------------------------------------------------------------

# 빈 문자열을 선언하는 2가지 방법

# 1. 내용없이 따옴표만 변수에 할당
empty1 = ''
print(empty1, type(empty1), len(empty1))
#  <class 'str'> 0
# 변수 empty1에 들어 있는 값은 빈문자열이기 때문에 콘솔창에서 보이지 않지만 마우스로 드래그하면 빈문자가 잡힌다

# 2. str() 함수로 빈문자열 생성
empty2 = str()
print(empty2, type(empty2), len(empty2))
#  <class 'str'> 0
# 변수 empty2에 들어 있는 값은 빈문자열이기 때문에 콘솔창에서 보이지 않지만 마우스로 드래그하면 빈문자열이 잡힌다

# ------------------------------------------------------------

# 이스케이프 코드
# 이스케이프 코드란 파이썬에서 값을 출력할때 정렬하기 위해 미리 지정된 코드를 의미한다.

# 1. \
correct_1 = 'Sgt. Pepper\'s Lonely Hearts Club Band'
correct_2 = "She said, \"I want you to win my heart\""

# 2. \t
# 문자열 사이 간격이 tab키 만큼 벌어진다.
print('a\tb')
# a       b
# tab키만큼 두문자가 벌어진다

# 3. \n
# 문자열 사이를 한줄씩 띄워준다.
print('a\nb')
# a
# b

# 4. r
# 일반적으로 백슬래쉬는 파일경로에 많이 사용하는데 이때 r을 사용해 백슬래쉬가( \ )가 문자열로 사용될 수 있도록 한다.
file_path = r'D:\document\study\python'
print(file_path)
# D:\document\study\python

# 5. ''' multiple line '''
# 작은따옴표 세개로 여러줄로 된 문자열을 감싸줄 수 있다.
multi_str1 = '''
In Penny Lane, there is a barber showing photographs
Of every head he's had the pleasure to know
And all the people that come and go
Stop and say hello
'''
# 역슬래쉬가 빈공간을 바인딩해준다
multi_str2 = \
'''
In Penny Lane, there is a barber showing photographs
Of every head he's had the pleasure to know
And all the people that come and go
Stop and say hello
'''
multi_str3 = \
'Here comes the sun '  \
'And I say it\'s all right'
print(multi_str3)
# Here comes the sun And I say it's all right
# 역슬래쉬가 빈공간을 바인딩 해주었기 때문에 한줄이 콘솔창에 프린트된다

# ------------------------------------------------------------

# 문자열 연산

# 문자열끼리 더할때
city1 = "New York"
city2 = "London"
print(city1 + city2)
# New YorkLondon

# 문자열을 곱했을때
city3 = "Paris"
print(city3 * 3)
# ParisParisParis

# ------------------------------------------------------------

# 문자열에 해당 문자가 있는지 확인할때

# 문자가 있는지 확인 (in)
city4 = "Milan"
print('M' in city4) # True
print('m' in city4) # False

# 문자가 없는지 확인 (not in)
city4 = "Milan"
print('A' not in city4) # True
print('a' not in city4) # False

# ------------------------------------------------------------

# 문자열을 다루는 함수

# 1.  len()
# 문자열의 길이를 구하는 함수
city5 = 'Tokyo'
print(len(city5))
# 5

# 2. str()
# 문자형이 아닌 데이터를 문자형을 만드는 함수
num_1 = 1
# 숫자형 데이터 1이 들어 있는 변수 num_1
change_to_str = str(num_1)
# 문자형 데이터로 바꾸는 함수 str()를 사용
print(change_to_str, type(change_to_str))
# 1 <class 'str'>
# 문자형 데이터로 바뀐 1이 출력

print(str(True), type(str(True)))
# True <class 'str'>
# bool 값인 True를 str() 함수로 문자열데이터로 변환시켜줌

print(str(False), type(str(False)))
# False <class 'str'>
# bool 값인 False를 str() 함수로 문자열데이터로 변환시켜줌

# 3. capitalize( )
# 첫글자를 대문자로 만드는 함수
city5 = 'tokyo'
print(city5.caplitalize())
# Tokyo

# 4. endswith('x')
# 문자열의 맨 끝 단어가 x로 끝나는지 확인하는 함수. True 또는 False를 리턴한다.
city5 = 'tokyo'
print(city5.endswith('o'))
# True
# 소문자 o가 해당 문자열 맨 끝에 있는지 확인

print(city5.endswith('O'))
# False
# 대문자 O가 해당 문자열 맨 끝에 있는지 확인

# 5. replace('x', 'y')
# 문자열에 있는 단어 x를 찾아 y로 바꿔준다.
city5 = 'tokyo'
print(city5.replace('kyo', ' me'))
# to me

# 6. sorted()
# 문자열의 단어를 순차적으로 정렬한 후 리스트 형태로 리턴한다.
city5 = 'tokyo'
print(sorted(city5))
# ['k', 'o', 'o', 't', 'y']

# 7. split('x')
# x를 기준으로 문자열을 나눠 리스트 형태로 리턴한다.

cities = 'New York, London, Paris, Milan'
abcd = 'a ! b ! c ! d'

print(cities.split(','))
# ['New York', ' London', ' Paris', ' Milan']

print(abcd.split('!'))
# ['a ', ' b ', ' c ', ' d']

# 8. ord('문자열')
# 해당하는 아스키 코드를 리턴한다.
print(ord('z'))
# 122

# 9. chr('아스키 코드')
# 해당하는 문자를 리턴한다.
print(chr(122))
# z

# ------------------------------------------------------------

# 문자열을 인덱스값으로 접근
# String[x:y:z]
# 문자열을 인덱스 x번부터 (y - 1)까지 z번을 건너뛰어 리턴한다.

str5 = 'Hello Python'

# 인덱스값 0번을 의미한다
print(str5[0])
# H

# 문자열 처음부터 끝까지
print(str5[:])
# Hello Python

# 문자열 처음부터 끝까지
print(str5[:len(str5)])
# Hello Python

# 인덱스 1부터 8까지 3개씩 건너뛰어서 리턴
print(str5[1:9:3])
# eoy

# 인덱스 0번은 첫번째 글자를 가리키고 인덱스 -1번은 맨 마지막 글자를 의미한다
# 인덱스 -1번째 글자부터 끝의 글자까지 리턴
print(str5[-1:])
# n

# 맨 오른쪽이 인덱스 -1이므로 맨 오른쪽부터 6번째 떨어져있는 P부터 끝의 글자까지 리턴
print(str5[-6:])
# Python

# 인덱스 3번째인 글자부터 -4번째인 글자까지 리턴
print(str5[3: -3])
# lo Pyt

# 인덱스 0번째 글자부터 맨끝 글자까지 2씩 건너뛴 글자를 리턴
print(str5[::2])
# HloPto