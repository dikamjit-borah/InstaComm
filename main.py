from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv

user_name = ''
password = ''
profile = ''

followers_list = []
following_list = []
likers = []

def sleep(t):
    time.sleep(t)

def login(u_name, p_word):
    insta_username = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
    insta_username.send_keys(u_name)
    insta_password = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
    insta_password.send_keys(p_word)
    time.sleep(2)   
    
    insta_submit = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
    insta_submit.click()    
    time.sleep(2)

    ui.WebDriverWait(open_Browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

def open_profile(profile_id):
    search_for = open_Browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    search_for.send_keys(profile_id)
    time.sleep(3)

    ant = open_Browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a")
    time.sleep(3)
    
    ant.click()
    time.sleep(3)

def find_followers():
    followers = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
    time.sleep(2)

    followers.click()
    time.sleep(4)

    scroll_box = open_Browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")
    last_ht, ht = 0, 1
    
    
    
    while last_ht != ht:
        last_ht = ht
        time.sleep(1)
        follower_links = scroll_box.find_elements_by_tag_name('a')
        for link in follower_links:
            follower_name = link.text
            if(follower_name!=''):
                print(follower_name)
                followers_list.append(follower_name)
        ht = open_Browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)

def find_following():
    following = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
    time.sleep(2)

    following.click()
    time.sleep(3)

    scroll_box = open_Browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")
    last_ht, ht = 0, 1

  

    while last_ht != ht:
        last_ht = ht
        time.sleep(1)
        following_links = scroll_box.find_elements_by_tag_name('a')
        for link in following_links:
            following_name = link.text
            if(following_name!=''):
                print(following_name)
                following_list.append(following_name)
        ht = open_Browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)

def find_likers():
    recent_post = open_Browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]")
    time.sleep(2)
    recent_post.click()
    time.sleep(2)
    likes = open_Browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button")
    time.sleep(2)
    likes.click()
    time.sleep(3)
    scroll_box = open_Browser.find_element_by_xpath("/html/body/div[5]/div/div[2]/div")
    last_ht, ht = 0, 1
   
    while last_ht != ht:
        last_ht = ht
        time.sleep(1)
        likers_links = scroll_box.find_elements_by_tag_name('a')
        for link in likers_links:
            likers_name = link.text
            if(likers_name!=''):
                print(likers_name)
                likers.append(likers_name)
        ht = open_Browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)



def write_2_file(filename, listname):
    file1 = open(filename, 'w')
    for i in listname:
        file1.write(i + "\n")
    file1.close()


if __name__ == "__main__":
    
    profile = input("Targeted profile \n @")
    user_name = input("Your username \n @")
    password = input("Your password \n ")
    open_Browser = webdriver.Chrome()
    open_Browser.get('https://www.instagram.com/')
    sleep(2)
    login(user_name, password)
    open_profile(profile)
    find_followers()
    write_2_file('him_followers', followers_list)
    

   
