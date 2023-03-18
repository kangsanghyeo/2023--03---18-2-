import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://comic.naver.com/webtoon/detail?titleId=648419&no=1' # 원하는 링크 입력 
site = requests.get(url, headers=headers) # 내용 가져오기
source1_data = site.text # 인터넷 소스코드를 source1_data변수에 저장

count1 = source1_data.count('" aria-current="') # 웹툰 제목 개수 가져오기

for i in range(count1): # 해당 개수만큼 반복   
      pos1 = source1_data.find('<div class="flicking-camera episode_list">')+ len('<div class="flicking-camera episode_list">') # <a href=" 만 쓰게된다면 그위에 다른 내용까지 나오기때문에 그위의 내용을 제외하고 가져올수있게하기위해서
      source1_data = source1_data[pos1:] # 해당 위치로 이동

      pos2 = source1_data.find('<a href="')+ len('<a href="') # 링크 앞부분을 지정하기위해 링크 바로앞부분 
      source1_data = source1_data[pos2:] # 해당 위치로 이동  

      pos3 = source1_data.find('" aria-current="') # 가져오는걸 끝내기 위해서 뒷부분 저장
      a_data = source1_data[: pos3] # 앞부분 부터 뒷부분까지 내용 추출 해서 저장
      
      pos4 = source1_data.find('<p class="title">')+ len('<p class="title">') # 제목 앞부분을 지정하기위한 제목 바로 앞부분
      source1_data = source1_data[pos4:] # 해당 위치로 이동

      pos5 = source1_data.find('</p>') # 가져오는걸 끝내기 위해서 뒷부분 저장
      b_data = source1_data[: pos5].strip() # 앞부분 부터 뒷부분 까지 내용 추출 해서 저장

      source1_data = source1_data[pos5+1:] # pos5까지 끝낸 이후 그다음 내용을 가져올때도 반복하기위해 +1을 붙여 다음 위치로 이동한다
      print(i+1, a_data, b_data) # 화면에 출력

      url = 'https://comic.naver.com/webtoon/detail?titleId=648419&no=1' # 링크 입력
      site = requests.get(url, headers=headers) # 내용 가져오기
      source2_data = site.text # 인터넷 소스 코드를 source2_data변수에 저장

      count2 = source2_data.count(' alt="comic content') # 개수 가져오기

      for i in range(count2): # 해당 개수만큼반복

            pos6 = source2_data.find('background:#FFFFFF">')+ len('background:#FFFFFF">') # 이미지 링크 앞부분 위치 지정하기위한 바로 앞부분
            source2_data = source2_data[pos6:] # 해당 위치로 이동

            pos7 = source2_data.find('<img src="')+ len('<img src="') # 이미지 링크 앞부분 위치 지정
            source2_data = source2_data[pos7:] # 해당 위치로 이동

            pos8 = source2_data.find('"') # 이미지 링크 뒷부분 위치 지정
            c_data = source2_data[: pos8] # 앞부분 부터 뒷부분 까지 내용 추출 해서 저장 
                  
            source2_data = source2_data[pos8+1:] # 다음 내용을 찾기위해 뒤부분을 이동시키기
            print(i+1, c_data) # 화면에 출력
            try:
                  file_name = './webtoon/{0}{1}{2}.{3}'.format('뷰티풀 군바리', 예고편, i+1, c_data[-3:]) # webtoon 파일에 파일 이름 저장하기
                  ss = requests.get(c_data, headers=headers) # 서버로 부터 응답을받은 내용을 ss 변수에 저장
                  file = open(file_name, 'wb') # 지정된 이름의 파일을 wb을 열어 파일 객체 생성
                  file.write(ss.content) # 변수에 저장 된 데이터를 파일에 쓰기
                  file.close() # 파일을 닫기
            except Exception as e: #  try 변수에 예외가 발생하면 
                  print('에러발생 : ', e) # 에러발생 을 화면에 출력
                  
