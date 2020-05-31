from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import sys
import getpass

load_dotenv()

# get data form env file
amazon_email = os.getenv("AMAZON_EMAIL")
# amazon_password = os.getenv("AMAZON_PASSWORD")
netflix_email = os.getenv("NETFLIX_EMAIL")
# netflix_password = os.getenv("NETFLIX_PASSWORD")
netflix_account_name = os.getenv("NETFLIX_ACCOUNT_NAME")
opal_username = os.getenv("OPAL_USERNAME")
# opal_password = os.getenv("OPAL_PASSWORD")
university_name = os.getenv("UNIVERSITY_NAME")
driver_type = os.getenv("DRIVER_TYPE")


class Login(object):
    def __init__(self):
        if driver_type == "firefox":
            self.driver = webdriver.Firefox(executable_path='./driver/geckodriver')
        elif driver_type == "chrome":
            self.driver = webdriver.Chrome(executable_path='./driver/chromedriver')

    def login_by_name(self, name):
        if name == "amazon":
            amazon_password = input("Password: ")
            self.driver.get('https://www.amazon.de/Amazon-Video/b?ie=UTF8&node=3010075031')
            try:
                # wait for <a>
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@id='nav-link-accountList']"))
                )
                # find Loggin Button
                link = self.driver.find_element_by_xpath("//a[@id='nav-link-accountList']")
                link.click()
                # wait for email input
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='ap_email']"))
                )
                email_input = self.driver.find_element_by_xpath("//input[@id='ap_email']")
                # send email to input
                email_input.send_keys(amazon_email, Keys.ENTER)
                # wait for pass input
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.ID, "ap_password"))
                )
                # send pass to input
                pass_input = self.driver.find_element_by_xpath("//input[@id='ap_password']")
                pass_input.send_keys(amazon_password, Keys.ENTER)
            except Exception:
                self.driver.quit()

        if name == "netflix":
            netflix_password = input("Password: ")
            self.driver.get('https://www.netflix.com/de-en/login')
            try:
                # find and wait for email input
                email_input = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='id_userLoginId']"))
                )
                email_input.send_keys(netflix_email)
                # set checkbox of remember me to false
                self.driver.execute_script("document.getElementsByName('rememberMe').value='false'")
                # find and wait for password input
                pass_input = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='id_password']"))
                )
                pass_input.send_keys(netflix_password, Keys.ENTER)
                # go to your account by Account Name
                account_link = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[text()='{netflix_account_name}']"))
                )
                account_link.click()
            except Exception:
                self.driver.quit()

        if name == "opal":
            opal_password = getpass.getpass("Password: ")
            self.driver.get("https://bildungsportal.sachsen.de/opal/")
            # select specific university form options
            select_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, f"//select[@name='wayfselection']/option[text()='{university_name}']"))
            )
            select_element.click()
            # submit login
            login_button = self.driver.find_element_by_xpath("//button[@name='shibLogin']")
            login_button.click()

            # specific for TU Dresden
            if university_name == "TU Dresden":
                # find and wait for zih input field
                zih_input = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
                )
                # set zih username
                zih_input.send_keys(opal_username)
                # find password input
                password_input = self.driver.find_element_by_xpath("//input[@id='password']")
                password_input.send_keys(opal_password, Keys.ENTER)
                # find and wait for accept login button
                accept_input = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@name='_eventId_proceed']"))
                )
                accept_input.click()


# class Series(Login):
#     def __init__(self):
#         super().__init__()
#     def search_series_by_name(self, serie, where):
#         self.login_by_name(where)
#         if where == 'amazon':
#             pass


if __name__ == "__main__":
    args = sys.argv
    login_place = args[1]
    Login = Login()
    Login.login_by_name(login_place)









