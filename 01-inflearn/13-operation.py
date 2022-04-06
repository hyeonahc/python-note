# 산술 연산자 (+, -, *, /)

# + 더하기
# - 빼기
# * 곱하기
# / 나누기

# ------------------------------------------------------------

# 비교 연산자 (>, >=, <, <=, ==, !=)

# A > B: A가 B보다 크다
# A >= B: A가 B보다 크거나 같다
# A < B: B가 A보다 크다
# A <= B: B가 A보다 크거나 같다
# A == B: A와 B는 같다
# A != B: A와 B는 다르다

# ------------------------------------------------------------

# 논리 연산자 (and, or, not)

# A and B: A와 B 모두 만족해야 True
print(True and True)
# True
print(True and False)
# False
print(False and False)
# False

# A and B: A와 B 모두 만족해야 True
print(True or True)
# True
print(True or False)
# True
print(False or False)
# False

# not A: A가 True면 False, A가 False면 True (역으로 연산)
print(not True)
# False
print(not False)
# True

# ------------------------------------------------------------

# 연산자 우선순위
# 1. 산술 연산자 (+, -, *, /)
# 2. 비교 연산자 (>, >=, <, <=, ==, !=)
# 3. 논리 연산자 (and, or, not)

print(20 + 20 > 11 and not 19 + 96 == 10)
# True
