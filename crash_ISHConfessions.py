from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with open('beemovie.txt', 'r') as filee:
    words = list(filee.read().split())

beemovie = words


for i, word in enumerate(beemovie):
    web = webdriver.Chrome()

    web.get('https://docs.google.com/forms/d/e/1FAIpQLSdJZoaSniRyd3rjQ6z8W_IvmysEY201PzM0VmfEeU3_bxeRnw/viewform')

    time.sleep(2)


    confession_box = web.find_element(by = By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/textarea')

    confession_box.send_keys(word)


    submit = web.find_element(by = By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    submit.click()

    time.sleep(1)


    get_confirmation_divtext = web.find_element(by = By.CSS_SELECTOR, value='.vHW8K')

    get_confirmation_divtext = get_confirmation_divtext.text

    if get_confirmation_divtext == 'Good job :D':
        print(f'submission {i} was succesfull')
    else:
        print(f'submission {i} was unsuccesfull')

    web.close()
