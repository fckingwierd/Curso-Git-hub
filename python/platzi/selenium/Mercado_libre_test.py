import unittest
from selenium import webdriver
from mercado_libre_POM import MercadoLibrePom
import time

class Idk(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.maximize_window
        bot.implicitly_wait(15)

    def test_mercadolibre_buy(self):
        idk = MercadoLibrePom(self.bot, "https://www.mercadolibre.com.ar")

        idk.load_page()
        idk.submit_data("ps4")
        idk.free_sending()
        time.sleep(4)
        idk.without_interest()
        time.sleep(4)
        idk.condition("usado")
        time.sleep(5)
        idk.relative_price(2000, 3000)
        time.sleep(4)
        hola = idk.quantity()

        print(hola)

    def tearDown(self):
        self.bot.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)
