import time
import unittest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
class TestDeleteAPost(unittest.TestCase):
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

    def test_delete_a_post_by_ECC_TC003_T1(self):
        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        title = "Running Up That Hill"
        input_post_title.send_keys(title)
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                          'and normalize-space()="%s"]' % title)
        self.assertTrue(len(ListOfTestPost) == 1)

        delete_post_button = self.driver.find_element_by_xpath('//*[contains(@class,"ItemList__value ") and '\
                'normalize-space()="%s"]/ancestor::tr//*[contains('\
                '@class,"ItemList__control--delete")]' % title)

        delete_post_button.click()
        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                                            'and normalize-space()="%s"]' % title)

        self.assertTrue(len(ListOfTestPost) == 0)

    def test_delete_a_post_by_ECC_TC003_T2(self):
        title ="extenDsssssssssssdsfdsafdfwefwrrrrrStrangerThingsjfAaaaaaaaaaaaaawefaeddsvawedsvwefdwfaaaaaaaaqqqqqq"

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")

        input_post_title.send_keys(title)
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                          'and normalize-space()="%s"]' % title)
        self.assertTrue(len(ListOfTestPost) == 1)


        delete_post_button = self.driver.find_element_by_xpath('//*[contains(@class,"ItemList__value ") and '\
                'normalize-space()="%s"]/ancestor::tr//*[contains('\
                '@class,"ItemList__control--delete")]' % title)

        delete_post_button.click()
        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                                            'and normalize-space()="%s"]' % title)

        self.assertTrue(len(ListOfTestPost) == 0)

    def test_delete_a_post_by_ECC_TC003_T3(self):
        title = 'Ha&@#48$^$%df-=+'

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")

        input_post_title.send_keys(title)
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                                            'and normalize-space()="%s"]' % title)
        self.assertTrue(len(ListOfTestPost) == 1)

        delete_post_button = self.driver.find_element_by_xpath('//*[contains(@class,"ItemList__value ") and ' \
                                                               'normalize-space()="%s"]/ancestor::tr//*[contains(' \
                                                               '@class,"ItemList__control--delete")]' % title)

        delete_post_button.click()
        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                                            'and normalize-space()="%s"]' % title)

        self.assertTrue(len(ListOfTestPost) == 0)

    def test_delete_a_post_by_BPC_TC003_P1(self):
        title = 'testP1'

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")

        input_post_title.send_keys(title)
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                                            'and normalize-space()="%s"]' % title)
        self.assertTrue(len(ListOfTestPost) == 1)

        delete_post_button = self.driver.find_element_by_xpath('//*[contains(@class,"ItemList__value ") and ' \
                                                               'normalize-space()="%s"]/ancestor::tr//*[contains(' \
                                                               '@class,"ItemList__control--delete")]' % title)

        delete_post_button.click()
        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                                            'and normalize-space()="%s"]' % title)

        self.assertTrue(len(ListOfTestPost) == 0)

    def test_delete_a_post_by_BPC_TC003_P2(self):
        title = 'testP1'

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()
        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")

        input_post_title.send_keys(title)
        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                                            'and normalize-space()="%s"]' % title)
        self.assertTrue(len(ListOfTestPost) == 1)

        delete_post_button = self.driver.find_element_by_xpath('//*[contains(@class,"ItemList__value ") and ' \
                                                               'normalize-space()="%s"]/ancestor::tr//*[contains(' \
                                                               '@class,"ItemList__control--delete")]' % title)
        delete_post_button.click()

        cancel_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="cancel"]')
        cancel_delete_post_button.click()

        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value ")' \
                                                            'and normalize-space()="%s"]' % title)
        self.assertTrue(len(ListOfTestPost) == 1)


    def tearDown(self) -> None:
        ListOfTestPost = self.driver.find_elements_by_xpath('//*[contains(@class,"ItemList__value--text")]')
        if len(ListOfTestPost)!=0:
            delete_post_button = self.driver.find_element_by_xpath('//*[contains(@class,"ItemList__control--delete")]')
            delete_post_button.click()
            confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
            confirm_delete_post_button.click()

        sign_out_link = self.driver.find_element_by_xpath('//a[@title="Sign Out"]')
        sign_out_link.click()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
