import random
from multiprocessing import Pool
import requests
from random import randint
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions import scroll_to_bottom_infinte
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def navigate_and_scroll(driver, url):
    driver.get(url)

    navigation_menus = {
        0: "nation",
        1: "state",
        2: "world",
        3: "politics",
        4: "business",
        5: "entertainment",
        6: "sports",
        7: "opinion"
    }

    try:
        scroll_to_bottom_infinte(driver=driver, SCROLL_PAUSE_TIME=1)

        for _ in range(3):
            menu_item_name = navigation_menus[get_random_integer(0, 7)]
            menu_item_xpath = f"//*[text()='{menu_item_name}' and contains(@class,'nav-link')]"
            menu_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, menu_item_xpath)))
            menu_item.click()
            scroll_to_bottom_infinte(driver=driver, SCROLL_PAUSE_TIME=1)
            time.sleep(2)

        time.sleep(2)

    except Exception as e:
        print(e)

def get_random_integer(min, max):
    return randint(min, max)

def get_chrome_options():
    PROXY = "socks5://localhost:9050"
    options = ChromeOptions()
    options.add_argument('--proxy-server=%s' % PROXY)
    return options

def check_ip():
    session = requests.session()
    creds = str(random.randint(10000,0x7fffffff)) + ":" + "foobar"
    session.proxies = {
        'http': 'socks5h://{}:9050'.format(creds),
        'https': 'socks5h://{}:9050'.format(creds)
    }
    r = session.get('http://httpbin.org/ip')
    print(r.text)

def get_desired_capabilities():
    capabilities = dict(DesiredCapabilities.CHROME)
    capabilities['proxy'] = {
        'proxyType': 'MANUAL',
        'socksProxy': 'localhost:9050',
        'socksVersion': 5,
        'class': "org.openqa.selenium.Proxy",
        'autodetect': False
    }
    capabilities['proxy']['socksUsername'] = str(random.randint(10000,0x7fffffff))
    capabilities['proxy']['socksPassword'] = 'foobar'
    return capabilities
