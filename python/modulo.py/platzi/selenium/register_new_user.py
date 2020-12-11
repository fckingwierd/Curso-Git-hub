import unittest
from selenium import webdriver
class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.implicitly_wait(15)
        bot.maximize_window()
        bot.get("http://demo-store.seleniumacademy.com/")

    def test_new_user(self):
        bot = self.bot
        bot.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        bot.find_element_by_link_text("Log In").click()

        create_account_button = bot.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')

        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual("Create New Customer Account", bot.title)

        first_name = bot.find_element_by_id("firstname")
        midle_name = bot.find_element_by_id("middlename")
        last_name = bot.find_element_by_id("lastname")
        email = bot.find_element_by_id("email_address")
        password = bot.find_element_by_id("password")
        password_confirm = bot.find_element_by_id("confirmation")
        newsletter_confirmation = bot.find_element_by_xpath('//*[@id="form-validate"]/div[1]/ul/li[4]/label')
        register_button = bot.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(first_name.is_enabled()
        and midle_name.is_enabled()
        and last_name.is_enabled()
        and email.is_enabled()
        and password.is_enabled()
        and password_confirm.is_enabled()
        and newsletter_confirmation.is_enabled()
        and register_button.is_enabled())

        first_name.send_keys("Test")
        bot.implicitly_wait(2)
        midle_name.send_keys("Test")
        bot.implicitly_wait(2)
        last_name.send_keys("Test")
        bot.implicitly_wait(2)
        email.send_keys("Test@testingmail.com")
        bot.implicitly_wait(2)
        password.send_keys("Test")
        bot.implicitly_wait(2)
        password_confirm.send_keys("Test")
        bot.implicitly_wait(2)
        newsletter_confirmation.click()
        bot.implicitly_wait(2)
        register_button.click()

    def tearDown(self):
        self.bot.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)