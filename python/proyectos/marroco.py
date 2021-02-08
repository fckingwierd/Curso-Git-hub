from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time


class InstagramFollower(unittest.TestCase):
    def setUp(self, username='thiagochiesa444@gmail.com', password='flamigera'):
        self.bot = webdriver.Firefox()
        
        bot = self.bot
        self.username = username
        self.password = password

        bot.maximize_window()
        bot.implicitly_wait(10)

    def test_follow_users(self):
        bot = self.bot
        iterator = 0

        bot.get('https://instagram.com')

        username = WebDriverWait(bot, 15).until(EC.element_to_be_clickable((By.NAME, 'username')))
        password = WebDriverWait(bot, 15).until(EC.element_to_be_clickable((By.NAME, 'password')))
 
        username.send_keys(self.username)
        password.send_keys(self.password + Keys.RETURN)

        time.sleep(3)

        bot.get('https://www.instagram.com/chiesa__idk/')

        followers = WebDriverWait(bot, 10).until(lambda s: s.find_element_by_class_name('nal3 '))
        followers.click()






        


        












    def tearDown(self):
        self.bot.quit()
        
        


















if __name__ == '__main__':
    unittest.main(verbosity=2)
