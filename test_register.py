import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from facebook_loketer import *

def test_registor():
    driver = webdriver.Chrome()
    driver.get(facebook_path)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH,
                        registor_path).click()
    time.sleep(3)
    loketerfname = driver.find_element(By.NAME, firstname).send_keys("walelgn")
    time.sleep(1)
    loketerlname = driver.find_element(By.NAME, lastname).send_keys("atanaw")
    time.sleep(1)
    driver.find_element(By.NAME, email).send_keys("0547227371")

    time.sleep(1)
    pasword = driver.find_element(By.XPATH,paswerd).send_keys("123waliy")
    time.sleep(1)
    driver.find_element(By.XPATH,mounth).send_keys(
        "mar")
    time.sleep(1)

    driver.find_element(By.XPATH, day).send_keys("23")
    time.sleep(1)
    driver.find_element(By.ID, year).send_keys("1997")
    time.sleep(1)

    driver.find_element(By.XPATH, gender).click()
    time.sleep(1)
    signin = driver.find_element(By.XPATH, sinup).click()
    time.sleep(20)

def test_invalid_facebook_register():
        # empty first name
    driver = webdriver.Chrome()
    driver.get(facebook_path1)
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.XPATH,
                    registor_path1).click()
    time.sleep(3)
    loketerfname = driver.find_element(By.NAME, firstname1).send_keys("")
    time.sleep(1)
    loketerlname = driver.find_element(By.NAME, lastname1).send_keys("atanaw")
    time.sleep(1)
    driver.find_element(By.NAME, email1).send_keys("0547227371")
    time.sleep(1)
    pasword = driver.find_element(By.XPATH, paswerd1).send_keys("123waliy")
    time.sleep(1)
    driver.find_element(By.XPATH, mounth1).send_keys(
        "mar")
    time.sleep(1)
    driver.find_element(By.XPATH, day1).send_keys("23")
    time.sleep(1)
    driver.find_element(By.ID, year1).send_keys("1997")
    time.sleep(1)
    driver.find_element(By.XPATH, gender1).click()
    time.sleep(1)
    signin = driver.find_element(By.XPATH, sinup1).click()
    time.sleep(20)
    Error_message = driver.find_element(By.XPATH,error_message1).text
    assert 'invalid firstname' == Error_message
def test_invalid_facebook_register1():
#empty lastname
        driver = webdriver.Chrome()
        driver.get(facebook_path2)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            registor_path2).click()
        time.sleep(3)
        loketerfname = driver.find_element(By.NAME, firstname2).send_keys("walelgn")
        time.sleep(1)
        loketerlname = driver.find_element(By.NAME, lastname2).send_keys("")
        time.sleep(1)
        driver.find_element(By.NAME, email2).send_keys("0547227371")

        time.sleep(1)
        pasword = driver.find_element(By.XPATH, paswerd2).send_keys("123waliy")
        time.sleep(1)
        driver.find_element(By.XPATH, mounth2).send_keys(
            "mar")
        time.sleep(1)

        driver.find_element(By.XPATH, day2).send_keys("23")
        time.sleep(1)
        driver.find_element(By.ID, year2).send_keys("1997")
        time.sleep(1)

        driver.find_element(By.XPATH, gender2).click()
        time.sleep(1)
        signin = driver.find_element(By.XPATH, sinup2).click()
        time.sleep(20)
        Error_message = driver.find_element(By.XPATH,error_message2).text
        assert 'invalid lastname' == Error_message
def test_invalid_facebook_register2():
#empty email
        driver = webdriver.Chrome()
        driver.get(facebook_path3)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            registor_path3).click()
        time.sleep(3)
        loketerfname = driver.find_element(By.NAME, firstname3).send_keys("walelgn")
        time.sleep(1)
        loketerlname = driver.find_element(By.NAME, lastname3).send_keys("atanaw")
        time.sleep(1)
        driver.find_element(By.NAME, email3).send_keys("")

        time.sleep(1)
        pasword = driver.find_element(By.XPATH, paswerd3).send_keys("123waliy")
        time.sleep(1)
        driver.find_element(By.XPATH, mounth3).send_keys(
            "mar")
        time.sleep(1)

        driver.find_element(By.XPATH, day3).send_keys("23")
        time.sleep(1)
        driver.find_element(By.ID, year3).send_keys("1997")
        time.sleep(1)

        driver.find_element(By.XPATH, gender3).click()
        time.sleep(1)
        signin = driver.find_element(By.XPATH, sinup3).click()
        time.sleep(20)
        Error_message = driver.find_element(By.XPATH,error_message3).text
        assert 'invalid email' == Error_message
