from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# options
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--kiosk")

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

driver = webdriver.Chrome(
    executable_path="C:\\drChrome\\chromedriver\\chromedriver.exe",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("http://91.242.35.147/security/authenticate")
    time.sleep(3)

    email_input = driver.find_element_by_xpath("//input[@type='text']")
    email_input.clear()
    email_input.send_keys("hiARTER")
    time.sleep(3)

    password_input = driver.find_element_by_xpath("//input[@type='password']")
    password_input.clear()
    password_input.send_keys("hiARTER1")
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    driver.get("http://91.242.35.147/promotions")
    time.sleep(10)

    task_button = driver.find_element_by_xpath("//button['@id=main-scroll]/div/div[1]/button']").click()
    time.sleep(10)

    group_button = driver.find_element_by_xpath("//section[@id=main-scroll]/div/div[3]/div[1]/div[2]").click()
    time.sleep(5)

    tor_button = driver.find_element_by_xpath("//section[@id=main-scroll]/div/div[3]/div[1]/div[2]/div[2]/div"
                                              "/span[1]/div]").click()
    time.sleep(5)

    #
    # news_link = driver.find_element_by_id("l_nwsf").click()
    # time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
