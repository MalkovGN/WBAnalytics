import requests
import random
import time
import pywhatkit
from bs4 import BeautifulSoup as Soup


LOGIN = '9cocbg'
PASSWORD = 'QJN879'

LOGIN_CANADA = 'g9p4Qt'
PASSWORD_CANADA = 'mDPk87'

LOGIN_USA = 'kVNGb0'
PASSWORD_USA = '1Xmss5'

LOGIN_RUSSIA_SHRD = 'nr2GNL'
PASSWORD_RUSSIA_SHRD = 'Y5qSRJ'

proxy_russia = {
    'https': f'http://{LOGIN}:{PASSWORD}@195.216.132.9:8000'
}

proxy_canada = {
    'https': f'http://{LOGIN_CANADA}:{PASSWORD_CANADA}@138.128.19.109:9999'
}

proxy_usa = {
    'https': f'http://{LOGIN_USA}:{PASSWORD_USA}@181.177.103.207:9145'
}

proxy_russia_shared = {
    'https': f'http://{LOGIN_RUSSIA_SHRD}:{PASSWORD_RUSSIA_SHRD}@194.67.200.14:9741'
}

proxies = [proxy_usa, proxy_canada, proxy_russia, proxy_russia_shared]


def get_location(url):
    response = requests.get(url=url, proxies=random.choice(proxies))
    soup = Soup(response.text, 'html.parser')

    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()

    print(f'IP: {ip}\nLocation: {location}')


if __name__ == '__main__':
    # times_sleeps = [1.23, 2.03, 3.3, 4.21, 5.5]
    # url = 'https://2ip.ru/'
    # for i in range(10):
    #     get_location(url)
    #     time_start = time.time()
    #     time.sleep(random.choice(times_sleeps))
    #     time_end = time.time() - time_start
    #     print(time_end)


    # url1 = 'https://www.wildberries.ru/catalog/produkty/zamorozhennaya-produktsiya'
    # response = requests.get(url=url1, proxies=proxy_russia_shared)
    # print(response.status_code)
    # print(type(proxy_russia_shared['https'][-4:]))

    pywhatkit.sendwhatmsg_instantly(phone_no='+79160526963', message='Test message')