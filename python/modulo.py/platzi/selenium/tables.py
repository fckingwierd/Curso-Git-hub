import unittest
from selenium import webdriver
from time import sleep

class Table(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.maximize_window()
        bot.implicitly_wait(15)
        bot.get("https://the-internet.herokuapp.com/tables#edit")

    def test_table(self):
        bot = self.bot

        table = [[] for i in range (4)]
        second_table = []
    
        for i in range(4):
            for j in range(5):
                    row_data = bot.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{i + 1}]/td[{j + 1}]')
                    table[i].append(row_data.text)

        for i in range(5):
            header_table = bot.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]')
            second_table.append(header_table.text)

        third_table = [[] for i in range(len(table))]
 
        for j in range(len(table)):
            for i in range(5):
                third_table[j].append(second_table[i])
                third_table[j].append(table[j][i])
 
    def tearDown(self):
        self.bot.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)