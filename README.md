#namechart.kr-crawler
[NameChart.kr](https://www.namechart.kr/)에서 한국인 이름 데이터를 크롤링하는 Python 코드입니다.


## 📌 기능
- Selenium과 BeautifulSoup을 활용하여 웹 페이지에서 데이터를 수집합니다.
- 1페이지부터 1276페이지까지 모든 이름 데이터를 크롤링합니다.
- 크롤링한 데이터를 CSV 파일로 저장합니다.


## 🛠️ 설치 및 실행 방법

### 1️⃣ 필수 패키지 설치
이 프로젝트를 실행하려면 아래의 Python 패키지가 필요합니다.
```bash
pip install selenium beautifulsoup4 pandas
```

### 2️⃣ 크롬 드라이버 다운로드
Selenium을 사용하려면 최신 ChromeDriver가 필요합니다. [ChromeDriver 다운로드](https://sites.google.com/chromium.org/driver/) 후 `crawler.py`에서 경로를 수정하세요.
```python
chrome_driver_path = '\path_to_chrome_driver'  # 크롬 드라이버 경로 수정
```

## ⚠️ 주의사항
- namechart.py 의 robots.txt를 확인하세요.(배포 시점 기준 크롤링 허용됨)
- `time.sleep(3)`을 환경에 맞게 조절하세요.
- 데이터 저장 경로를 `save_directory` 변수에서 원하는 경로로 설정하세요.
