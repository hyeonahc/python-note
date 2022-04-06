# 선언
# 1. {}안에 원소 넣어 선언
a = {1, 2, 3}
print(a, type(a))
# {1, 2, 3} <class 'set'>

# 2. 함수 set()으로 선언
a = set({1, 2, 3})
print(a, type(a))
# {1, 2, 3} <class 'set'>

a = set([1, 2, 3])
print(a, type(a))
# {1, 2, 3} <class 'set'>

# 딕셔너리 vs 집합
# 딕셔너리는 key와 value가 한쌍인 값들의 집합으로 이루어진 데이터 형태
dataDict = {
  'key': 'value'
}

# 집합은 key 없이 value로만 이루어진 데이터 형태
dataSet = {'value1', 'value2', 'value3'}

# 집합에서는 서로 다른 자료형을 저장할 수 있다
a = {1, 2, 3, 'Alpha', 'Gamma', 'Delta'}

# 집합에서는 데어터가 중복될 수 없다
a = {1, 2, 3, 3, 3}
print(a)
# {1, 2, 3}

# ------------------------------------------------------------

# 형변환
b = set([1, 2, 3])
print(b)
# {1, 2, 3}

# 1. 집합 -> 튜플
dataTuple = tuple(b)

print(dataTuple)
# (1, 2, 3)

# 튜플형 응용
print(dataTuple[0])
# 1

print(dataTuple[1:3])
# (2, 3)

# 2. 집합 -> 리스트
dataList = list(b)

print(dataList)
# [1, 2, 3]

print(dataList[0])
# 1

print(dataList[1:3])
# [2, 3]

# ------------------------------------------------------------

# 집합 자료형 활용 (교집합, 합집합, 차집합)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
# 기호 &
print(s1 & s2)
# {4, 5, 6}

# 함수 intersection()
print(s1.intersection(s2))
# {4, 5, 6}

# 합집합
# 기호 |
print(s1 | s2)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 함수 union()
print(s1.union(s2))
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합 
# 기호 -
print(s1 - s2)
# {1, 2, 3}

# 함수 difference()
print(s1.difference(s2))
# {1, 2, 3}

# ------------------------------------------------------------

# 집합에서 자주 쓰이는 함수
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = set([1, 2, 3])

# 1. len()
# 집합안에 있는 원소의 개수를 리턴하는 함수
print(len(s1))
# 6

# 2. isdisjoint()
# 집합에 중복 원소가 없는지 확인하는 함수
# True: 교집합되는 원소가 없을때
# False: 교집합되는 원소가 있을때
print(s1.isdisjoint(s2))
# False

# 3. issubset()
# 부분 집합인지 확인하는 함수
print(s2.issubset(s1))
# False
print(s3.issubset(s1))
# True

# 4. issuperset()
# 상위 집합인지 확인하는 함수
print(s1.issuperset(s2))
# False
print(s1.issuperset(s3))
# True

# 5. add()
# 데이터를 집합에 추가하는 함수
s1.add('new data')
print(s1)
# {1, 2, 3, 4, 5, 6, 'new data'}

# 6. remove()
# 데이터를 집합에서 삭제하는 함수
s1 = set([1, 2, 3, 4, 5, 6])
s1.remove(6)
print(s1)
# {1, 2, 3, 4, 5}

# 7. discard()
# 데이터를 집합에서 삭제하는 함수
s1 = set([1, 2, 3, 4, 5, 6])
s1.remove(6)
print(s1)
# {1, 2, 3, 4, 5}

# 8. clear()
# 집합에서 모든 데이터를 삭제하는 함수
s1 = set([1, 2, 3, 4, 5, 6])
s1.clear()
print(s1)
# set()
