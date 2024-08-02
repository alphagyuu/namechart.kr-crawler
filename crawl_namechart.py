from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# 크롬 드라이버 경로 설정
chrome_driver_path = '\path_to_chrome_driver'

# Selenium WebDriver 설정
def create_driver():
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# 메인 함수
def main(save_directory):
    driver = create_driver()
    base_url = 'https://www.namechart.kr/chart/all?gender=t&page='
    names = []

    try:
        for page in range(1, 1277):  # 1페이지부터 1276페이지까지
            driver.get(base_url + str(page))
            time.sleep(3)  # 페이지 로딩 시간을 기다림

            # 페이지 소스 가져오기
            html = driver.page_source

            # BeautifulSoup으로 HTML 파싱
            soup = BeautifulSoup(html, 'html.parser')

            # 테이블에서 데이터 추출
            tables = soup.find_all('table')
            for i, table in enumerate(tables):
                rows = table.find_all('tr')
                if i == 0:  # 첫 번째 테이블은 헤더가 있음
                    for row in rows[1:]:  # 첫 번째 행은 헤더이므로 제외
                        cols = row.find_all('td')
                        if len(cols) > 1:  # 이름 열이 있는지 확인
                            name = cols[1].text.strip()  # 두 번째 열에 이름이 있음
                            names.append(name)
                else:  # 두 번째 테이블은 헤더가 없음
                    for row in rows:  # 모든 행을 포함
                        cols = row.find_all('td')
                        if len(cols) > 1:  # 이름 열이 있는지 확인
                            name = cols[1].text.strip()  # 두 번째 열에 이름이 있음
                            names.append(name)
            print(f"{page} 페이지 완료")

    except Exception as e:
        print("에러 발생:", e)
    
    finally:
        # 드라이버 닫기
        driver.quit()

    # 데이터프레임으로 변환
    df = pd.DataFrame(names, columns=['Name'])
    print(df)

    # 디렉토리가 없으면 생성
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # CSV 파일로 저장
    save_path = os.path.join(save_directory, 'filename.csv')
    df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"CSV 파일이 성공적으로 {save_path}에 저장되었습니다.")

if __name__ == "__main__":
    # 저장할 디렉토리를 인자로 받음
    save_directory = '\save_dir'  # 원하는 디렉토리 경로로 변경
    main(save_directory)
