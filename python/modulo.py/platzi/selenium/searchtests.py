from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.implicitly_wait(15)
        bot.maximize_window()
        bot.get("https://www.youtube.com/")
        time.sleep(7)
    
    def test_search_donow(self):
        bot = self.bot
        search_field = bot.find_element_by_name("search_query").send_keys("black clover" + Keys.RETURN)
        time.sleep(5)

    def tearDown(self):
        bot = self.bot
        bot.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)