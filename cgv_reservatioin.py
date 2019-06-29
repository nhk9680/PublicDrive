from selenium import webdriver
from bs4 import BeautifulSoup
import time

ID = ''
PW = ' '
executable_path = 'D:/chromedriver.exe'

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
#options.add_argument('disable-gpu')

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
driver.implicitly_wait(1)

while True:
    driver.get('http://www.cgv.co.kr/ticket/')
    driver.switch_to.frame('ticket_iframe')
    time.sleep(1)
#'movie_idx'"81619"

    #영화제목
    '''
    영화 순위에 따라 제목의 위치가 변경될 수 있음. li[2]의 숫자를 바꿔줘야 함.
    이 숫자는 bs4로 파싱한 후, 영화 제목을 로드하여 몇번째 리스트인지 찾아서 반환해야 함.
    그냥 사람이 코드를 갱신하는게?
    '''
    movie = driver.find_element_by_xpath('//*[@id="movie_list"]/ul/li[2]/a')
    movie.click()
    time.sleep(2)

    #IMAX 선택
    selectBox = driver.find_element_by_xpath('//*[@id="sbmt_imax"]/a')
    selectBox.click()
    time.sleep(1)

    #지역 선택
    location = driver.find_element_by_xpath('//*[@id="theater_area_list"]/ul/li[1]/div/ul/li[2]/a')
    location.click()
    time.sleep(1)

    #날짜 선택
    '''
    날짜도 마찬가지로 하루 지날때마다 위치가 바뀜. li[6]=>li[5] --;
    '''
    date = driver.find_element_by_xpath('//*[@id="date_list"]/ul/div/li[6]/a')
    date.click()
    time.sleep(1)

    #상영관 선택
    theater = driver.find_element_by_xpath('//*[@id="ticket"]/div[2]/div[1]/div[4]/div[2]/div[3]/div[1]/div/ul/li[2]/a')
    theater.click()
    time.sleep(1)

    #좌석선택 버튼
    seatBtn = driver.find_element_by_xpath('//*[@id="tnb_step_btn_right"]')
    seatBtn.click()
    time.sleep(2)

    #로그인
    username = driver.find_element_by_xpath('//*[@id="txtUserId"]')
    password = driver.find_element_by_xpath('//*[@id="txtPassword"]')
    username.send_keys("ID")
    password.send_keys("PW")

    login = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/button')
    login.click()

    time.sleep(5)

    # 좌석선택 빨강버튼
    seatBtn = driver.find_element_by_xpath('//*[@id="tnb_step_btn_right"]')
    seatBtn.click()
    time.sleep(2)

    #관람등급안내
    notice = driver.find_element_by_xpath('/html/body/div[4]/div[3]/a[1]')
    notice.click()
    time.sleep(1)

    #인원선택
    numOfPeople = driver.find_element_by_xpath('//*[@id="nop_group_adult"]/ul/li[2]/a')
    numOfPeople.click()
    '''
    A열
    
    좌블
    //*[@id="seats_list"]/div[1]/div[1]/div[2]/div/div[1]/a
    //*[@id="seats_list"]/div[1]/div[1]/div[2]/div/div[2]/a
    
    ...
    
    중블(a열은 파여있는 구조라 3~5)
    //*[@id="seats_list"]/div[1]/div[1]/div[3]/div/div[1]/a
    //*[@id="seats_list"]/div[1]/div[1]/div[3]/div/div[2]/a
    
    
    //*[@id="seats_list"]/div[1]/div[1]/div[5]/div/div[5]/a
    ...
    우블
    //*[@id="seats_list"]/div[1]/div[1]/div[6]/div/div[1]/a
    
    ---
    B열
    
    좌블
    //*[@id="seats_list"]/div[1]/div[2]/div[2]/div/div[1]/a
    //*[@id="seats_list"]/div[1]/div[2]/div[2]/div/div[2]/a
    
    중블
    //*[@id="seats_list"]/div[1]/div[2]/div[3]/div[1]/div[1]/a
    //*[@id="seats_list"]/div[1]/div[2]/div[3]/div[2]/div[1]/a
    //*[@id="seats_list"]/div[1]/div[2]/div[3]/div[2]/div[3]/a
    //*[@id="seats_list"]/div[1]/div[2]/div[3]/div[3]/div[3]/a
    //*[@id="seats_list"]/div[1]/div[2]/div[3]/div[3]/div[4]/a
    우블
    //*[@id="seats_list"]/div[1]/div[2]/div[4]/div/div[1]/a
    
    ---
    '''
    #뭐 이런식으로 긁어서 돌려야할듯?
    seats=driver.find_elements_by_class_name('seat')
    

    while True:
        for seat in seats:
            try:
                seat.click()
                time.sleep(1)

                '''
                예상 오류
                1. 예매완료 좌석(뺏김)
                    ->  1) 확인 버튼을 누르고
                        2) 방금 선택한 좌석을 다시 클릭해서 해제한 후
                        3) 1초 로딩 기다리고
                        4) 다음 좌석 선택 시도로 넘어가기  
                    
                
                2. 선택불가, 예매 완료된 회색 좌석
                    클릭해서 아무 반응이 없는 상태로 다음 버튼을 누를 때
                     <관람인원과 선택 좌석 수가 동일하지 않습니다> 발생
                    
                    ->  1) 확인 버튼을 누르고
                        2) 다음 좌석 선택 시도로 넘어가기
                    
                     
                '''

            except:
                continue

        # 결제선택 빨강버튼
        seatBtn = driver.find_element_by_xpath('//*[@id="tnb_step_btn_right"]')
        seatBtn.click()
        time.sleep(2)
'''
    #자리 나면 알림용 파싱
    while True:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        seats=soup.select('#seats_list')
        print(seats)

        time.sleep(1)
'''

    break

#driver.close()
