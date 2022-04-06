# input() 함수

# input("질문내용")
# - 사용자에 입력값을 받아와 출력해주는 함수
# - input함수의 첫번째 파라미터는 문자열형태로 사용자에게 물어볼 질문 내용을 적는다
# - input으로 받아온 값은 무조건 문자열이다

# 예제1: input으로 사용자에게 값 받아오기
# 받아온 값은 변수에 할당된다
# firstName = input('enter your first name >>> ')
# lastName = input('enter your last name >>> ')

# input으로 받아온 값 출력
# print(firstName, lastName)

# 예제2: input으로 숫자형 데이터 계산하기
num1 = input('Enter first number >>> ')
num2 = input('Enter second number >>> ')

print(num1, '+', num2, '=', int(num1) + int(num2))