def test_invalid_facebook_register3():
#empty password
        driver = webdriver.Chrome()
        driver.get(facebook_path4)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            registor_path4).click()
        time.sleep(3)
        loketerfname = driver.find_element(By.NAME, firstname4).send_keys("walelgn")
        time.sleep(1)
        loketerlname = driver.find_element(By.NAME, lastname4).send_keys("atanaw")
        time.sleep(1)
        driver.find_element(By.NAME, email4).send_keys("")

        time.sleep(1)
        pasword = driver.find_element(By.XPATH, paswerd4).send_keys("123waliy")
        time.sleep(1)
        driver.find_element(By.XPATH, mounth4).send_keys(
            "mar")
        time.sleep(1)

        driver.find_element(By.XPATH, day4).send_keys("23")
        time.sleep(1)
        driver.find_element(By.ID, year4).send_keys("1997")
        time.sleep(1)

        driver.find_element(By.XPATH, gender4).click()
        time.sleep(1)
        signin = driver.find_element(By.XPATH, sinup4).click()
        time.sleep(20)
        Error_message = driver.find_element(By.XPATH,error_message4).text
        assert 'invalid password' == Error_message
def test_invalid_facebook_register4():
#empty month
        driver = webdriver.Chrome()
        driver.get(facebook_path5)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            registor_path5).click()
        time.sleep(3)
        loketerfname = driver.find_element(By.NAME, firstname5).send_keys("walelgn")
        time.sleep(1)
        loketerlname = driver.find_element(By.NAME, lastname5).send_keys("atanaw")
        time.sleep(1)
        driver.find_element(By.NAME, email5).send_keys("")

        time.sleep(1)
        pasword = driver.find_element(By.XPATH, paswerd5).send_keys("123waliy")
        time.sleep(1)
        driver.find_element(By.XPATH, mounth5).send_keys(
            "")
        time.sleep(1)

        driver.find_element(By.XPATH, day5).send_keys("23")
        time.sleep(1)
        driver.find_element(By.ID, year5).send_keys("1997")
        time.sleep(1)

        driver.find_element(By.XPATH, gender5).click()
        time.sleep(1)
        signin = driver.find_element(By.XPATH, sinup5).click()
        time.sleep(20)
        Error_message = driver.find_element(By.XPATH,error_message5).text
        assert 'Invalid month' == Error_message
def test_invalid_facebook_register5():
#empty  day
        driver = webdriver.Chrome()
        driver.get(facebook_path6)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            registor_path6).click()
        time.sleep(3)
        loketerfname = driver.find_element(By.NAME, firstname6).send_keys("walelgn")
        time.sleep(1)
        loketerlname = driver.find_element(By.NAME, lastname6).send_keys("atanaw")
        time.sleep(1)
        driver.find_element(By.NAME, email6).send_keys("0547227371")

        time.sleep(1)
        pasword = driver.find_element(By.XPATH, paswerd6).send_keys("123waliy")
        time.sleep(1)
        driver.find_element(By.XPATH, mounth6).send_keys(
            "mar")
        time.sleep(1)

        driver.find_element(By.XPATH, day6).send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, year6).send_keys("1997")
        time.sleep(1)

        driver.find_element(By.XPATH, gender6).click()
        time.sleep(1)
        signin = driver.find_element(By.XPATH, sinup6).click()
        time.sleep(20)
        Error_message = driver.find_element(By.XPATH,error_message6).text
        assert 'Invalid day' == Error_message
def test_invalid_facebook_register6():
#empty  year
        driver = webdriver.Chrome()
        driver.get(facebook_path7)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            registor_path7).click()
        time.sleep(3)
        loketerfname = driver.find_element(By.NAME, firstname7).send_keys("walelgn")
        time.sleep(1)
        loketerlname = driver.find_element(By.NAME, lastname7).send_keys("atanaw")
        time.sleep(1)
        driver.find_element(By.NAME, email7).send_keys("0547227371")

        time.sleep(1)
        pasword = driver.find_element(By.XPATH, paswerd7).send_keys("123waliy")
        time.sleep(1)
        driver.find_element(By.XPATH, mounth7).send_keys(
            "mar")
        time.sleep(1)

        driver.find_element(By.XPATH, day7).send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, year7).send_keys("1997")
        time.sleep(1)

        driver.find_element(By.XPATH, gender7).click()
        time.sleep(1)
        signin = driver.find_element(By.XPATH, sinup7).click()
        time.sleep(20)
        Error_message = driver.find_element(By.XPATH,error_message7).text
        assert 'Invalid year' == Error_message
def test_invalid_facebook_register7():
#empty  gender
        driver = webdriver.Chrome()
        driver.get(facebook_path8)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,
                            registor_path8).click()
        time.sleep(3)
        loketerfname = driver.find_element(By.NAME, firstname8).send_keys("walelgn")
        time.sleep(1)
        loketerlname = driver.find_element(By.NAME, lastname8).send_keys("atanaw")
        time.sleep(1)
        driver.find_element(By.NAME, email8).send_keys("0547227371")

        time.sleep(1)
        pasword = driver.find_element(By.XPATH, paswerd8).send_keys("123waliy")
        time.sleep(1)
        driver.find_element(By.XPATH, mounth8).send_keys(
            "mar")
        time.sleep(1)

        driver.find_element(By.XPATH, day8).send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, year8).send_keys("1997")
        time.sleep(1)

        driver.find_element(By.XPATH, gender8).click()
        time.sleep(1)
        signin = driver.find_element(By.XPATH, sinup8).click()
        time.sleep(20)
        Error_message = driver.find_element(By.XPATH,
                                        error_message8).text
        assert 'invalid gender' == Error_message






