# 딕셔너리
# 딕셔너리 자료형은 순서가 없다
# 딕셔너리는 수정과 삭제가 가능하다

# ------------------------------------------------------------

# 선언

# 선언하는 3가지 방법
# 1. {}안에 key와 value로 이루어진 데이터를 넣는다
# key와 value의 값은 작은따옴표('')나 큰따옴표("")로 감싸준다
a = {
  'key': 'value'
}

# 2. dict() 함수로 리스트 안에 튜플 형태로 넣는다
a = dict([
  ('key', 'value')
])

# 3. dict() 함수 안에 더 간단히 넣는 방법
a = dict(
  key = 'value'
)

# 한 딕셔너리 안에 key 이름은 중복되어 사용할 수 없다
# 딕셔너리안에 있는 value 값에 접근하기 위해서 key가 필요한데 같은 key를 사용하면 가장 마지막에 선언한 key의 value에만 접근한다
names = {
  'name': 'John',
  'name': 'Paul'
}

print(names['name'])
# Paul
# John은 출력되지 않는다

# key값으로 숫자형 데이터를 사용할 수 있다
a = {
  0: 'value'
}

# 어떤 자료형이든 딕셔너리의 value값으로 사용할 수 있다
a = {
  'list': [1, 2, 3] 
}

# 딕셔너리는 데이터를 관리하기 용이하다
member1 = {
  'name': 'John Lenno',
  'birthday': 'October 9, 1940',
}

# 리스트로 전체데이터를 관리 할 수 있다
# beatles = [member1...]

# ------------------------------------------------------------

# 출력

# 출력하는 2가지 방법

a = {
  'key': 'value'
}

# 1. 속성으로 접근
print(a['key'])

# 2. get() 함수로 접근
print(a.get('key'))

# 속성 vs get()함수로 접근하는 방법의 차이
member1 = {
  'name': 'John Lennon',
  'birthday': 'October 9, 1940',
}

# 딕셔너리에 해당 값이 없을 때 속성으로 접근하면 에러 발생
# print(member1['city'])

# 딕셔너리에 해당 값이 없을 때 get()함수로 접근하면 None 리턴
# 에러를 발생하지 않기때문에 좀더 안정적으로 개발할 수 있다
print(member1.get('city'))
# None 

# ------------------------------------------------------------

# 수정

# 기존에 있던 key를 가져와서 새로운 값을 넣어주면 수정이 일어난다
member1 = {
  'name': 'John Lennon',
  'birthday': 'October 9, 1940',
}
member1['name'] = 'Paul McCartney'

# ------------------------------------------------------------

# 추가

# 기존에 없던 key를 가져와서 값을 넣어주면 딕셔너리에 새로운 값이 추가가 된다
member1 = {
  'name': 'John Lennon',
  'birthday': 'October 9, 1940',
}
member1['city'] = 'Liverpool'

# ------------------------------------------------------------

# 딕셔너리에서 지원하는 여러가지 함수

member2 = {
  'name': 'Paul McCartney',
  'birthday': 'June 18, 1942',
}

# 1. keys()
# key 값만 가져와서 리턴하는 함수
print(member2.keys())
# dict_keys(['name', 'birthday'])

print(list(member2.keys()))
# ['name', 'birthday']
# 받아온 key 값을 리스트 형태로 변환

# 2. values()
# value 값만 가져와서 리턴하는 함수
print(member2.values())
# dict_values(['Paul McCartney', 'June 18, 1942'])

print(list(member2.values()))
# ['Paul McCartney', 'June 18, 1942']
# 받아온 value 값을 리스트 형태로 변환

# 3. items()
# key와 value를 동시에 가져오는 함수
print(member2.items())
# dict_items([('name', 'Paul McCartney'), ('birthday', 'June 18, 1942')])

# dict()함수를 사용해 딕셔너리를 선언할때 사용하는 방법과 같은 형태로 리턴된다
a = dict([
  ('name', 'Paul McCartney'),
  ('birthday', 'June 18, 1942')
])

# 4. pop()
# 딕셔너리에서 해당하는 value 값을 리턴하고 삭제하는 함수
member2 = {
  'name': 'Paul McCartney',
  'birthday': 'June 18, 1942',
}

print(member2.pop('birthday'))
# June 18, 1942

print(member2)
# {'name': 'Paul McCartney'}

# 5. popitem()
# key를 몰라도 사용 가능
# 임의로 아무 값이나 리턴하고 삭제
member2 = {
  'name': 'Paul McCartney',
  'birthday': 'June 18, 1942',
}

print(member2.popitem())
# ('birthday', 'June 18, 1942')

print(member2)
# {'name': 'Paul McCartney'}

# 6. update()
# 딕셔너리 수정 & 추가 해주는 함수
member3 = {
  'name': 'George Harrison',
  'birthday': 'February 25, 1943',
}

# 수정
print(member3.update(birthday='1943-02-25'))

# 추가
print(member3.update(city='Liverpool'))

# 변수로 추가
newData = {'nationality': 'British'}
member3.update(newData)

print(member3)
# {'name': 'George Harrison', 'birthday': '1943-02-25', 'city': 'Liverpool', 'nationality': 'British'}

# ------------------------------------------------------------

# in 메소드
member4 = {
  'name': 'Ringo Starr',
  'birthday': 'July 7, 1940',
}

# 딕셔너리 안에 해당 key 값이 있는지 조회
# 대소문자 구별
print('Name' in member4)
# False
print('name' in member4)
# True