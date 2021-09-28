import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_Globales
from Funciones.Funciones import Funciones_Globales
from Funciones.Page_Login import Pagina_Login


tg=.2
class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        # driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")



    def test1(self):
        driver=self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/text-box",tg)
        f.Texto_Mixto("id","userName","Rodrigo",tg)
        f.Texto_Mixto("id","userEmail","rodrigo@gmail.com",tg)
        f.Texto_Mixto("id","currentAddress","Demo uno de texto, para pruebas.",tg)
        f.Texto_Mixto("id","permanentAddress","Demo uno de texto, para pruebas.",tg)
        f.Click_Mixto("id","submit",tg)








    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()






