# print 함수
# 메세지를 화면에 출력시키는 함수. 싱글 쿼트 또는 더블 쿼트로 메세지 내용을 감싼다.

# 싱글 쿼트
print('single quote')

# 더블 쿼트
print("double quote")

# 싱글쿼트나 더블쿼트를 연속적으로 사용할수도 있다
print('''Here are three single quotes''')
print("""Here are three double quotes""")

# 내용물이 없는 print함수는 줄바꿈을 한다
print()

# ------------------------------------------------------------

# print 함수의 파라미터

# separator 옵션
# print 함수를 원하는 형식으로 출력을 할때 print에 있는 파리미터 사이에 결합문자를 넣는다
print('p', 'y', 't', 'h', 'o', 'n')
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('p', 'y', 't', 'h', 'o', 'n', sep=',')
print('p', 'y', 't', 'h', 'o', 'n', sep='|')
print('010', '0000', '0000', sep='-')
print('hello', 'gmail.com', sep='@')

# end 옵션
# print문은 자동으로 줄바꿈을 해준다 만약 줄바꿈 없이 이어서 쓰고 싶다면 end 옵션을 사용한다
print('Welcome to')
print('My Blog')
print()
print('Welcome to ', end='')
print('My Blog')

# file 옵션
# import: 예약어, 변수명으로 사용할 수 없다
# import sys
# print('', file='sys.stdout')