from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from tkinter.font import Font
from googletrans import Translator
import unittest

class Novels(unittest.TestCase):
    def setUp(self):
        self.bot = webdriver.Firefox()
        bot = self.bot
        self.novel_list_name = list()
        self.novel_list_name_sorted = list()
        self.iterator = 0

        bot.implicitly_wait(10)

    def test_get_novel_names(self):
        root = Tk()

        def add_novel():
            entry_camp = entry.get()

            if len(entry_camp) > 2:
                self.novel_list_name.append(entry_camp)
                entry.delete(0, END)
                start_button = Button(root, text='Start', font=font, fg='white', bg='black', padx=10, pady=5, command=lambda:start_program())
                start_button.grid(row=1, column=1)

            else:
                entry.insert(0, 'Debes poner el nombre con mas de dos caracteres')
        
        def start_program():
            root.destroy()
    
        font = Font(family='Times New Roman', size=15)
        label = Label(root, text='Elige las novelas a descargar', font=font)
        entry = Entry(root, width=35, borderwidth=5, bg='white', fg='black')
        start_button = Button(root, text='Start', font=font, fg='white', bg='black', padx=10, pady=5, state=DISABLED)
        plus_button = Button(root, text='Plus', font=font, fg='white', bg='black', padx=10, pady=5, command=lambda:add_novel())

        label.grid(row=0, column=0)
        entry.grid(row=1, column=0)
        start_button.grid(row=1, column=1)
        plus_button.grid(row=1, column=2)

        root.mainloop()

        self.__sort_novels_names()

    def __sort_novels_names(self):
        novel_name = str()

        for i in range(len(self.novel_list_name)):
            variable = self.novel_list_name[i].split(' ')

            for i in range(len(variable)):
                novel_name += ''.join(variable[i] + '-')

            self.novel_list_name_sorted.append(novel_name + 'boxnovel')
            novel_name = str()

        self.__get_chapter_novels()
    
    def __get_chapter_novels(self):
        root = Tk()

        for i in range(len(self.novel_list_name_sorted)):
            def chapter_numbers_func():
                chapters_quantity = entry.get()
                
                if len(chapters_quantity) > 0:
                    root.quit()
                    chapters_quantity = int(chapters_quantity)
                    self.__download_novels(chapters_quantity)

                #else:
                    #entry.insert(0, 'Introduzca un numero de dos digitos o mas')

            font = Font(family='Times New Roman')
            label = Label(root, text=f'Introduzca la cantidad de capitulos a descargar de {self.novel_list_name[i]}', font=font)
            entry = Entry(root, width=35, borderwidth=5, fg='black', bg='white')
            start_button = Button(root, text='Start', font=font, fg='white', bg='black', padx=10, pady=5, command=lambda:chapter_numbers_func())

            label.grid(row=0, column=0)
            entry.grid(row=1, column=0)
            start_button.grid(row=1, column=1)

            root.mainloop()
            
    def __download_novels(self, chapters):
        bot = self.bot
        translator = Translator()
        chapter_entity = list()
        chapters_traduced = list()

        for i in range(chapters):
            bot.get('https://boxnovel.com/novel/' + self.novel_list_name_sorted[self.iterator] + f'/chapter-{i + 1}')
            chapter = bot.find_element_by_class_name('cha-words')
            chapter_entity.append(chapter.text)

        translations = translator.translate(chapter_entity, dest='es')

        for j in range(len(chapter_entity)):
            variable = chapter_entity[j].split()
            for i in range(len(variable)):
                chapter_entity[j] = ''.join(variable[i] + ' ')

        print(chapter_entity)

        #for translation in translations:
            #chapters_traduced.append(translation.text)

        #print(chapters_traduced)






        
        


    def tearDown(self):
        self.bot.quit()



if __name__ == '__main__':
    unittest.main(verbosity = 2)


