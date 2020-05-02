from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



'''
#search on google, and open instagram
open_Browser.get('https://www.google.com')

search_box = open_Browser.find_element_by_name('q')

search_box.send_keys("instagram")
time.sleep(2)
#submit_btn = open_Browser.find_element_by_name('btnK')
submit_button = open_Browser.find_element_by_css_selector("input[type='submit']")
#print(submit_btn.get_attribute("name"))
time.sleep(2)
submit_button.click()
insta = open_Browser.find_element_by_xpath("/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a/h3")
time.sleep(2)
insta.click()'''


user_name = 'setuappa3842'
password = 'PbUfKDL7FDuzFNP'


open_Browser = webdriver.Chrome()

open_Browser.get('https://www.instagram.com/')
time.sleep(3)
insta_username = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
insta_username.send_keys(user_name)
insta_password = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
insta_password.send_keys(password)
time.sleep(3)
insta_submit = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
insta_submit.click()    
time.sleep(2)

'''
#not_now = open_Browser.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
WebDriverWait(open_Browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='aOOlW   HoLwm ']"))).click()
# WebDriverWait(open_Browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.aOOlW.HoLwm"))).click()

time.sleep(3)
#not_now.click()

'''

ui.WebDriverWait(open_Browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

search_for = open_Browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
search_for.send_keys("antripa003")
time.sleep(3)
ant = open_Browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a")
time.sleep(3)
ant.click()

time.sleep(3)
'''
followers = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
following = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
time.sleep(2)

following.click()
time.sleep(3)


#scroll_box = ui.WebDriverWait(open_Browser, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]")))

time.sleep(2)
scroll_box = open_Browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")
last_ht, ht = 0, 1
while last_ht != ht:
    last_ht = ht
    time.sleep(1)
    ht = open_Browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
#scroll_box = open_Browser.find_element_by_xpath("/html/body/div[3]/div/div[2]")
'''

recent_post = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]")
time.sleep(2)
recent_post.click()
time.sleep(2)
likes = open_Browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button")
time.sleep(2)
likes.click()