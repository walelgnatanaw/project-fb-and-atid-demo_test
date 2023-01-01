from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from fb_locator import *

def test_login():
    driver=webdriver.Chrome()
    driver.get(facebook_linkage)
    driver.find_element(By.XPATH,facebook).click()
    sleep(1)
    driver.find_element(By.NAME,user_name_enter).send_keys("0547227371")
    sleep(1)
    driver.find_element(By.NAME,password_enter).send_keys("123waliy")
    sleep(2)
    driver.find_element(By.NAME,login_button).click()
    sleep(2)
def test_forgotpassword():
     driver = webdriver.Chrome()
     driver.get(linkage_fb)
     driver.maximize_window()
     sleep(1)
     driver.find_element(By.XPATH,fb).click()
     sleep(2)
     driver.find_element(By.NAME,user_email).send_keys('0547227371')
     sleep(2)
     driver.find_element(By.XPATH,forg_password).click()
     sleep(2)
     driver.find_element(By.XPATH,enter_send_code).click()
def test_invalid_message():
    driver = webdriver.Chrome()
    driver.get(linkage_fb1)
    driver.maximize_window()
    sleep(1)
    driver.find_element(By.XPATH,fb1).click()
    sleep(2)
    driver.find_element(By.NAME, user_email).send_keys('0547227371')
    sleep(2)
    driver.find_element(By.NAME,forg_password).send_keys('')
    error_message=driver.find_element(By.XPATH,path).click()
    assert "invalid password"==error_message
def test1_invalid_message():
    driver = webdriver.Chrome()
    driver.get(linkage_fb2)
    driver.maximize_window()
    sleep(1)
    driver.find_element(By.XPATH,fb2).click()
    sleep(2)
    driver.find_element(By.NAME, user_email2).send_keys('')
    sleep(2)
    driver.find_element(By.NAME,forg_password2).send_keys('123waliy')
    error_message=driver.find_element(By.XPATH,path2)
    assert "invalid password"==error_message








