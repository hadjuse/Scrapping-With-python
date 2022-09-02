#!/usr/bin/env python3
from datetime import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class WebScrapping:
    def __init__(self):
        self.prices = []
        self.article = ""
        self.name = []

    def Scrapp_page(self):
        # faire une fonction qui scrapp des pages 1 par 1
        self.article = input("Choisissez l'article que vous voulez recherchez \n")
        time.sleep(random.randint(2, 5))
        driver = webdriver.Chrome()
        # Whe are getting the URL
        driver.get("https://www.amazon.fr/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='sp-cc-accept']").click()
        time.sleep(random.randint(2, 5))

        # finding element by attribute thanks to the function ".find_element" (BASIC HTML KNOWLEDGE needed !)
        driver.find_element(By.XPATH,
                            "//input[@id='twotabsearchtextbox']").send_keys(self.article)
        driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        #same here
        p = driver.find_elements(By.XPATH, "//span[@class='a-price']")
        time.sleep(random.randint(2, 5))
        for price in p:
            if price.text != '':
                self.prices.append(price.text)
        time.sleep(random.randint(2, 5))
        ObjectName = driver.find_elements(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
        for name in ObjectName:
            if price.text != '':
                self.name.append(str(name.text.strip()))

        for i in range(len(self.prices)):
            self.prices[i] = self.prices[i].replace(',', '.')
            self.prices[i] = self.prices[i].replace('€', '')
            self.prices[i] = float(self.prices[i])

    def Price_Array(self):
        return self.prices

    def Name_Array(self):
        return self.prices

    def minimum_price(self):
        minimum1 = min(self.prices, default=0)
        return minimum1

    def max_price(self):
        maximum1 = max(self.prices, default=0)
        return maximum1

    def average_price(self):
        average1 = sum(self.prices) / len(self.prices)
        return average1


s = WebScrapping()
s.Scrapp_page()
maximum = s.max_price()
minimum = s.minimum_price()
average = s.average_price()
print(f"The average price of {s.article} = {average} €\n"
      f"The most expensive price of {s.article} is '{s.name[s.prices.index(minimum)]}' = {maximum} €\n"
      f"The cheapest price of  {s.article} is '{s.name[s.prices.index(minimum)]}' = {minimum}\n €")
