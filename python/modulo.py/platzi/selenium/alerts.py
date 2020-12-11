import time
import unittest
from selenium import webdriver

class Alert(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.implicitly_wait(15)
        bot.maximize_window()
        bot.get("http://demo-store.seleniumacademy.com/")

    def test_compare_products_removal_alert(self):
        bot = self.bot
        search_field = bot.find_element_by_name("q")

        search_field.send_keys("Tee")
        search_field.submit()

        time.sleep(5)

        bot.find_element_by_class_name("link-compare").click()
        bot.find_element_by_link_text("Clear All").click()

        time.sleep(4)

        alert = bot.switch_to_alert()
        alert_text = alert.text

        alert.accept()

        time.sleep(4)


    def tearDown(self):
        self.bot.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)