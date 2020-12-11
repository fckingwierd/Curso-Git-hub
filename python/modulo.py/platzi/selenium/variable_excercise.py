import unittest
from selenium import webdriver
from time import sleep
from tkinter import *
from tkinter.font import Font

class AddRemoveElements(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        bot.implicitly_wait(15)
        bot.maximize_window()
        bot.get("https://the-internet.herokuapp.com/")
        bot.find_element_by_link_text("Add/Remove Elements").click()
    
    def test_add_remove(self):
        root = Tk()
        def add_func():
            operation_variable = entry_field.get()
            entry_field.delete(0, END)

            if len(operation_variable) > 0:
                first_variable = int(operation_variable)
                message = Label(root, text = "Introduce the amount of \nelements you want to subtract", font = my_font)
                okay_button = Button(root, text = "Okay", bg =  "black", fg = "white", width = 23, command = lambda: remove_func(first_variable))

                okay_button.grid (row = 3, column  = 0)
                message.grid(row = 0, column = 0)

            else:
                second_operation_variable = 0
                entry_field.insert(0, "You have to introduce a numerical value")
                
        def remove_func(first_variable):
            second_operation_variable = entry_field.get()

            if len(second_operation_variable) > 0:
                root.destroy()
                second_variable = int(second_operation_variable)
                self.__add_remove(first_variable, second_variable)

            else:
                second_operation_variable = 0
                entry_field.insert(0, "You have to introduce a numerical value ")
            
        my_font = Font (family = "Times New Roman", size = 15)
        message = Label(root, text = "Introduce the amount of\nelements you want to add", font = my_font)
        entry_field = Entry(root, width = 27, borderwidth = 5, bg = "black", fg = "white")
        okay_button = Button(root, text = "Okay", command = add_func, bg = "black", fg = "white", width = 23)


        message.grid(row = 0, column = 0)
        entry_field.grid (row = 2, column = 0)
        okay_button.grid (row = 3, column  = 0)

        root.mainloop()

    def __add_remove(self, first, second):
        for i in range(first):
            self.bot.find_element_by_xpath('//*[@id="content"]/div/button').click()
        sleep(3)
        for i in range(second):
            try:
                self.bot.find_element_by_xpath('//*[@id="elements"]/button').click()
            except :
                print ("You are trying to delete more elements than there is")

    def tearDown(self):
        self.bot.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)

        