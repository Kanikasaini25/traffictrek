import os
import subprocess
from multiprocessing import Pool
import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from utils import navigate_and_scroll
from utils import get_chrome_options
from utils import check_ip
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

def run_tor_browser():
    while True:
        profile_path = os.path.expandvars(
            r"C:\Users\melio\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")    # Update this path

        options = Options()
        options.set_preference("profile", profile_path)
        service = Service(executable_path=GeckoDriverManager().install())
        options.set_preference("network.proxy.type", 1)
        options.set_preference("network.proxy.socks", "127.0.0.1")
        options.set_preference("network.proxy.socks_port", 9050)
        options.set_preference("network.proxy.socks_remote_dns", False)

        try:
            torexe = subprocess.Popen(
                os.path.expandvars(
                    r"C:\Users\melio\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe")   # Update this path
            )
            with Firefox(service=service, options=options) as driver:
                navigate_and_scroll(driver, "https://assamesedailytimes.com")
                print(f"Request successful")
                time.sleep(2)
        except FileNotFoundError:
            print("Tor executable not found. Please check the path.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if torexe:
                print(f"Terminating Tor process with PID: {torexe.pid}")
                torexe.kill()

def run_chrome_with_tor_proxy():
    # Initialize Chrome WebDriver
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()), options=check_ip())
    try:
        # navigate_and_scroll(driver, "https://assamesedailytimes.com")
        # driver.get("http://check.torproject.org")
        # driver.get("https://ipv4.icanhazip.com/")
        print(f"Request successful")
        time.sleep(20)
    except FileNotFoundError:
        print("Tor executable not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # with ThreadPoolExecutor(max_workers=10) as executor:
    #     futures = [executor.submit(run_chrome_with_tor_proxy) for _ in range(6)]
    #     for future in futures:
    #         future.result()
    #     print("All threads have completed execution.")
    #     time.sleep(60)
    run_chrome_with_tor_proxy()
    with Pool(processes=8) as pool:
        for _ in range(9):
            pool.apply_async(check_ip)
        pool.close()
        pool.join()