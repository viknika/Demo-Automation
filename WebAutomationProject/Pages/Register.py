from selenium import webdriver
from selenium.webdriver.support.ui import Select


class registerPage():

    def __init__(self,driver):
        self.driver = driver
        self.login_xpath = "//a[@class='login']"
        self.firstname_textbox_xpath = "//input[@placeholder='First Name']"
        self.lastname_textbox_xpath = "//input[@placeholder='Last Name']"
        self.address_textbox_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]"
        self.email_textbox_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]"
        self.phone_textbox_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]"
        self.gender_male_xpath = "//label[1]//input[1]"
        self.gender_female_xpath = "//label[2]//input[1]"
        self.hobbies_cricket_xpath = "//input[@id='checkbox1']"
        self.hobbies_movies_xpath = "//input[@id='checkbox2']"
        self.hobbies_hockey_xpath = "//input[@id='checkbox3']"
        self.languages_xpath = "//li[15]"
        self.skills_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[8]/div[1]/select[1]"
        self.country_xpath = "//select[@id='countries']"
        self.dob_year_xpath ="//select[@id='yearbox']"
        self.dob_month_xpath = "//select[@placeholder='Month']"
        self.dob_day_xpath = "//select[@id='daybox']"
        self.password_xpath = "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[12]/div[1]/input[1]"
        self.conf_password_xpath = "//input[@id='secondpassword']"
        self.submit_button = "//button[@id='submitbtn']"
        self.refresh_button = "//button[@id='Button1']"



    def enter_firstname(self, firstname):
        self.driver.find_element_by_xpath(self.firstname_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.firstname_textbox_xpath).send_keys(firstname)
        #self.driver.implicity_wait(10)

    def enter_lastname(self, lastname):
        self.driver.find_element_by_xpath(self.lastname_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.lastname_textbox_xpath).send_keys(lastname)
        #self.driver.implicity_wait(10)

    def enter_address(self, address):
        self.driver.find_element_by_xpath(self.address_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.address_textbox_xpath).send_keys(address)
        #self.driver.implicity_wait(10)

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)
        #self.driver.implicity_wait(10)

    def enter_phone(self, phone):
        self.driver.find_element_by_xpath(self.phone_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.phone_textbox_xpath).send_keys(phone)
        #self.driver.implicity_wait(10)

    def choose_gender(self,gender ):
        if gender =="Male":
            self.driver.find_element_by_xpath(self.gender_male_xpath).click()
        if gender =="FeMale":
            self.driver.find_element_by_xpath(self.gender_female_xpath).click()

    def choose_hobbies(self, hobby):
        if hobby == "Cricket":
            self.driver.find_element_by_xpath(self.hobbies_cricket_xpath).click()
        if hobby == "Movies":
            self.driver.find_element_by_xpath(self.hobbies_movies_xpath).click()
        if hobby == "Hockey":
            self.driver.find_element_by_xpath(self.hobbies_hockey_xpath).click()

    def choose_languages(self):
        self.driver.find_element_by_xpath("//div[@id='msdd']").click()
        self.driver.find_element_by_xpath(self.languages_xpath).click()

    def choose_skills(self,skill):
        element = self.driver.find_element_by_xpath(self.skills_xpath)
        drp = Select(element)
        drp.select_by_visible_text(skill)

    def choose_country(self,country):
        element = self.driver.find_element_by_xpath(self.country_xpath)
        drp = Select(element)
        drp.select_by_visible_text(country)

    def dateOfBirth(self, year,month,day):
        element_y = self.driver.find_element_by_xpath(self.dob_year_xpath)
        drp_y = Select(element_y)
        drp_y.select_by_visible_text(year)
        element_m = self.driver.find_element_by_xpath(self.dob_month_xpath)
        drp_m = Select(element_m)
        drp_m.select_by_visible_text(month)
        element_d = self.driver.find_element_by_xpath(self.dob_day_xpath)
        drp_d = Select(element_d)
        drp_d.select_by_visible_text(day)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def confirm_password(self,password):
        self.driver.find_element_by_xpath(self.conf_password_xpath).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.submit_button).click()




