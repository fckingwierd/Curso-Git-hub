from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
import requests
import urllib
import time
class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)
        bot.find_element_by_class_name("KPnG0").click() 
        bot.find_element_by_id("email").send_keys(self.username)
        bot.find_element_by_id("pass").send_keys(self.password + Keys.RETURN)
        time.sleep(9)
    def download_image(self,amount, hashtags):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/"+hashtags+"/")
        response = requests.get("https://www.instagram.com/explore/tags/"+hashtags+"/")
        soup = BeautifulSoup(response.content, "html.parser")
        time.sleep(6)
        iterator = 0
        bot.find_element_by_class_name("_9AhH0").click()
        while iterator <= amount:
            time.sleep(6)
            image_container = BeautifulSoup.find_all(class_="KL4Bh")
            print (image_container)
            image_url = image_container.find("img")["src"]
            urlib.request.urlretrieve(image_url)
            bot.find_element_by_class_name("coreSpriteRightPaginationArrow").click()




ed = InstaBot ("thiagochiesa2010@hotmail.com","flamigera123")
ed.login()
ed.download_image(5, "amazing")
