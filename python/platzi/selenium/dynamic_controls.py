import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.maximize_window()
        bot.implicitly_wait(15)
        bot.get("https://the-internet.herokuapp.com/dynamic_controls")

    def test_dynamic_controls(self):
        self.bot.find_element_by_xpath('//*[@id="checkbox"]/input').click()

        self.bot.find_element_by_xpath('//*[@id="checkbox-example"]/button').click()

        self.bot.find_element_by_xpath('//*[@id="input-example"]/button').click()

        enable_button = WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/input')))
        enable_button.send_keys("TEST SUCCESFULLY COMPLETED")

        sleep(4)



    def tearDown(self):
        self.bot.quit()





if __name__ == "__main__":
    unittest.main(verbosity = 2)