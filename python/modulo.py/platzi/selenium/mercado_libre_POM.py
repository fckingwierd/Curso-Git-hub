from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
class MercadoLibrePom:
    def __init__ (self, bot, url):
        self._bot = bot
        self._url = url
    
    def load_page (self):
        self._bot.get(self._url)

    def submit_data (self, data):
        search_field = WebDriverWait(self._bot, 10).until(EC.element_to_be_clickable((By.NAME, "as_word")))
        search_field.send_keys(data)
        search_field.submit()

    def only_official_shops(self):
        only_official_shops_variable = WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Solo tiendas oficiales')))
        self._bot.execute_script("arguments[0].click();", only_official_shops_variable)
    
    def free_sending (self):
        free_sending_variable = WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Gratis')))
        self._bot.execute_script("arguments[0].click();", free_sending_variable)
   
    def fast_sending (self):
        fast_sending_variable = WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Llegan en menos de 24 hs')))
        self._bot.execute_script("arguments[0].click();", fast_sending_variable)

    def without_interest(self):
        without_interest_variable = WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Sin interés")))
        self._bot.execute_script("arguments[0].click();", without_interest_variable)
               
    def condition(self, data):
        if data.lower() == "nuevo":
            condition_variable =  WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Nuevo")))
            self._bot.execute_script("arguments[0].click();", condition_variable)
        elif data.lower() == "usado":
            condition_variable = WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Usado")))
            self._bot.execute_script("arguments[0].click();", condition_variable)

    def relative_price(self, first, second):
        first_variable = WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.NAME, 'Mínimo')))
        first_variable.send_keys(first)

        second_variable = WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.NAME, 'Máximo')))
        second_variable.send_keys(second)

        submit_button = self._bot.find_element_by_class_name("ui-search-price-filter-action-btn")
        self._bot.execute_script("arguments[0].click();", submit_button)

    
    def best_sellers(self):
        best_sellers_variable = WebDriverWait(self._bot, 15).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Mejores vendedores")))
        self._bot.execute_script("arguments[0].click();", best_sellers_variable)
        
    def quantity(self):
        href_list = []
        name_list = []
        price_list = []

        for i in range(25):
            try:
                quantity_list = self._bot.find_element_by_xpath(f'/html/body/main/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a')
                price_variable = self._bot.find_element_by_xpath(f'/html/body/main/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]')

                href_element = quantity_list.get_attribute("href")
                name_element = quantity_list.get_attribute("title")

                href_list.append(href_element)
                name_list.append(name_element)
                price_list.append(price_variable.text)
    
            except:
                continue
        
        product_list = [[] for i in range (len(name_list))]
    
        for i in range (len(name_list)):
            product_list[i].append(name_list[i])
            product_list[i].append(price_list[i])
            product_list[i].append(href_list[i])

        return product_list
