from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()# 크롬 웹드라이버
driver.get("https://www,google.co.kr/imghp?hl=ko&tab=wi&ogbl") # 구글 이미지검색
elem = driver.find_element_by_name("q") #검색창
elem.send_keys("뷔") # 검색
elem.send_keys(Keys.RETURN) # 엔터

SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")# 스크롤 높이 저장

while True :
  
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") # 스크롤 내리기
  time.sleep(SCROLL_PAUSE_TIME)# 로딩까지 기다리기
  new_height = driver.execute_script("return document.body.scrollHeight")# 변화한 스크롤 높이 저장
  
  if new_height == last_height :# 스크롤 길이가 같다면 ==> 스크롤이 다 내려간것
    try :
      driver.find_element_by_css_selector(".mye4qd").click() # 결과 더보기 클릭
    except: # 오류가 난다면
      break # 반복문종료 
      
  last_height = new_height
  
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #작은이미지를 변수에 저장
count = 1

for image in images : 
  try :
    image.click()# 작은이미지를 선택
    time.sleep(2) # 로딩까지 기다리기
    imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")# 큰이미지의 주소를 저장
    #                                  _xpath() <-xpath로 정확하게 선택가능. class 선택시 광범위로 인한 오류를 해결할 수 있다.
    urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")# 이미지를 저장
    count = count +1 # 숫자를 늘려가며 이미지 이름을 1.2.3.. .jpg로 저장하기위함.
  exceot :
    pass
  
driver.close() # 브라우저 닫기
