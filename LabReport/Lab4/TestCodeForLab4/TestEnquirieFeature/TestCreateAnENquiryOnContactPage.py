import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import warnings


class CreateANewEnquirieonContactPage(unittest.TestCase):
    def setUp(self):
        # Login Step
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.driver = webdriver.Chrome(options=options, executable_path='../chromedriver.exe')
        self.driver.get("http://127.0.0.1:3000/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_link_text("Contact").click()

    def testCase_happypath_Expect_create_new_enquirie_success(self):
        # InputData
        self.name = "Tony Stark"
        self.email = "enquirieTest@ntut.com"
        self.phone = "0912345678"
        self.Regarding = ""
        self.Message = "test for creating new enquirie in  contact page."
        print("testCase_happypath_Expect_create_new_enquirie_success running start")
        self.driver.find_element_by_name('name.full').send_keys(self.name)
        self.driver.find_element_by_name('email').send_keys(self.email)
        self.driver.find_element_by_name('phone').send_keys(self.phone)
        Select(self.driver.find_element_by_name('enquiryType')).select_by_index(1)
        self.driver.find_element_by_name('message').send_keys(self.Message)
        submitButton = self.driver.find_element_by_tag_name('form')
        submitButton.submit()
        time.sleep(1)
        assert "Success!" in self.driver.find_element_by_tag_name('h1').text
        print("testCase_happypath_Expect_create_new_enquirie_success running end")
        self.delete_a_enquiry(self.name)

    def testCase_with_T1_by_ECC_Expect_get_warning(self):
        # InputData
        self.name = None
        self.email = None
        self.phone = None
        self.Regarding = '(require)'
        self.Message = None
        print("testCase_with_T1_by_ECC_Expect_get_warning running start")

        submitButton = self.driver.find_element_by_tag_name('form')
        submitButton.submit()
        time.sleep(1)
        assert "Sorry, an error occurred loading the page (500)" in self.driver.find_element_by_tag_name('h1').text

        print("testCase_with_T1_by_ECC_Expect_get_warning running end")

    def testCase_with_T2_by_ECC_Expect_get_warning(self):

        self.name = 'T2testCreateAEnquiryonContactPage'
        self.email = ' '
        self.phone = 'phone'
        self.Regarding = 'Just leaving a message'
        self.Message = 'T2MessageForTestCreateAEnquiryonContactPage'
        print("testCase_with_T2_by_ECC_Expect_get_warning running start")
        self.driver.find_element_by_name('name.full').send_keys(self.name)
        self.driver.find_element_by_name('email').send_keys(self.email)
        self.driver.find_element_by_name('phone').send_keys(self.phone)
        self.inputRegarding(self.Regarding)
        self.driver.find_element_by_name('message').send_keys(self.Message)
        submitButton = self.driver.find_element_by_tag_name('form')
        submitButton.submit()
        time.sleep(1)
        assert "Sorry, an error occurred loading the page (500)" in self.driver.find_element_by_tag_name('h1').text

        print("testCase_with_T2_by_ECC_Expect_get_warning running end")

    def testCase_with_T3_by_ECC_Expect_get_warning(self):
        # InputData
        self.name = 'T3TestCreatedNewEnquirybyISPECC1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmno12345678'
        self.email = '109598073@ntut'
        self.phone = '09123'
        self.Regarding = "I've got a question"
        self.Message = 'T3TestCreatedNewEnquirybyISPECC1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmno12345678'
        print("testCase_with_T3_by_ECC_Expect_get_warning running start")
        self.driver.find_element_by_name('name.full').send_keys(self.name)
        self.driver.find_element_by_name('email').send_keys(self.email)
        self.driver.find_element_by_name('phone').send_keys(self.phone)
        self.inputRegarding(self.Regarding)
        self.driver.find_element_by_name('message').send_keys(self.Message)
        submitButton = self.driver.find_element_by_tag_name('form')
        submitButton.submit()
        time.sleep(1)
        assert "Sorry, an error occurred loading the page (500)" in self.driver.find_element_by_tag_name('h1').text
        print("testCase_with_T3_by_ECC_Expect_get_warning running end")

    def testCase_with_T4_by_ECC_Expect_create_new_enquirie_success(self):
        # InputData
        self.name = 'T4_testCreate@EnquiryonCont@ctPage###123'
        self.email = '109598073@ntut.com'
        self.phone = '09123456748'
        self.Regarding = "Something else..."
        self.Message = 'T4_MessageForTestCreate@EnquiryonCont@ctPage###123'
        print("testCase_with_T4_by_ECC_Expect_create_new_enquirie_success running start")
        self.driver.find_element_by_name('name.full').send_keys(self.name)
        self.driver.find_element_by_name('email').send_keys(self.email)
        self.driver.find_element_by_name('phone').send_keys(self.phone)
        self.inputRegarding(self.Regarding)
        self.driver.find_element_by_name('message').send_keys(self.Message)
        submitButton = self.driver.find_element_by_tag_name('form')
        submitButton.submit()
        time.sleep(1)
        assert "Success!" in self.driver.find_element_by_tag_name('h1').text
        print("testCase_with_T4_by_ECC_Expect_create_new_enquirie_success running end")
        self.delete_a_enquiry(self.name)

    def testCase_with_T5_by_ECC_Expect_create_new_enquirie_success(self):
        # InputData
        self.name = 'T5_testCreate@EnquiryonCont@ctPage###123'
        self.email = '109598073@ntut.com'
        self.phone = '091234567890'
        self.Regarding = "Something else..."
        self.Message = 'T5_MessageForTestCreate@EnquiryonCont@ctPage###123'
        print("testCase_with_T5_by_ECC_Expect_create_new_enquirie_success running start")
        self.driver.find_element_by_name('name.full').send_keys(self.name)
        self.driver.find_element_by_name('email').send_keys(self.email)
        self.driver.find_element_by_name('phone').send_keys(self.phone)
        self.inputRegarding(self.Regarding)
        self.driver.find_element_by_name('message').send_keys(self.Message)
        submitButton = self.driver.find_element_by_tag_name('form')
        submitButton.submit()
        time.sleep(1)
        assert "Success!" in self.driver.find_element_by_tag_name('h1').text
        print("testCase_with_T5_by_ECC_Expect_create_new_enquirie_success running end")
        self.delete_a_enquiry(self.name)

    def delete_a_enquiry(self, fullName):
        self.driver.find_element_by_link_text("Sign In").click()
        # Input email/password
        email = self.driver.find_element_by_name("email")  # id will change every time
        password = self.driver.find_element_by_name("password")
        email.send_keys("demo@keystonejs.com")
        password.send_keys("demo")
        # press signIn
        signInButton = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/form/button")
        signInButton.click()

        time.sleep(1)
        self.driver.find_element_by_link_text("Enquiries").click()  # route to Enquiries
        time.sleep(1)
        self.driver.find_element_by_link_text(fullName).click()
        time.sleep(1)

        self.driver.find_element_by_class_name('css-1mj7u0z').click()
        self.driver.find_element_by_class_name('css-t4884').click()
        time.sleep(1)

        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_link_text(fullName)
        time.sleep(1)

        self.driver.get("http://127.0.0.1:3000/keystone")
        signOutButton = self.driver.find_element_by_xpath(
            "//div[@id='react-root']/div/header/nav/div/ul[2]/li[2]/a/span")
        signOutButton.click()

    def tearDown(self):
        self.driver.close()

    def inputRegarding(self, Regarding):
        if Regarding == "Just leaving a message":
            selectIndex = 1
        elif Regarding == "I've got a question":
            selectIndex = 2
        elif Regarding == "Something else...":
            selectIndex = 3
        else:
            selectIndex = 0
        Select(self.driver.find_element_by_name('enquiryType')).select_by_index(selectIndex)


if __name__ == "__main__":
    unittest.main()