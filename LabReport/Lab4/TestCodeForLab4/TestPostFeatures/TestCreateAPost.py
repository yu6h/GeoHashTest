import time
import unittest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestCreateAPost(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:3000/')
        sign_in_button = self.driver.find_element_by_css_selector("a[href='/keystone/signin']")
        sign_in_button.click()

        self.driver.implicitly_wait(10)
        input_email = self.driver.find_element_by_css_selector("input[name='email']")
        input_email.send_keys("demo@keystonejs.com")
        input_password = self.driver.find_element_by_css_selector("input[name='password']")
        input_password.send_keys("demo")

        sign_in_button_by_sigin_page = self.driver.find_element_by_css_selector("button[class='css-2960tt']")
        sign_in_button_by_sigin_page.click()


    def test_create_a_post_by_ECC_TC001_T1(self):

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys("")
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()
        warnging_text = self.driver.find_element_by_xpath("//div[@class='css-1nqppvz']/div")
        self.assertEquals("Name is required", warnging_text.get_attribute('innerHTML').strip())

        cancel_new_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="cancel"]')
        cancel_new_post_button.click()

    def test_create_a_post_by_ECC_TC001_T2(self):

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys("Wakanda forever")
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[contains(@id,'keystone-html-0_ifr')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("Spider man")

        self.driver.switch_to.default_content()

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        self.assertEquals(
            "Wakanda forever", new_post_link.get_attribute('innerHTML').strip()
        )

        delete_post_button = self.driver.find_element_by_xpath("//button[contains(@class,'ItemList__control--delete')]")
        delete_post_button.click()

        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

    def test_create_a_post_by_ECC_TC001_T3(self):
        self.driver.implicitly_wait(10)
        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()
        self.driver.implicitly_wait(10)
        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys("Hdasfuidsfhdsssdsafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffqqqqqqqqqqqqq")
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[contains(@id,'keystone-html-0_ifr')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("AAAAAuidgyiueowffesafffffffffffffffffffffffffffdsfsdfDGDEEffffffffffffffffffffffffqqqxxxxxxxwertiopu")

        self.driver.switch_to.default_content()

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        self.assertEquals(
            "Hdasfuidsfhdsssdsafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffqqqqqqqqqqqqq"
            , new_post_link.get_attribute('innerHTML').strip()
        )

        delete_post_button = self.driver.find_element_by_xpath("//button[contains(@class,'ItemList__control--delete')]")
        delete_post_button.click()

        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

    def test_create_a_post_by_ECC_TC001_T4(self):

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys('Ha@#488adf-=+')
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[contains(@id,'keystone-html-0_ifr')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("486*a=-#$%/fdg56Ss")

        self.driver.switch_to.default_content()

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        self.assertEquals(
            'Ha@#488adf-=+', new_post_link.get_attribute('innerHTML').strip()
        )

        delete_post_button = self.driver.find_element_by_xpath("//button[contains(@class,'ItemList__control--delete')]")
        delete_post_button.click()

        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

    def test_create_a_post_by_BPC_TC001_happy_path_choice(self):
        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()

        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys("Wakanda forever")

        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[contains(@id,'keystone-html-0_ifr')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("Spider man")

        self.driver.switch_to.default_content()

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        self.assertEquals(
            "Wakanda forever", new_post_link.get_attribute('innerHTML').strip()
        )

        delete_post_button = self.driver.find_element_by_xpath("//button[contains(@class,'ItemList__control--delete')]")
        delete_post_button.click()

        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

    def test_create_a_post_by_BPC_TC001_alternative_path_choice(self):
        self.driver.implicitly_wait(10)
        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()
        self.driver.implicitly_wait(10)
        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys("")
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()
        warnging_text = self.driver.find_element_by_xpath("//div[@class='css-1nqppvz']/div")
        self.assertEquals("Name is required", warnging_text.get_attribute('innerHTML').strip())

        cancel_new_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="cancel"]')
        cancel_new_post_button.click()

    def tearDown(self) -> None:

        sign_out_link = self.driver.find_element_by_xpath('//a[@title="Sign Out"]')
        sign_out_link.click()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
