import unittest
from selenium import webdriver
from time import sleep

class TyposTest(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.maximize_window()
        bot.implicitly_wait(15)
        bot.get("https://the-internet.herokuapp.com/typos")

    def test_typos(self):
        bot = self.bot

        correct_text = "Sometimes you'll see a typo, other times you won't."
        tries = 1

        while True:
            paragraph_to_check = bot.find_element_by_css_selector("#content > div > p:nth-child(3)")
            check_variable = paragraph_to_check.text

            if check_variable == correct_text:
                print(f"The test has been realized succesfully with {tries} tries")
                break
            else:
                tries += 1
                print (f"The test hasn't been realized succesfully with {tries} tries")
                bot.refresh()


    def tearDown(self):
        self.bot.quit()








if __name__ == "__main__":
    unittest.main(verbosity = 2)