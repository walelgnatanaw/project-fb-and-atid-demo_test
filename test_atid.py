from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from atid_locator import *


def test_accessorie():
    driver = webdriver.Chrome()
    driver.get(atid_demo)
    sleep(2)
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH,accessories).click()

    sleep(3)#
    driver.find_element(By.XPATH,select_item).click()
    sleep(3)
    driver.find_element(By.XPATH,add_item).click()
    sleep(3)
    driver.find_element(By.XPATH,view_cart).click()
    sleep(3)
    bank=driver.find_element(By.XPATH,check_cart).text
    assert bank=="Cart"
    sleep(3)
    coupon_field=driver.find_element(By.XPATH,coupon)
    coupon_field.clear()
    sleep(3)
    coupon_field.send_keys('dfghjkyu78')
    sleep(3)
    driver.close()




def test_store():
    driver = webdriver.Chrome()
    driver.get(atid_demo1)
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH,store).click()
    sleep(3)#
    driver.find_element(By.XPATH,select_item1).click()
    sleep(3)#
    driver.find_element(By.XPATH,add_item1).click()
    sleep(3)
    driver.find_element(By.XPATH,view_cart1).click()
    sleep(4)
    name = driver.find_element(By.XPATH, check_cart1).text
    assert name == 'Anchor Bracelet'
    coupon_field=driver.find_element(By.XPATH,coupon1)
    sleep(3)
    coupon_field.clear()
    coupon_field.send_keys('2345rty')
    sleep(3)
    driver.close()


def test_women():
    driver = webdriver.Chrome()
    driver.get(atid_demo2)
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH,women).click()
    sleep(3)
    driver.find_element(By.XPATH,select_item2).click()
    sleep(3)
    driver.find_element(By.XPATH,add_item2).click()
    sleep(3)
    driver.find_element(By.XPATH,view_cart2).click()
    sleep(3)
    name=driver.find_element(By.XPATH,check_cart2).text
    assert name=="Anchor Bracelet"
    sleep(3)
    coupon_fiel=driver.find_element(By.XPATH,coupon2)
    coupon_fiel.clear()
    sleep(3)
    coupon_fiel.send_keys('1234w')
    sleep(3)

def test_men():
    driver = webdriver.Chrome()
    driver.get(atid_demo3)
    driver.maximize_window()
    driver.find_element(By.XPATH,men).click()
    sleep(3)
    driver.find_element(By.XPATH,select_item3).click()
    sleep(3)
    driver.find_element(By.XPATH,add_item3).click()
    sleep(3)
    driver.find_element(By.XPATH,view_cart3).click()
    sleep(3)
    atanaw=driver.find_element(By.XPATH,check_cart3).text
    sleep(3)
    assert atanaw=="ATID Green Tshirt"
    sleep(3)
    coupon_field=driver.find_element(By.XPATH,coupon3)
    sleep(3)
    coupon_field.clear()
    sleep(3)
    coupon_field.send_keys('345ert')
    sleep(3)
    driver.close()

