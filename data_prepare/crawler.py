import json
import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def crawl_yanolja_reviews(name, url):
    review_list = []
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(3)

    scroll_count = 20
    for i in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div')
    review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf')

    for i in range(len(review_containers)):
        review_text = review_containers[i].find('p', class_='content-text').text
        review_stars = review_containers[i].select('path[fill="currentColor"]')
        star_cnt = sum(1 for star in review_stars if not star.has_attr('fill-rule'))
        date = review_date[i].text

        review_dict = {
            'review': review_text,
            'stars': star_cnt,
            'date': date
        }

        review_list.append(review_dict)

    with open(f'./res/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(review_list, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # name, url = sys.argv[1], sys.argv[2]
    holels = [{
    "name" : "강릉경포 호텔 마레",
    "file_name" : "1.gangneung_mare",
    "url" : "https://nol.yanolja.com/reviews/domestic/10046839?sort=HOST_CHOICE"},
    {
    "name": "인사동 나인트리",
    "file_name": "2.insadong_ninetree",
    "url": "https://nol.yanolja.com/reviews/domestic/1000102261?sort=HOST_CHOICE"
    },
    {
    "name": "강릉 더홍씨호텔",
    "file_name": "3.kyongpo_the_hongc",
    "url": "https://nol.yanolja.com/reviews/domestic/3013655?sort=HOST_CHOICE"
    },
    {
    "name": "홍천 비발디파크",
    "file_name": "4.hongcheon_vivaldi",
    "url": "https://nol.yanolja.com/reviews/domestic/3001803?sort=HOST_CHOICE"
    }]
    for hotel in holels:
        file_name = hotel['file_name']
        url = hotel['url']
        print(f'Start crawling {file_name} reviews...')
        crawl_yanolja_reviews(name=file_name, url=url)