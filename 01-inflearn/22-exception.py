#  22. exception

# 파이썬 에러 종류
# 1. Syntax Error: 파이썬 문법을 지키지 않았을때 발생하는 에러
# 2. Name Error: 참조할 이름이 없을때 발생하는 에러
# 3. ZerioDivisionError: 어떤수를 0으로 나누려고할때 발생하는 에러
# 4. Index Error: 인덱스의 범위를 초과했을때 발생하는 에러
# 5. Key Error: 딕셔너리형 데이터 안에 있는 key에서 발생하는 에러
# 6. AttributeError: 어떤 모듈에 존재하지 않는 속성을 사용할때 발생하는 에러 
# 7. ValueError: 참조하려는 값이 존재하지 않을때 발생하는 에러
# 8. FileNotFoundError: 해당하는 파일을 찾지 못했을때 발생하는 에러
# 9. TypeError: 자료형에 맞지 않는 연산을 수행하는 경우 발생하는 에러

# 1. SyntaxError: 파이썬 문법을 지키지 않았을때 발생하는 에러
# print('this is syntax error)
# SyntaxError: unterminated string literal (detected at line X)

# if True
#   pass
# SyntaxError: expected ':'

# 2. NameError: 참조할 이름이 없을때 발생하는 에러
a = 1
b = 2
print(c)
# NameError: name 'c' is not defined

# 3. ZeroDivisionError: 어떤수를 0으로 나누려고할때 발생하는 에러
# print(100 / 0)
# ZeroDivisionError: division by zero

# 4. IndexError: 인덱스의 범위를 초과했을때 발생하는 에러
x = ['hello', 0, 'python', False, (1, 2, 3)]
print(x[5])
# IndexError: list index out of range

# y = [1, 2, 3]
# print(y.pop())
# print(y.pop())
# print(y.pop())
# print(y.pop())
# IndexError: pop from empty list

# 5. keyError: 딕셔너리 데이터에 없는 key를 요청했을때 발생하는 에러
dict = { 'Name': 'Olivia', 'Born': '2003', 'City': 'California' }
# print(dict['birthday'])
# KeyError: 'birthday'
# print(dict.get('birthday'))
# None

# 딕셔너리의 value값을 key로 가져오는 2가지 방법
# 1) 키 이름으로 직접 접근
# 딕셔너리['키이름']
# 2) get 메소드 사용 
# 딕셔너리.get('키이름')
# key로 데이터를 가져올때는 get 메소드를 사용하는게 더 안전하다

# 6. AttributeError: 어떤 모듈에 존재하지 않는 속성을 사용할때 발생하는 에러 
# import time
# print(time.time())
# 1643634191.539969
# print(time.whattimeisit())
# AttributeError: module 'time' has no attribute 'whattimeisit'

# 7. ValueError: 참조하려는 값이 존재하지 않을때 발생하는 에러
# numbers = [1, 31, 3, 27]
# numbers.remove(1203)
# ValueError: list.remove(x): x not in list

# 8. FileNotFoundError: 해당하는 파일을 찾지 못했을때 발생하는 에러
# f = open('test.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# 9. TypeError: 자료형에 맞지 않는 연산을 수행하는 경우 발생하는 에러
# x = [1, 2] # 가변형
# y = (1, 2) # 불변형
# print(x + y)
# TypeError: can only concatenate list (not "tuple") to list

# ------------------------------------------------------------

# 예외란?
# 파이썬에서 에러메세지를 무시하고 싶을때 try, except 구문을 사용해서 오류를 예외적으로 처리하는것 

# 예외 처리 기본 구조
# try문이 실행되는 중에 오류가 발생하면 except문이 실행된다
# try문이 실행되는 중에 오류가 발생하지 않으면 except문이 실행되지 않는다
# try:
#   ...
# except:
#   ...

# 예제 
names = ['Emma', 'Isabella', 'Mia']

# case 1: try 구문 실행
# try문이 실행되는 중에 오류가 발생하지 않으면 except문이 실행되지 않는다.
try:
  name = 'Emma'
  result = names.index(name)
  print('{} is in the list. Index Number: {}'.format(name, result))
except:
  print('Something went wrong')
# Emma is in the list. Index Number: 0

# case 2: except 구문 실행
# try문이 실행되는 중에 오류가 발생하면 except문이 실행된다.
try:
  name = 'Camila'
  result = names.index(name)
  print('{} is in the list. Index Number: {}'.format(name, result))
except:
  print('Something went wrong')
# Something went wrong

# case 3: except 구문에 에러종류를 명시하고 실행하기
# except 키워드 다음에 어떤 에러 종류인지 명시하면 상응하는 에러가 발생할때만 except구문이 실행된다.
# 에러 종류를 명시하지 않으면 종류에 상관없이 에러가 발생하면 except 구문이 실행된다.
try:
  name = 'Camila'
  result = names.index(name)
  print('{} is in the list. Index Number: {}'.format(name, result))
except ValueError:
  print('Something went wrong')
# Something went wrong

# case 4: else
# try문 수행중 오류가 발생하면 except 구문이 수행되고 오류가 없으면 try구문과 else 구문이 수행된다
try:
  name = 'Emma'
  result = names.index(name)
  print('{} is in the list. Index Number: {}'.format(name, result))
except ValueError:
  print('Something went wrong')
else:
  print('else statement is executed when try code runs succesfully')
# Emma is in the list. Index Number: 0
# else statement is executed when try code runs succesfully

# case 5: finally
# finally 구문은 예외처리에 실행여부에 관계 없이 마지막에 반드시 실행되어야 하는 구문이다 
try:
  name = 'Emma'
  result = names.index(name)
  print('{} is in the list. Index Number: {}'.format(name, result))
except ValueError:
  print('Something went wrong')
else:
  print('else clause is executed when try clause runs succesfully')
finally:
  print('finally clause is always executed in the end')
# Emma is in the list. Index Number: 0
# else clause is executed when try clause runs succesfully
# finally clause is always executed in the end

# case 6: raise
# raise로 에러 강제로 발생시킨다.
try:
  name = 'Liam'
  if name == 'Noah':
    print('You are successfully logged in')
  else:
    raise ValueError
except ValueError: 
  print('You are failed to login')
else:
  print('else statement is executed when try code runs succesfully')
# You are failed to login
