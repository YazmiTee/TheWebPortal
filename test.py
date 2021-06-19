from django.test import LiveServerTestCase
from selenium import webdriver



class Hosttest(LiveServerTestCase):
    
    def testHomepage(self):
        driver = webdriver.chrome('\Users\yterr\Documents\SEP project')

        driver.get('http://127.0.0.1:8000/')

        assert "The Web Portal" in driver.title