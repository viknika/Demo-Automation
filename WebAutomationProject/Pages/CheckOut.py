from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class checkoutPage():

    def __init__(self, driver):
        self.driver = driver
        self.checkout = "//a[@class='checkout-button button alt wc-forward']"
        self.bill_firstname_xpath = "//input[@id='billing_first_name']"
        self.bill_lastname_xpath = "//input[@id='billing_last_name']"
        self.bill_email_address_xpath = "//input[@id='billing_email']"
        self.bill_phone = "//input[@id='billing_phone']"
        self.bill_country_drdw = "//span[@id='select2-chosen-1']"
        self.bill_country_search = "//input[@id='s2id_autogen1_search']"
        self.country_xpath = "//span[@class='select2-match']"
        self.bill_street = "//input[@id='billing_address_1']"
        self.bill_city ="//input[@id='billing_city']"
        self.bill_province_drdw ="//div[@id='s2id_billing_state']//b"
        self.bill_province_search = "//input[@id='s2id_autogen2_search']"
        self.bill_province_xpath = "//span[@class='select2-match']" #//span[contains(@class,'select2-match')]
        self.bill_postcode_xpath = "//input[@id='billing_postcode']"
        self.bill_payment_option = "//input[@id='payment_method_cod']"
        self.placeorder_xpath = "//input[@id='place_order']"


    def proceed_check_out(self):
        checkout = self.driver.find_element_by_xpath("//a[@class='checkout-button button alt wc-forward']")
        actions = ActionChains(self.driver)
        actions.move_to_element(checkout).click().perform()

    def enter_bill_firstname(self, firstname):
        self.driver.find_element_by_xpath(self.bill_firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.bill_firstname_xpath).send_keys(firstname)
        # self.driver.implicity_wait(10)

    def enter_bill_lastname(self, lastname):
        self.driver.find_element_by_xpath(self.bill_lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.bill_lastname_xpath).send_keys(lastname)
        # self.driver.implicity_wait(10)

    def enter_bill_email_address(self, address):
        self.driver.find_element_by_xpath(self.bill_email_address_xpath).clear()
        self.driver.find_element_by_xpath(self.bill_email_address_xpath).send_keys(address)
        # self.driver.implicity_wait(10)


    def enter_bill_phone(self, phone):
        self.driver.find_element_by_xpath(self.bill_phone).clear()
        self.driver.find_element_by_xpath(self.bill_phone).send_keys(phone)
        # self.driver.implicity_wait(10)

    def select_bill_country(self,coun):
        self.driver.find_element_by_xpath(self.bill_country_drdw).click()
        self.driver.find_element_by_xpath(self.bill_country_search).send_keys(coun)
        self.driver.find_element_by_xpath(self.country_xpath).click()

    def enter_bill_street(self,street):
        self.driver.find_element_by_xpath(self.bill_street).send_keys(street)

    def enter_bill_city(self,city):
        self.driver.find_element_by_xpath(self.bill_city).send_keys(city)

    def select_bill_province(self,prov):
        self.driver.find_element_by_xpath(self.bill_province_drdw).click()
        self.driver.find_element_by_xpath(self.bill_province_search).send_keys(prov)
        self.driver.find_element_by_xpath(self.bill_province_xpath).click()

    def enter_bill_postcode(self,postcode):
        self.driver.find_element_by_xpath(self.bill_postcode_xpath).send_keys(postcode)

    def select_the_payment_option(self):
        self.driver.find_element_by_xpath(self.bill_payment_option).click()

    def place_order(self):
        self.driver.find_element_by_xpath(self.placeorder_xpath)

