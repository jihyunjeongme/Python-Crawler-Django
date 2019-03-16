# websaver/parser.py
import requests
from bs4 import BeautifulSoup
import json
import os


## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django

django.setup()

# Blogdata를 import 해옵니다.
from parsed_date.models import BlogData


# Python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}


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


# with open(os.path.join(BASE_DIR, "result.json"), "w+") as json_file:
#     json.dump(data, json_file)

## 이 명령어는 이 파일이 import가 아닌 python에서 직접 실행할 경우에만 아래 코드가 동작하도록 합니다.
if __name__ == "__main__":
    blog_data_dict = parse_blog()
    print(blog_data_dict)
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()
