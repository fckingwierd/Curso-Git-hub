from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
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
    def hashtag(self,hashtags):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/"+hashtags+"/")
        time.sleep(6)
    def download_image(self,amount):
        bot = self.bot
        iterator = 0
        bot.find_element_by_class_name("_9AhH0").click()
        while iterator <= amount:
            time.sleep(10)
            bot.find_element_by_xpath("//div[@aria-label='Me gusta']");
            bot.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            iterator += 1




ed = InstaBot ("thiagochiesa2010@hotmail.com","flamigera123")
ed.login()
ed.hashtag("amazing")
ed.download_image(5)
