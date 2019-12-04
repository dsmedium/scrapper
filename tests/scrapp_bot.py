from selenium import webdriver
import time
import unittest
from bot import scrapp

class ScrapSite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)


    def test_bot(self):
        driver = self.driver

        #navigating to url
        driver.get('https://www.ganderoutdoors.com/')

        # creating bot object
        bot = scrapp.Scrap(driver)

        # removing the advert popup
        bot.rem_popup()

        # navigating to archery page and setting up page
        bot.archery_page()

        # get all the urls of pages
        bot.populate_urls()

        # scrape the data from the pages
        bot.get_data()

        # get the second highest price
        bot.second_highest()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('Completed')

if __name__ == '__main__':
    unittest.main()
