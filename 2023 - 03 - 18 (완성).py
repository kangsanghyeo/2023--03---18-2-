import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}


url = 'https://comic.naver.com/webtoon/detail?titleId=648419&no={0}'.format
site = requests.get(url, headers=headers)
source1_data = site.text

count1 = source1_data.count('" aria-current="')

for i in range(count1):
            
      pos1 = source1_data.find('<div class="flicking-camera episode_list">')+ len('<div class="flicking-camera episode_list">')
      source1_data = source1_data[pos1:]

      pos2 = source1_data.find('<a href="')+ len('<a href="')
      source1_data = source1_data[pos2:]

      pos3 = source1_data.find('" aria-current="')
      a_data = source1_data[: pos3].strip()
      
      pos4 = source1_data.find('<p class="title">')+ len('<p class="title">')
      source1_data = source1_data[pos4:]

      pos5 = source1_data.find('</p>')
      b_data = source1_data[: pos5].strip()

      source1_data = source1_data[pos5+1:]
      print(i+1, a_data, b_data)

      url = 'https://comic.naver.com/webtoon/detail?titleId=648419&no=11'
      site = requests.get(url, headers=headers)
      source2_data = site.text

      count2 = source2_data.count(' alt="comic content')

      for i in range(count2):

            pos6 = source2_data.find('background:#FFFFFF">')+ len('background:#FFFFFF">')
            source2_data = source2_data[pos6:]

            pos7 = source2_data.find('<img src="')+ len('<img src="')
            source2_data = source2_data[pos7:]

            pos8 = source2_data.find('"')
            c_data = source2_data[: pos8]
                  
            source2_data = source2_data[pos8+1:]
            print(i+1, c_data)
            try:
                  file_name = './webtoon/{0}{1}{2}.{3}'.format('뷰티풀 군바리', '10화_유격 ', i+1, c_data[-3:])
                  ss = requests.get(c_data, headers=headers)
                  file = open(file_name, 'wb')
                  file.write(ss.content)
                  file.close()
            except Exception as e:
                  print('에러발생 : ', e)
                  
