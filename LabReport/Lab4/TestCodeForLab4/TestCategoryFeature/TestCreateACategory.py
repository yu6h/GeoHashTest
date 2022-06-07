import time
import unittest
from selenium import webdriver

class TestCreateACategory(unittest.TestCase):
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

        category_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-categories"]')
        category_page_button.click()

    def test_create_a_category_by_ECC_TC007_T1(self):
        self.category = None
        create_category_button = self.driver.find_element_by_xpath('//*[@data-e2e-list-create-button="no-results"]')
        create_category_button.click()

        if self.category:
            category_inputText = self.driver.find_element_by_xpath('//input[@name="name"]')
            category_inputText.send_keys(self.category)

        confirm_create_category_button = self.driver.find_element_by_xpath('//*[@data-button-type="submit"]')
        confirm_create_category_button.click()

        warning_div = self.driver.find_element_by_xpath('//*[@data-alert-type="danger"]')
        self.assertEqual("Name is required", warning_div.text)

        close_cofirm_dialog_button = self.driver.find_element_by_xpath('//*[@class="css-rd63ky"]')
        close_cofirm_dialog_button.click()

        self.assertFalse(self.isCategoryItemExistedOnCategoryPage(self.category))

    def test_create_a_category_by_ECC_TC007_T2(self):
        self.category = "Running Up That Hill"
        create_category_button = self.driver.find_element_by_xpath('//*[@data-e2e-list-create-button="no-results"]')
        create_category_button.click()

        if self.category:
            category_inputText = self.driver.find_element_by_xpath('//input[@name="name"]')
            category_inputText.send_keys(self.category)

        confirm_create_category_button = self.driver.find_element_by_xpath('//*[@data-button-type="submit"]')
        confirm_create_category_button.click()

        back_to_category_page_button = self.driver.find_element_by_xpath('//*[@class="css-dmf4a8"]')
        back_to_category_page_button.click()

        self.assertTrue(self.isCategoryItemExistedOnCategoryPage(self.category))

    def test_create_a_category_by_ECC_TC007_T3(self):
        self.category = 'Hdasfuidsfhdsssdsafffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffqqqqqqqqqqqqq'
        create_category_button = self.driver.find_element_by_xpath('//*[@data-e2e-list-create-button="no-results"]')
        create_category_button.click()

        if self.category:
            category_inputText = self.driver.find_element_by_xpath('//input[@name="name"]')
            category_inputText.send_keys(self.category)

        confirm_create_category_button = self.driver.find_element_by_xpath('//*[@data-button-type="submit"]')
        confirm_create_category_button.click()

        back_to_category_page_button = self.driver.find_element_by_xpath('//*[@class="css-dmf4a8"]')
        back_to_category_page_button.click()

        self.assertTrue(self.isCategoryItemExistedOnCategoryPage(self.category))

    def test_create_a_category_by_ECC_TC007_T4(self):
        self.category = "sdfds1561%^&+=!"
        create_category_button = self.driver.find_element_by_xpath('//*[@data-e2e-list-create-button="no-results"]')
        create_category_button.click()

        if self.category:
            category_inputText = self.driver.find_element_by_xpath('//input[@name="name"]')
            category_inputText.send_keys(self.category)

        confirm_create_category_button = self.driver.find_element_by_xpath('//*[@data-button-type="submit"]')
        confirm_create_category_button.click()

        back_to_category_page_button = self.driver.find_element_by_xpath('//*[@class="css-dmf4a8"]')
        back_to_category_page_button.click()

        self.assertTrue(self.isCategoryItemExistedOnCategoryPage(self.category))



    def test_create_a_category_by_BPC_TC007_P1(self):
        self.category = "test category"
        create_category_button = self.driver.find_element_by_xpath('//*[@data-e2e-list-create-button="no-results"]')
        create_category_button.click()

        if self.category:
            category_inputText = self.driver.find_element_by_xpath('//input[@name="name"]')
            category_inputText.send_keys(self.category)

        confirm_create_category_button = self.driver.find_element_by_xpath('//*[@data-button-type="submit"]')
        confirm_create_category_button.click()

        back_to_category_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-categories"]')
        back_to_category_page_button.click()

        self.assertTrue(self.isCategoryItemExistedOnCategoryPage(self.category))

    def test_create_a_category_by_BPC_TC007_P2(self):
        self.category = "test category"
        create_category_button = self.driver.find_element_by_xpath('//*[@data-e2e-list-create-button="no-results"]')
        create_category_button.click()

        if self.category:
            category_inputText = self.driver.find_element_by_xpath('//input[@name="name"]')
            category_inputText.send_keys(self.category)

        cancel_create_category_button = self.driver.find_element_by_xpath('//*[@data-button-type="cancel"]')
        cancel_create_category_button.click()

        self.assertFalse(self.isCategoryItemExistedOnCategoryPage(self.category))

    def isCategoryItemExistedOnCategoryPage(self,category_name):
        if len(self.driver.find_elements_by_xpath("//*[normalize-space()='%s']/ancestor::tr" % category_name)) > 0:
            return True
        else:
            return False

    def tearDown(self) -> None:

        if self.category and self.isCategoryItemExistedOnCategoryPage(self.category):
            delete_button = self.driver.find_element_by_xpath("//*[normalize-space()='%s']/ancestor::tr//*[contains(@class,'ItemList__control--delete')]" % self.category)
            delete_button.click()

            confirm_delete_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
            confirm_delete_button.click()

        sign_out_link = self.driver.find_element_by_xpath('//a[@title="Sign Out"]')
        sign_out_link.click()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
