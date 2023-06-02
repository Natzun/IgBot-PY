# pip freeze | xargs pip uninstall -y
# pip freeze > requirements.txt
# * -- Imports
import os
import sys
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

# * -- Variables
title = "IgBot-PY"  # ? Title
path = os.path.realpath(__file__)  # ? Directory path

load_dotenv(dotenv_path=".env")  # ? Load .env file
test = os.getenv("TEST")  # ? Test variable

# * -- Functions


def clearConsole() -> None:  # ? Clear console
    os.system("cls" if os.name == "nt" else "clear")


def main() -> None:
    driver.get("https://www.instagram.com")

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
    )
    element.send_keys(os.getenv("USERNAME2"))

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
    )
    element.send_keys(os.getenv("PASSWORD"))
    element.send_keys(Keys.ENTER)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_aV"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))
    )
    element.send_keys(Keys.ENTER)

    # elem.clear()
    # elem.send_keys(Keys.RETURN)
    # driver.send_keys(Keys.RETURN)

    input(f"[{title}#main] Press Enter to close...")
    driver.close()

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        _, _, exc_tb = sys.exc_info()
        print(f"[{title}#__main__] error (line: {exc_tb.tb_lineno}): ", e)
