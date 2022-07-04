from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from features.locatorsBank import locatorsBank
from features.test_data import testData
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class Bank:
    @given('I open XYZ Bank login page')
    def openLogpage(context):
        s = Service("C:\\webdriver\\chromedriver.exe")
        context.driver = webdriver.Chrome(service=s)
        context.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
        context.driver.implicitly_wait(10)
        context.driver.maximize_window()

    @when('I click on the "Bank Manager Login"')
    def clickBMlogin(context):
        context.driver.find_element(By.XPATH, locatorsBank.bank_manager_btn).click()

    @when('I add a new Customer')
    def addCustomer(context):
        context.driver.find_element(By.XPATH,locatorsBank.add_cust_btn).click()

        context.driver.find_element(By.XPATH,locatorsBank.cust_input_name).send_keys(testData.testname)

        context.driver.find_element(By.XPATH,locatorsBank.cust_input_lname).send_keys(testData.testLname)

        context.driver.find_element(By.XPATH,locatorsBank.cust_input_postal).send_keys(testData.testPostCode)

        context.driver.find_element(By.XPATH, locatorsBank.submit_cust).click()

        alert_obj = driver.switch_to.alert

        alert_obj.accept()


    @when('I search the customer on Customers list')
    def searchCustomer(context):
      context.driver.find_element(By.XPATH, locatorsBank.cust_btn).click()

      context.driver.find_element(By.XPATH, locatorsBank.search_field).send_keys("Ani")
      element = driver.find_element(By.XPATH, "//td[contains(text(),'Ani')]")
      if element.is_displayed():
        print("A New Customer is added")
      else:
        print("A new customer is not added")


    @then('I assert that customer is added with correct info')
    def assertCustomer(context):
        first_name = context.driver.find_element(By.XPATH,locatorsBank.name)
        last_name = context.driver.find_element(By.XPATH,locatorsBank.lname)
        p_code = context.driver.find_element(By.XPATH,locatorsBank.postal_code)
        assert first_name == testData.testname
        assert last_name == testData.testLname
        assert p_code == testData.testPostCode


    @when('delete customer')
    def deleteCustomer(context):
       dltbutton = context.driver.find_element(By.XPATH, '//tbody/tr[6]/td[5]/button[1]')
       dltbutton.click()
       assert dltbutton.is_displayed is True


    @then('assert that customer is deleted')
    def assertDeleted(context):
        dltd_cust =context.driver.find_element(By.XPATH,locatorsBank.name)
        if dltd_cust.is_displayed():
            print("Customer is not deleted")
        else:
            print ("Customer is deleted")


    @then('close browser')
    def closeBrowser(context):
     context.driver.close()


