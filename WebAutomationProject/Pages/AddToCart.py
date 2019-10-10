from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class addtocartPage():

    def __init__(self, driver):
        self.driver = driver
        self.practice_Tab_xpath = "//a[contains(text(),'Practice Site')]"
        self.add_item = "//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart']"
        self.view = "//a[@class='added_to_cart wc-forward']"


    def start_purchase(self):
        self.driver.find_element_by_xpath(self.practice_Tab_xpath).click()
        #self.driver.switch_to.alert.accept()

    def choose_item(self):
        #self.driver.implicity_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000) ", "")
        self.driver.save_screenshot("D:/Veronika/PycharmProjects/Selenium/WebAutomationProject/ScreenShots/homepage1.png")
        #self.driver.implicity_wait(5)

    def add_item_to_cart(self):
        self.driver.find_element_by_xpath(self.add_item).click()

    def view_cart(self):
        self.driver.find_element_by_xpath(self.view).click()

    def check_out(self):
        checkout = self.driver.find_element_by_xpath("//a[@class='checkout-button button alt wc-forward']")
        actions = ActionChains(self.driver)
        actions.move_to_element(checkout).click().perform()

