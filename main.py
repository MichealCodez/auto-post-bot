from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from twocaptcha import TwoCaptcha
import os
import time


def solve_captcha(url):
    api_key = os.getenv('APIKEY_2CAPTCHA', 'your api key')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.hcaptcha(
            sitekey='1dcf45a9-7c48-49f8-ba65-febc3f08d43f',
            url=f'{url}',
        )

    except Exception as e:
        print(e)
        return False

    else:
        return result


def access():
    try:
        accept = WebDriverWait(driver, 3).until(
            ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/div[3]/button')))
        accept.click()
        time.sleep(1)
        try:
            cancel = driver.find_element(By.XPATH, '/html/body/div/div[5]/div/div/div[1]/button')
            cancel.click()
        except:
            pass
        cook = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/button[1]')
        cook.click()
    except:
        pass


opt = webdriver.ChromeOptions()

opt.add_argument("--start-maximized")
opt.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=opt)

driver.get('https://milano.bakecaincontrii.com/')
time.sleep(3)
form = driver.find_element(By.XPATH, '/html/body/div/header/nav/div/div[2]/ul/li[3]/a')
form.click()
time.sleep(1)
access()
category = Select(driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div/div[2]/'
                                                'div/div[1]/select'))
category.select_by_visible_text('Donna Cerca Donna')

city = Select(driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div/div[2]/div/div[2]/select'))
city.select_by_visible_text('Livorno')

age = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div/div[3]/div/div[1]/input')
age.send_keys('46')

title = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div/div[3]/div/div[2]/textarea')
title.send_keys('Un capriccio molto capriccioso')

text = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div/div[3]/div/div[3]/textarea')
text.send_keys("""Mi piacerebbe incontrare una ragazza per una frequentazione non occasionale. No a fidanzamenti, matrimoni etc.etc.
Voglio stabilire con te un rapporto basato sui capricci di entrambi.
I miei sono quelli di vederti partecipare a mini gang, farti montare regolarmente dal bull di turno e, fare da taxista: mentre io guido, tu scopi.
Insomma tutte cose molto divertenti ed eccitanti.
Le caramelle per ogni incontro sono cin que cento
Tassativa breve conoscenza online ed incontro conoscitivo 
Sono una persona a modo, distinta ed educata. Garantisco e pretendo massima privacy.
Per cortesia leggi con attenzione e contattami SOLO se le tue aspettative corrispondono a quelle descritte.""")
time.sleep(1)

email_only = driver.find_element(By.XPATH, '//input[@value="1"]')
driver.execute_script("arguments[0].click();", email_only)

email_address = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div/div[4]/'
                                              'div[2]/div[1]/input')
email_address.send_keys('email')
time.sleep(1)


def capt():
    captcha = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '#hcap-script > iframe')))
    answer = solve_captcha(driver.current_url)
    try:
        code = answer['code']
        time.sleep(1)
        driver.execute_script(
            "document.querySelector(" + "'" + '[name="h-captcha-response"]' + "'" + ").innerHTML = " + "'" + code + "'")
        time.sleep(2)
        captcha.click()
        time.sleep(1)
        proceed = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[2]/'
                                                                                       'div[2]/form/div/div[9]/div/'
                                                                                       'button')))
        proceed.click()
    except:
        print('not capt')
        print(answer['code'])
        capt()


switch = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/div/div[6]/div[1]/label/input')
driver.execute_script("arguments[0].click();", switch)

capt()
access()
time.sleep(1)

proceed1 = driver.find_element(By.XPATH, '/html/body/div/main/form/div/div[4]/div/button')
proceed1.click()
access()

final = driver.find_element(By.XPATH, '/html/body/div/main/div/div[2]/div[2]/div[2]/div/div/div/button')
final.click()
access()

driver.execute_script('''window.open("","_blank");''')
driver.switch_to.window(driver.window_handles[1])


def vmail():
    driver.get("http://mail.com")
    time.sleep(5)
    iframe = driver.find_element(By.XPATH, '/html/body/div[3]/iframe')
    driver.switch_to.frame(iframe)
    iframe1 = driver.find_element(By.XPATH, '/html/body/iframe')
    driver.switch_to.frame(iframe1)
    agree = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div[2]/div/div/button')
    agree.click()
    driver.switch_to.default_content()

    signin = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/header/'
                                                                                  'div[1]/div[2]/a[2]')))
    signin.click()

    enter_email = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/'
                                                                                           'div/div/div/div[2]/form/'
                                                                                           'div[1]/input')))
    enter_email.send_keys('email')
    password = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[2]/form/div[2]/input')
    password.send_keys('password')
    enter = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/div/div/div[2]/form/button')
    enter.click()
    time.sleep(3)

    e_mail = driver.find_element(By.XPATH, '/html/body/nav/nav-actions-menu/div[1]/div[1]/a[2]')
    e_mail.click()
    time.sleep(5)

    frame = driver.find_element(By.ID, 'thirdPartyFrame_mail')
    driver.switch_to.frame(frame)

    time.sleep(5)
    spam = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[4]/div/div[3]/'
                                              'div[2]/div[2]/ul/li[2]/div/a')))
    spam.click()
    time.sleep(5)

    mail = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/div[1]/div/form/div[3]/div/'
                                         'div/table/tbody/tr[1]/td[2]')
    mail.click()

    time.sleep(3)

    frame2 = driver.find_element(By.ID, 'mail-detail')
    driver.switch_to.frame(frame2)
    time.sleep(5)
    message = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/div[7]/div/div/div/div/div/a')
    message.click()


try:
    vmail()
except:
    vmail()

time.sleep(3)
driver.close()
