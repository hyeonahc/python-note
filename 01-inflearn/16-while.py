# while문

# 기본 문법

# while True
#   실행문

# while False
#   실행문

# while이 True면 실행하고 False면 실행하지 않는다

# 무한 반복

# 예제 1
# n = 5
# while n > 0:
#   print(n)
# n값이 항상 0이상이므로 실행문이 무한반복된다

# 예제 2
# a = ['Alpha', 'Gamma', 'Delta']
# while a:
#   print(a)
# a값이 항상 True이므로 실행문이 무한반복된다

# ------------------------------------------------------------

# break문
# break를 만나면 while문을 종료한다

n = 5
while n > 0:
  n -= 1
  if n == 2:
    break
  print(n)
print('Loop Ended')

# 4
# 3
# Loop Ended

# ------------------------------------------------------------

# continue문
# continue를 만나면 while문 처음으로 돌아간다

n = 5
while n > 0:
  n -= 1
  if n == 2:
    continue
  print(n)
print('Loop Ended')

# 4
# 3
# 1
# 0
# Loop Ended

# ------------------------------------------------------------

# while문과 if문이 함께 쓰일때
i = 1
while i <= 10:
  print(i)
  if i == 6:
    break
  i += 1
# 1
# 2
# 3
# 4
# 5
# 6

# ------------------------------------------------------------

# while else문

# break가 있을때
n = 5
while n > 0:
  n -= 1
  print(n)
  if n == 2:
    break
else:
  print('else out')
# 4
# 3
# 2

# break가 없을때
n = 5
while n > 0:
  n -= 1
  print(n)
else:
  print('else out')
# 4
# 3
# 2
# 1
# 0
# else out

# ------------------------------------------------------------

a = ['Alpha', 'Gamma', 'Delta']

while True:
  if not a:
    break
  print(a.pop())
# Delta
# Gamma
# Alpha