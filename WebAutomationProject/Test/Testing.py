import unittest
from selenium import webdriver
from WebAutomationProject.Pages.Register import registerPage
from WebAutomationProject.Pages.AddToCart import addtocartPage
from WebAutomationProject.Pages.CheckOut import checkoutPage
import HtmlTestRunner


class WAPTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/Veronika/PycharmProjects/Selenium/WebAutomationProject/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test1(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/Register.html")

        signUp = registerPage(driver)
        signUp.enter_firstname("Vik")
        signUp.enter_lastname("Mor")
        signUp.enter_address("15 Tom Cook, Maple, ON, L6A4N6")
        signUp.enter_email("VikMor@gmail.com")
        signUp.enter_phone("4168425789")
        signUp.choose_gender("FeMale")
        signUp.choose_hobbies("Movies")
        signUp.choose_hobbies("Hockey")
        signUp.choose_languages()
        signUp.choose_skills("Python")
        signUp.choose_country("Canada")
        signUp.dateOfBirth("2000","January","1")

        driver.implicitly_wait(10)

        signUp.enter_password("Vik159")
        signUp.confirm_password("Vik159")
        signUp.submit()
        driver.implicitly_wait(10)

        driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/WebAutomationProject/ScreenShots/register.png")

    def test2(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")

        add = addtocartPage(driver)

        add.start_purchase()
        add.choose_item()
        add.add_item_to_cart()
        add.view_cart()

        driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/WebAutomationProject/ScreenShots/add.png")

    def test3(self):
        driver = self.driver

        checkout = checkoutPage(driver)

        checkout.proceed_check_out()
        checkout.enter_bill_firstname("Vik")
        checkout.enter_bill_lastname("Mor")
        checkout.enter_bill_email_address("VikMor@gmail.com")
        checkout.enter_bill_phone("4168425789")
        checkout.select_bill_country("canada")
        checkout.enter_bill_street("15 Tom Cook")
        checkout.enter_bill_city("Maple")
        checkout.select_bill_province("ontario")
        checkout.enter_bill_postcode("L6A4N6")
        checkout.select_the_payment_option()
        checkout.place_order()



        driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/WebAutomationProject/ScreenShots/bill.png")




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
