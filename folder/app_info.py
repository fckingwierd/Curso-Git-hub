from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    def hashtag(self,hashtag):
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(6)
    def download_image(self,amount):
        bot = self.bot
        iterator = 0
        while iterator <= amount:
            bot.find_element_by_class_name("Nnq7C weEfm")
            bot.find_element_by_class_name("eLAPa")
            image_container = bot.find_element_by_class_name("KL4Bh")
            image_url = image_container.find("img",)["src"]
            urllib.request.urlretrieve(f"https:{image_url}")



ed = InstaBot ("thiagochiesa2010@hotmail.com","flamigera123")
ed.login()
ed.hashtag("amazing")
ed.download_image(5)

