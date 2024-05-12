from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions import scroll_to_bottom_infinte
from utils import get_random_integer
from selenium.webdriver.common.by import By
import time

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