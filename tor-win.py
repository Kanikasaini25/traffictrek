import os
import subprocess
import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from main import navigate_and_scroll

def run_tor_browser():
    while True:
        profile_path = os.path.expandvars(
            r"C:\Users\melio\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default")

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
                    r"C:\Users\melio\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe")
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

if __name__ == "__main__":
    # run_tor_browser()
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(run_tor_browser) for _ in range(600)]
        for future in futures:
            future.result()
        print("All threads have completed execution.")
        time.sleep(60)