import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones():

    def __init__(self, driver):
        self.driver = driver


    def saludos(self):
        print("Hola desde la función")

    def saludos2(self):
        print("Esta es la segunda Función")
