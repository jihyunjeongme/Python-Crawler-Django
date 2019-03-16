<h1 align="center">
  <br>
  <a href="https://stophyun.tistory.com/category"><img src="https://user-images.githubusercontent.com/43984584/54471897-bfb62d80-4803-11e9-9975-076c567e5ca9.png" alt="Markdownify" width=""></a>
  <br>
  
  <br>
</h1>

<h1 align="center"> Django를 이용하여 Tistory 블로그 제목과 URL 가져오기
</p>

# Overview

- 대상: 파이썬 기본 지식, HTML 초급 정도의 지식, Django 기초룰 가지고 있는 분에게 권장합니다.
- 목표
  - Tistory 블로그에서 제목과 URL을 가져옵니다.
    - https://stophyun.tistory.com/category

## Tistory 블로그

<img src="https://user-images.githubusercontent.com/43984584/54471904-d066a380-4803-11e9-9a69-68712d24da98.png">

- BeautifulSoup를 이용하여 CSS검색을 통해 제목과 URL을 가져옵니다.

```bash
def parse_blog():
    req = requests.get("https://stophyun.tistory.com/category", headers=headers)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    blog_title = soup.select("div.col-md-9 > div > ul > li > a")

    data = {}

    for title in blog_title:
        print(title.get("href"))
        data[title.text] = title.get("href")
    return data
```

## 결과

#### 1. Django를 정상적으로 설치하고 `python manage.py runserver` 명령어를 입력한 뒤 `http://localhost:8000/`로 이동하면 아래와 같은 화면이 뜹니다. 정상적으로 설치되었습니다.

<img src="https://user-images.githubusercontent.com/43984584/54471959-892ce280-4804-11e9-81f8-ef7ba9f1ccb3.png">

#### 2. `http://localhost:8000/admin` 으로 이동한 뒤 admin으로 login 합니다.

<img src="https://user-images.githubusercontent.com/43984584/54471965-9649d180-4804-11e9-9ec8-e642d955ea60.png">

#### 3. `Blog datas`를 클릭합니다.

<img src="https://user-images.githubusercontent.com/43984584/54471967-9e097600-4804-11e9-939d-07b3193577db.png">

#### 4. 블로그 게시글 제목들이 정상적으로 저장된 것을 확인 할 수 있습니다.

<img src="https://user-images.githubusercontent.com/43984584/54471897-bfb62d80-4803-11e9-9975-076c567e5ca9.png">

<img src="https://user-images.githubusercontent.com/43984584/54472019-3869b980-4805-11e9-83f7-a6fed50efb37.png">

## 참고

- [Django로 크롤링한 데이터 저장하기](https://beomi.github.io/gb-crawling/posts/2017-03-01-HowToMakeWebCrawler-Save-with-Django.html)

## 기타 문의

- 블로그 : https://stophyun.tistory.com/
- 이메일: stophyuni@gmail.com
- 궁금한 사항은 이메일로 부담없이 보내주세요.
