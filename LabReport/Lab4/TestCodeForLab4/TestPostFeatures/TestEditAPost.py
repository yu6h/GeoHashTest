import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEditAPost(unittest.TestCase):
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

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()

        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys("test")

        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()



    def test_edit_a_post_by_ECC_TC002_T1(self):

        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        new_post_link.click()

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

    def test_edit_a_post_by_ECC_TC002_T2(self):

        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        new_post_link.click()


        state_span = self.driver.find_element_by_xpath('//div[contains(@class,"has-value")]')
        state_span.click()
        published_state = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[@aria-label="Published"]')
        published_state.click()

        author_div = self.driver.find_element_by_xpath('//*[@for="author"]//*[@class="Select-multi-value-wrapper"]')
        author_div.click()


        demo_user_author = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[normalize-space()="Demo User"]')
        demo_user_author.click()

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        date_input.click()

        prev_month_button = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-NavButton--prev")]')
        prev_month_button.click()

        first_day_in_month = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-Day") and normalize-space()=1]')
        first_day_in_month.click()

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_126']//iframe[contains(@id,'keystone-html')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("Stranger Things")
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_152']//iframe[contains(@id,'keystone-html')]"))
        content_extended = self.driver.find_element_by_xpath("//*[@id='tinymce']")
        content_extended.send_keys("I Am Ironman")
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0,0);")

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

    def test_edit_a_post_by_ECC_TC002_T3(self):

        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        new_post_link.click()

        state_span = self.driver.find_element_by_xpath('//div[contains(@class,"has-value")]')
        state_span.click()

        archived_state = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[@aria-label="Archived"]')
        archived_state.click()

        author_div = self.driver.find_element_by_xpath('//*[@for="author"]//*[@class="Select-multi-value-wrapper"]')
        author_div.click()

        demo_user_author = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[normalize-space()="Demo User"]')
        demo_user_author.click()

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        date_input.click()

        next_month_button = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-NavButton--next")]')
        next_month_button.click()

        first_day_in_month = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-Day") and normalize-space()=1]')
        first_day_in_month.click()

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_126']//iframe[contains(@id,'keystone-html')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("dsssssssssssssssssssssssasdsdafreeeeeeeeeeeeeeeeeeeegq4wefewrrrrrEadsfinweojfAaaaaaaaaaaaaaaaaaaaaa")
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_152']//iframe[contains(@id,'keystone-html')]"))
        content_extended = self.driver.find_element_by_xpath("//*[@id='tinymce']")
        content_extended.send_keys("extenDsssssssssssdsfdsafdfwefwrrrrrEadsfinweojfAaaaaaaaaaaaaawefaeddsvawedsvwefdwfaaaaaaaaqqqqqqqqq")
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0,0);")

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()



        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

    def test_edit_a_post_by_ECC_TC002_T4(self):

        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        new_post_link.click()

        state_span = self.driver.find_element_by_xpath('//div[contains(@class,"has-value")]')
        state_span.click()

        archived_state = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[@aria-label="Archived"]')
        archived_state.click()

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        date_input.click()

        next_month_button = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-NavButton--next")]')
        next_month_button.click()

        first_day_in_month = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-Day") and normalize-space()=1]')
        first_day_in_month.click()

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_126']//iframe[contains(@id,'keystone-html')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("abce*%^#$@)(")
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_152']//iframe[contains(@id,'keystone-html')]"))
        content_extended = self.driver.find_element_by_xpath("//*[@id='tinymce']")
        content_extended.send_keys("rewe)(3241=+/-+" )
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0,0);")

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())


    def test_edit_a_post_by_BPC_P1(self):
        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        new_post_link.click()

        state_span = self.driver.find_element_by_xpath('//div[contains(@class,"has-value")]//*[@class="Select-value-label"]')
        state_span.click()


        archived_state = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[@aria-label="Archived"]')
        archived_state.click()

        author_div = self.driver.find_element_by_xpath('//*[@for="author"]//*[@class="Select-multi-value-wrapper"]')
        author_div.click()

        demo_user_author = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[normalize-space()="Demo User"]')
        demo_user_author.click()

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        date_input.click()

        next_month_button = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-NavButton--next")]')
        next_month_button.click()

        first_day_in_month = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-Day") and normalize-space()=1]')
        first_day_in_month.click()

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_126']//iframe[contains(@id,'keystone-html')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("Bruno Mars")
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_152']//iframe[contains(@id,'keystone-html')]"))
        content_extended = self.driver.find_element_by_xpath("//*[@id='tinymce']")
        content_extended.send_keys("The Lazy Song" )
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0,0);")

        save_post_button = self.driver.find_element_by_xpath("//button[@data-button='update']")
        save_post_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

    def test_edit_a_post_by_BPC_P2(self):
        origin_data = dict()
        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        new_post_link.click()

        state_span = self.driver.find_element_by_xpath('//div[contains(@class,"has-value")]//*[@class="Select-value-label"]')
        origin_data['state'] = state_span.text
        state_span.click()

        archived_state = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[@aria-label="Archived"]')
        archived_state.click()

        author_div = self.driver.find_element_by_xpath('//*[@for="author"]//*[@class="Select-multi-value-wrapper"]')
        origin_data['author'] = author_div
        author_div.click()

        demo_user_author = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[normalize-space()="Demo User"]')
        demo_user_author.click()

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        origin_data['published_date'] = date_input.get_attribute('value')
        date_input.click()

        next_month_button = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-NavButton--next")]')
        next_month_button.click()

        first_day_in_month = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-Day") and '
                                                               'normalize-space()=1]')
        first_day_in_month.click()

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')


        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_126']//iframe[contains(@id,'keystone-html')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        origin_data['content_brief'] = content_brief.text
        content_brief.send_keys("Radiohead")
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_152']//iframe[contains(@id,'keystone-html')]"))
        content_extended = self.driver.find_element_by_xpath("//*[@id='tinymce']")
        origin_data['content_extended'] = content_extended.text
        content_extended.send_keys("Creep" )
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0,0);")

        reset_changes_button = self.driver.find_element_by_xpath('//*[@data-button="reset"]')
        reset_changes_button.click()

        reset_confirm_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        reset_confirm_button.click()

        state_span = self.driver.find_element_by_xpath(
            '//div[contains(@class,"has-value")]//*[@class="Select-value-label"]')
        self.assertEquals(origin_data['state'], state_span.text)

        author_div = self.driver.find_element_by_xpath('//*[@for="author"]//*[@class="Select-multi-value-wrapper"]')
        self.assertEquals(origin_data['author'], author_div)


        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        self.assertEquals(origin_data['published_date'], date_input.get_attribute('value'))

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_126']//iframe[contains(@id,'keystone-html')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        self.assertEquals(origin_data['content_brief'], content_brief.text)
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(
            self.driver.find_element_by_xpath("//*[@id='mceu_152']//iframe[contains(@id,'keystone-html')]"))
        content_extended = self.driver.find_element_by_xpath("//*[@id='tinymce']")
        self.assertEquals(origin_data['content_extended'], content_extended.text)
        self.driver.switch_to.default_content()

    def test_edit_a_post_by_BPC_P3(self):
        edited_data = dict()
        new_post_link = self.driver.find_element_by_xpath("//a[contains(@class,'ItemList__value')]")
        new_post_link.click()

        state_span = self.driver.find_element_by_xpath('//div[contains(@class,"has-value")]//*[@class="Select-value-label"]')
        state_span.click()

        archived_state = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[@aria-label="Archived"]')
        archived_state.click()

        state_span = self.driver.find_element_by_xpath('//div[contains(@class,"has-value")]//*[@class="Select-value-label"]')
        edited_data['state'] = state_span.text

        author_div = self.driver.find_element_by_xpath('//*[@for="author"]//*[@class="Select-multi-value-wrapper"]')
        author_div.click()


        demo_user_author = self.driver.find_element_by_xpath('//div[@class="Select-menu-outer"]//div[normalize-space()="Demo User"]')
        demo_user_author.click()

        author_div = self.driver.find_element_by_xpath('//*[@for="author"]//*[@class="Select-multi-value-wrapper"]')
        edited_data['author'] = author_div.text

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        date_input.click()

        next_month_button = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-NavButton--next")]')
        next_month_button.click()

        first_day_in_month = self.driver.find_element_by_xpath('//*[contains(@class,"DayPicker-Day") and normalize-space()=1]')
        first_day_in_month.click()

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        edited_data['published_date'] = date_input.get_attribute('value')

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_126']//iframe[contains(@id,'keystone-html')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content_brief.send_keys("Radiohead")
        edited_data['content_brief'] = content_brief.text
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_152']//iframe[contains(@id,'keystone-html')]"))
        content_extended = self.driver.find_element_by_xpath("//*[@id='tinymce']")
        content_extended.send_keys("Creep")
        edited_data['content_extended'] = content_extended.text
        self.driver.switch_to.default_content()

        self.driver.execute_script("window.scrollTo(0,0);")

        reset_changes_button = self.driver.find_element_by_xpath('//*[@data-button="reset"]')
        reset_changes_button.click()

        reset_cancel_button = self.driver.find_element_by_xpath('//*[@data-button-type="cancel"]')
        reset_cancel_button.click()

        state_span = self.driver.find_element_by_xpath(
            '//div[contains(@class,"has-value")]//*[@class="Select-value-label"]')
        self.assertEquals(edited_data['state'], state_span.text)

        author_div = self.driver.find_element_by_xpath('//*[@for="author"]//*[@class="Select-multi-value-wrapper"]')
        self.assertEquals(edited_data['author'], author_div.text)

        date_input = self.driver.find_element_by_xpath('//*[@name="publishedDate"]')
        self.assertEquals(edited_data['published_date'], date_input.get_attribute('value'))


        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id='mceu_126']//iframe[contains(@id,'keystone-html')]"))
        content_brief = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        self.assertEquals(edited_data['content_brief'], content_brief.text)
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(
            self.driver.find_element_by_xpath("//*[@id='mceu_152']//iframe[contains(@id,'keystone-html')]"))
        content_extended = self.driver.find_element_by_xpath("//*[@id='tinymce']")
        self.assertEquals(edited_data['content_extended'], content_extended.text)
        self.driver.switch_to.default_content()

    def tearDown(self) -> None:
        post_list_page_button = self.driver.find_element_by_xpath("//a[contains(@class,'css-dmf4a8')]")
        post_list_page_button.click()

        delete_post_button = self.driver.find_element_by_xpath("//button[contains(@class,'ItemList__control--delete')]")
        delete_post_button.click()

        confirm_delete_post_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
        confirm_delete_post_button.click()

        sign_out_link = self.driver.find_element_by_xpath('//a[@title="Sign Out"]')
        sign_out_link.click()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
