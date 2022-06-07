import time
import unittest
from selenium import webdriver

class TestDeleteComment(unittest.TestCase):
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

        self.go_to_Comments_page()

        create_comment_button = self.driver.find_element_by_xpath('//*[@class="css-h629qq"]')
        create_comment_button.click()

        confrim_create_comment_button = self.driver.find_element_by_xpath("//*[contains(@type,'submit')]")
        confrim_create_comment_button.click()

        self.commentID = self.driver.find_element_by_xpath("//*[@class='EditForm__name-field']").text



    def go_to_Comments_page(self):
        comments_list_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-comments"]')
        comments_list_page_button.click()

    def test_delete_a_comment_by_BPC_TC006_P1(self):
        self.go_to_Comments_page()
        delete_comment_button = self.driver.find_element_by_xpath("//*[@title='%s']/..//preceding-sibling::*" % self.commentID)
        delete_comment_button.click()
        confirm_delete_comment_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_comment_button.click()

        comment_in_list = self.driver.find_elements_by_xpath("//*[@title='%s']"% self.commentID)
        self.assertTrue(len(comment_in_list) is 0)

    def test_delete_a_comment_by_BPC_TC006_P2(self):
        self.go_to_Comments_page()
        print(self.commentID)
        delete_comment_button = self.driver.find_element_by_xpath("//*[@title='%s']/ancestor::tr//button[contains(@class,'ItemList__control--delete')]" % self.commentID)
        delete_comment_button.click()
        confirm_delete_comment_button = self.driver.find_element_by_xpath('//*[@data-button-type="cancel"]')
        confirm_delete_comment_button.click()

        comment_in_list = self.driver.find_elements_by_xpath("//*[@title='%s']"% self.commentID)
        self.assertTrue(len(comment_in_list) is 1)

    def test_delete_a_comment_by_BPC_TC006_P3(self):
        delete_button_in_comment_edit_page = self.driver.find_element_by_xpath('//*[@data-button="delete"]')
        delete_button_in_comment_edit_page.click()
        confirm_delete_button_in_comment_edit_page = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_button_in_comment_edit_page.click()

        comment_in_list = self.driver.find_elements_by_xpath("//*[@title='%s']"% self.commentID)
        self.assertTrue(len(comment_in_list) is 0)

    def test_delete_a_comment_by_BPC_TC006_P4(self):
        delete_button_in_comment_edit_page = self.driver.find_element_by_xpath('//*[@data-button="delete"]')
        delete_button_in_comment_edit_page.click()
        cancel_delete_button_in_comment_edit_page = self.driver.find_element_by_xpath('//*[@data-button-type="cancel"]')
        cancel_delete_button_in_comment_edit_page.click()

        self.go_to_Comments_page()

        time.sleep(3)

        comment_in_list = self.driver.find_elements_by_xpath("//*[@title='%s']" % self.commentID)
        self.assertTrue(len(comment_in_list) is 1)

    def tearDown(self) -> None:
        self.go_to_Comments_page()

        comment_in_list = self.driver.find_elements_by_xpath("//*[@title='%s']/ancestor::tr" % self.commentID)
        if len(comment_in_list) is not 0:
            delete_comment_button = self.driver.find_element_by_xpath("//*[@title='%s']/ancestor::tr//button[contains(@class,'ItemList__control--delete')]" %self.commentID)
            delete_comment_button.click()

            confirm_delete_comment_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
            confirm_delete_comment_button.click()

        sign_out_link = self.driver.find_element_by_xpath('//a[@title="Sign Out"]')
        sign_out_link.click()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
