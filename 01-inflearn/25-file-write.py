# 파일 생성, 읽기, 쓰기

# 파일 생성: open(), close()
# 파일 읽기: read(), readline(), seek()
# 파일 쓰기: write(), writeline(), writelines()

# 절대경로
# 파일 주소 전체

# 상대경로
# / 루트 폴더
# ./ 현재 위치
# ../ 현재 위치의 상위 폴더로 이동

# ------------------------------------------------------------

# 1. open 함수 & close 함수
# open(): 파일을 여는 함수
# close(): 파일을 닫는 함수

# open() 함수 정의
# open('파일명', '모드', '인코딩')

# 절대경로
# open('/Users/hyeonah/Documents/Study/Python/resource/news.txt')

# 상대경로
open('./resource/news.txt')

# 파일 열기
news = open('./resource/news.txt', 'r', encoding='UTF-8')
# 속성 확인
print(dir(news))
# 파일 이름
print(news.name)
# 모드 확인
print(news.mode)
# 인코딩 확인
print(news.encoding)
# open() 함수로 연파일을 작업이 끝나면 닫아야한다
news.close()

# ------------------------------------------------------------

# 2. read 함수 & seek 함수
# read(): 파일을 읽어오는 함수
# seek(): 파일의 특정부분을 찾는 함수

# with문을 사용해서 파일 열기
# with문 정의
# with open('인자1', '인자2', '인자3') as 변수명:
#   ...
# with문을 사용하면 close() 함수로 open된 파일을 닫지 않아도 된다(자동으로 닫힘)

with open('./resource/news.txt', 'r', encoding='UTF-8') as news:
  # read() 함수 안에 첫번째 파라미터로 읽어올 용량을 넣어준다
  # 여기서 단위는 byte고 공백 10칸, 영문 기준으로 10글자가 10byte다
  content = news.read(10)
  print(content)
  # file.read()는 마지막으로 읽은곳을 기억하고 있다
  content = news.read(20)
  print(content)
  # 처음으로 파일에 돌아가고싶으면 seek() 함수를 호출한다
  news.seek(0, 0)
  content = news.read(10)
  print(content)

# ------------------------------------------------------------

# 3. readline 함수
# readline(): 파일을 한줄씩 읽어오는 함수
with open('./resource/news.txt', 'r', encoding='UTF-8') as news:
  # 첫번째줄 읽어오기
  line = news.readline()
  print(line)
  # 두번째줄 읽어오기
  line = news.readline()
  print(line)

# ------------------------------------------------------------

# 4. readlines 함수
# readlines(): 파일의 모든 줄을 읽어서 각각의 줄을 리스트로 만들어 리턴하는 함수
with open('./resource/news.txt', 'r', encoding='UTF-8') as news:
  lines = news.readlines()
  print(lines)

# ------------------------------------------------------------

# 5. write 함수
# write(): 해당 파일에 내용을 쓰는 함수
# 덮어씌우기 (모드: write)
with open('./resource/news.txt', 'w') as news:
  news.write('I love python\n')

# 추가하기 (모드: append)
with open('./resource/news.txt', 'a') as news:
  news.write('I love react\n')

# ------------------------------------------------------------

# 6. writelines 함수
# writelines(): 파일에 list 요소를 쓰는 함수
with open('./resource/news.txt', 'w') as news:
  fruits = ['Apple\n', 'Banana\n', 'Melon\n']
  news.writelines(fruits)