import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.maximize_window()
        bot.implicitly_wait(15)
        bot.get("https://the-internet.herokuapp.com/")
        bot.find_element_by_xpath('//*[@id="content"]/ul/li[9]/a').click()


    def test_dinamyc_elements(self):
        iterator = 0

        while True:
            try:
                sleep(2)
                self.bot.find_element_by_xpath('//*[@id="content"]/div/ul/li[5]/a')
                print(f"Se han realizado en total {iterator} intentos")
                break

            except:
                sleep(2)
                iterator += 1
                self.bot.refresh()
                print(f"Vamos {iterator} intentos")


    def tearDown(self):
        self.bot.quit()








if __name__ == "__main__":
    unittest.main(verbosity = 2)