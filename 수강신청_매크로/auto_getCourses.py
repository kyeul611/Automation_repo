'''
수강신청 실패를 만회하기 위한 수강신청 매크로 

1. 종합정보시스템으로 수강신청 사이트 접근
2. 계정 정보를 입력
3. 

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


id = '201814102'
pw = 'asas8989!!'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 이게 뭐였지?
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe", options=options)

with open('information.txt', 'r') as f:
    id = f.readline.replace('\n', '')
    pw = f.readline

# 1. 종합정보시스템 로그인 페이지 이동
# driver.get("https://portal.skhu.ac.kr/html/main/index.html?portalPage=portal_main") 

# # 2. 로그인 정보 넣기.
# login_id = driver.find_element(By.ID, 'id')
# login_pw = driver.find_element(By.ID, 'pw')
# login_bt = driver.find_element(By.ID, 'btnLogin')
# login_id.send_keys(id)
# login_pw.send_keys(pw)
# login_bt.click()

# time.sleep(5)

# # 3. 종합정보 시스템 접속
# driver.get("http://tis.skhu.ac.kr")
# time.sleep(3)

# 4. 수강신청시스템 접속
# into_bt = driver.find_element(By.ID, 'mainframe.HFrameSet00.LeftFrame.form.div_left_wrap2.form.menulist_wrap.form.menu_dep02_wrap_1.form.menu_dep03_wrap_1.form.menu_dep04_wrap_2.form.menu_dep04_4:icontext')
# into_bt.click()
driver.get('https://sugang.skhu.ac.kr/')

# 5. 수강신청사이트 로그인
# 수강신청사이트는 iframe 속에 있기 때문에 iframe 전환을 우선 진행해야 함.
driver.switch_to.frame('Main')

login_id = driver.find_element(By.ID, 'txtUserID')
login_pw = driver.find_element(By.ID, 'txtPwd')
login_bt = driver.find_element(By.ID, 'btn-login')

login_id.send_keys(id)
login_pw.send_keys(pw)
login_bt.click()

# 6. 수강신청 탭 클릭
driver.get('https://sugang.skhu.ac.kr/')
driver.switch_to.frame('Main')
# courses_bt = driver.find_element(By.XPATH, '/html/body/header/div/div[2]/ul/li[1]/div/ul/li[1]')
# courses_bt.send_keys('\n')

driver.execute_script("fnMenuLoad('/core/coreNotice1')")
print(driver.page_source)
print("\n\n\n\n ================")
driver.switch_to.default_content()
print(driver.page_source)

time.sleep(2)

# # 7. 수강신청 시작 버튼 클릭
driver.switch_to.frame("Main")
print("\n\n\n\n ================")
# driver.switch_to.default_content()
# print(driver.page_source)
# start_bt = driver.find_element(By.XPATH, '//*[@id="s-contents"]/div/div[2]/button')

# start_bt.click()

time.sleep(2)