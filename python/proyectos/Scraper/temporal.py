from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter.font import Font
import time
import wget
import operator 
import os
import glob

class InstaBot:
    def __init__(self,username,password, photo_counter=0, hashtag_iterator=0):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        self.photo_counter = photo_counter
        self.hashtag_iterator = hashtag_iterator 
        self.like_dictionary = {}
        self.like_iterator = 0
    
    def window_label(self):
        hashtags = []
        root = Tk()
        def plus_hashtags():
            hashtag = my_scraper.get()
            if len(hashtag) > 1:
                 hashtags.append(str(hashtag))
                 my_scraper.delete(0, END)
                 ready_button = Button (root, text = "Listo", padx = 15, pady = 2, command = ready_func)
                 ready_button.grid(row = 1, column = 2)
            else:
                my_scraper.insert(0, "Introduce hashtags de 2 caracteres o mas")

        def ready_func():
            root.destroy()
            self.penetrating(hashtags)
        

        my_text = Label(root, text = "Introduce Hashtags")
        my_scraper = Entry(root, width = 25, borderwidth = 5)
        ready_button = Button (root, text = "Listo", padx = 15, pady = 2, state = DISABLED )
        plus_button = Button (root, text = "Agregar", padx = 15, pady = 2,  command = plus_hashtags)

        ready_button.grid(row = 1, column = 2)
        plus_button.grid (row = 1, column = 1)
        my_text.grid(row = 0, column = 0, columnspan = 3)
        my_scraper.grid(row = 1, column = 0)

        root.mainloop()
    
    def penetrating(self, hashtags):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

        bot.find_element_by_class_name("KPnG0").click() 
        time.sleep(4)

        bot.find_element_by_id("email").send_keys(self.username)
        bot.find_element_by_id("pass").send_keys(self.password + Keys.RETURN)
        time.sleep(9)

        bot.get("https://www.instagram.com/explore/tags/"+hashtags[0]+"/")
        time.sleep(3)

        self.__get_image(hashtags)

    def __get_image(self, hashtags):
        bot = self.bot

        root = Tk()
        root.title("Photos")

        image_url = []
        image_container = bot.find_elements_by_class_name("FFVAD")

        for i in range(len(image_container) - 1):
            image_structure = image_container[i]
            image = image_structure.get_attribute("src")
            image_url.append(image)

        def administration():
            global quantity
            quantity = my_entry.get()
            if len(quantity) == 0:
                my_entry.insert(0, "Tienes que poner un valor numérico")

            else:
                root.destroy()

                bot.find_element_by_class_name('_9AhH0').click()
                quantity = int(quantity)

                for i in range(quantity):
                    time.sleep(1.5)

                    try:
                        like = bot.find_element_by_class_name('Nm9Fw').text
                        new_like = like.replace(' Me gusta', '')
                        if ',' in new_like:
                            new_like = new_like.replace(',', '')

                    except:
                        pass

                    new_like = int(new_like)

                    self.like_dictionary[self.like_iterator] = new_like
                    self.like_iterator += 1

                    bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()

                self.__download_image(image_url, quantity, hashtags[self.hashtag_iterator])

    
        my_text = Label(root, text = f"Hay {len(image_url)} posibles descargas en el hashtag \nCuantas fotos quieres descargar? ")
        my_entry = Entry(root, width = 25, borderwidth = 5)
        ready_button = Button (root, text = "Okey", padx = 15, pady = 2, command = administration )

        my_text.grid(row = 0, column = 0)
        my_entry.grid(row = 1, column = 0)
        ready_button.grid(row = 1, column= 1)

        root.mainloop()

        print("\nDescarga completa")
        print (f"Se han registrado {quantity} descargas en el hashtag '{hashtags[self.hashtag_iterator]}'. ")
        respuesta = str(input("Quieres terminar y/n?: "))

        if respuesta.lower() == "y":
            bot.quit()
            self.tkinter_image(hashtags)

            files = glob.glob('e:/proyecto/python/Scraper/Photos/*')
            for f in files:
                os.remove(f)

            return
 
        self.hashtag_iterator += 1

        if self.hashtag_iterator == len(hashtags):
            self.hashtag_iterator = 0

        bot.get(f"https://www.instagram.com/explore/tags/{hashtags[self.hashtag_iterator]}/")
        time.sleep(3)
        self.__get_image(hashtags)



    def __download_image(self, image_url, quantity, hashtag):
        for i in range(len(image_url) - 1):
            if i == quantity:
                break
            self.photo_counter += 1
            wget.download(image_url[i], f'E://proyecto//python//proyectos//Scraper//Photos//{self.photo_counter}.png')


    def tkinter_image(self, hashtags):
        bot = self.bot
        hashtag = str()

        for idx, i in enumerate (hashtags):
            if idx == len(hashtags) - 1:
                hashtag += ''.join(i)

            else:
                hashtag += ''.join(i + ', ' )

        new_like_dictionary = sorted(self.like_dictionary.items(), key=operator.itemgetter(1))
        new_like_dictionary.reverse()

        root = Tk()
        root.title(f'hashtags: ' + hashtag)

        image_list = []
        row = 1
        column = 0
        i = 0
        like_list = []

        main_frame = Frame(root)
        main_frame.pack(fill=BOTH, expand = 1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand = 1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)

        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
        
        while True:
            try: 
                i += 1
                image = ImageTk.PhotoImage(Image.open(f'E://proyecto//python//proyectos//Scraper//Photos//{i}.png'))
                image_list.append(image)

            except FileNotFoundError:
                break 

        for like_value in new_like_dictionary:
            like_list.append(int(like_value[0]))

        print(new_like_dictionary)
        print(like_list)
        print(len(image_list))

        for photos in like_list:
            my_image = Label(second_frame, image = image_list[photos])
            my_image.grid(row = row, column = column)
            column += 1
            if column > 2:
                column = 0
                row += 1

        root.mainloop()
    

ed = InstaBot ("thiagochiesa2010@hotmail.com","flamigera123")
ed.window_label()
