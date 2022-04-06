# 문자열을 형식화하는 두가지 방법
# 1. % 기호를 사용한 방식
# 2. format() 함수를 사용한 방식

# ------------------------------------------------------------

# % 기호를 사용한 방식
# % 기호를 사용하면 문자열이 길어지면서 가독성이 나빠지므로 문자열을 형식화 할때는 format 함수 사용을 권장한다

# 기본 문법
# print('%d %s %f' % (digit, string, float))
# digit: 정수 i.e) 1
# string: 문자열 i.e) 'hello'
# float: 실수 i.e) 3.14

print('%d %s %f' % (1, 'hello', 3.14))
# 1 hello 3.140000
# 실수는 소수점 자리가 6개로 출력되는것이 디폴트이다

print('%s %s' % ('one', 'two'))
# one two
# %s가 두개이므로 문자열 두개를 출력한다

# ------------------------------------------------------------

# % 기호를 사용해 포맷팅하기
# 공백 만들기, 글자를 넣을 공간 한정하기 (절삭하기), 소수점자리 제한

# 공백 만들기
# 왼쪽부터 공백만들기
print('%5s' % ('123'))
#   123
# 왼쪽부터 5칸의 공간을 확보, 2칸의 공백, 3칸의 value값을 놓는 곳

# 오른쪽부터 공백만들기
print('%-5s' % ('123'))
# 123  
# 오른쪽부터 5칸의 공간을 확보, 2칸의 공백, 3칸의 value값을 놓는 곳

# 글자를 넣을 공간 한정하기 (절삭하기)
print('%.5s' % ('My Name is Python'))
# My Na
# 총 5개의 빈공간을 확보 후 value 값을 넣어주었다
# 빈공간이 5칸밖에 없으므로 6칸째부터 해당하는 me is Python은 삭제한 후 출력한다

# 소수점자리 제한
print('%6.2f'%(3.14159265359))
#   3.14
# 빈공간 6개, 소수점자리 2개

print('%06.2f'%(3.14159265359))
# 003.14
# 정수 빈부분 0 넣기, 빈공간 6개, 소수점자리 2개