import unittest
import time
from selenium import webdriver

class TestEditACommment(unittest.TestCase):
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

    def go_to_comments_list_page(self):
        comments_list_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-comments"]')
        comments_list_page_button.click()

    def test_edit_a_comment_by_ECC_TC005_T1(self):
        AUTHOR = None
        POST = "Daredevil"
        STATE = "Draft"
        CONTENT = ""

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()

        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys(POST)

        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        self.go_to_comments_list_page()

        create_comment_button = self.driver.find_element_by_xpath('//*[@class="css-h629qq"]')
        create_comment_button.click()

        if AUTHOR is not None:
            author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select--single')]")
            author_option.click()
            selected_author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select-option') and normalize-space()='%s']" % AUTHOR)
            selected_author_option.click()

        post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select--single')]")
        post_option.click()
        selectd_post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select-option') and normalize-space()='%s']" % POST)
        selectd_post_option.click()

        confrim_create_comment_button = self.driver.find_element_by_xpath("//*[contains(@type,'submit')]")
        confrim_create_comment_button.click()

        time.sleep(1)
        self.driver.refresh()

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        comment_column_item_list[1].click()

        time.sleep(1)
        self.driver.refresh()

        state = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]')
        state.click()
        state_option = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]//*[contains(@class,"Select-option")  and normalize-space()="Draft"]')
        state_option.click()

        PUBLISHED_DATE = self.driver.find_element_by_xpath("//*[@for='publishedOn']//*[contains(@class,'FormField__inner')]").text


        save_button = self.driver.find_element_by_xpath("//*[@data-button='update']")
        save_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        self.assertEquals("" if AUTHOR is None else AUTHOR,comment_column_item_list[2].text)
        self.assertEquals(POST,comment_column_item_list[3].text)

        for element in PUBLISHED_DATE.split(' '):
            self.assertTrue(element in comment_column_item_list[4].text)
        self.assertEquals(STATE,comment_column_item_list[5].text)

        comment_column_item_list[1].click()

        select_item_list_in_comment_edit_page = self.driver.find_elements_by_xpath("//*[contains(@class,'Select--single')]//*[contains(@class,'Select-multi-value-wrapper')]")
        self.assertEquals("Select..." if AUTHOR is None else AUTHOR,select_item_list_in_comment_edit_page[0].text)
        self.assertEquals(POST,select_item_list_in_comment_edit_page[1].text)
        self.assertEquals(STATE,select_item_list_in_comment_edit_page[2].text)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        self.assertEquals(CONTENT,content.text)
        self.driver.switch_to.default_content()

    def test_edit_a_comment_by_ECC_TC005_T2(self):
        AUTHOR = "Demo User"
        POST = "WandaVision"
        STATE = "Published"
        CONTENT = "Vision"

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()

        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys(POST)

        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        self.go_to_comments_list_page()

        create_comment_button = self.driver.find_element_by_xpath('//*[@class="css-h629qq"]')
        create_comment_button.click()

        if AUTHOR is not None:
            author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select--single')]")
            author_option.click()
            selected_author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select-option') and normalize-space()='%s']" % AUTHOR)
            selected_author_option.click()


        post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select--single')]")
        post_option.click()
        selected_post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select-option') and normalize-space()='%s']" % POST)
        selected_post_option.click()

        confrim_create_comment_button = self.driver.find_element_by_xpath("//*[contains(@type,'submit')]")
        confrim_create_comment_button.click()

        time.sleep(1)
        self.driver.refresh()

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        comment_column_item_list[1].click()

        time.sleep(1)
        self.driver.refresh()

        state = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]')
        state.click()
        state_option = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]//*[contains(@class,"Select-option")  and normalize-space()="%s"]' % STATE)
        state_option.click()

        PUBLISHED_DATE = self.driver.find_element_by_xpath("//*[@for='publishedOn']//*[contains(@class,'FormField__inner')]").text

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content.send_keys(CONTENT)
        self.driver.switch_to.default_content()

        save_button = self.driver.find_element_by_xpath("//*[@data-button='update']")
        save_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        self.assertEquals("" if AUTHOR is None else AUTHOR,comment_column_item_list[2].text)
        self.assertEquals(POST,comment_column_item_list[3].text)

        for element in PUBLISHED_DATE.split(' '):
            self.assertTrue(element in comment_column_item_list[4].text)
        self.assertEquals(STATE,comment_column_item_list[5].text)

        comment_column_item_list[1].click()
        select_item_list_in_comment_edit_page = self.driver.find_elements_by_xpath("//*[contains(@class,'Select--single')]//*[contains(@class,'Select-multi-value-wrapper')]")
        self.assertEquals("Select..." if AUTHOR is None else AUTHOR,select_item_list_in_comment_edit_page[0].text)
        self.assertEquals(POST,select_item_list_in_comment_edit_page[1].text)
        self.assertEquals(STATE,select_item_list_in_comment_edit_page[2].text)

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        self.assertEquals(CONTENT,content.text)
        self.driver.switch_to.default_content()

    def test_edit_a_comment_by_ECC_TC005_T3(self):
        AUTHOR = None
        POST = "extenDsssssssssssdsfdsafdfwefwrrrrrStrangerThingsjfAaaaaaaaaaaaaawefaeddsvawedsvwefdwfaaaaaaaaqeqqq"
        STATE = "Archived"
        CONTENT = "extenDsssssssssssdsfdsafdfwefwrrrrrStrangerThingsjfAaaaaaaaaaaaaawefaeddsvawedsvwefdwfaaaaaaaaqeaaa"

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()

        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys(POST)

        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        comments_list_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-comments"]')
        comments_list_page_button.click()

        create_comment_button = self.driver.find_element_by_xpath('//*[@class="css-h629qq"]')
        create_comment_button.click()

        if AUTHOR is not None:
            author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select--single')]")
            author_option.click()
            selected_author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select-option') and normalize-space()='%s']" % AUTHOR)
            selected_author_option.click()


        post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select--single')]")
        post_option.click()
        selected_post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select-option') and normalize-space()='%s']" % POST)
        selected_post_option.click()

        confrim_create_comment_button = self.driver.find_element_by_xpath("//*[contains(@type,'submit')]")
        confrim_create_comment_button.click()

        time.sleep(1)
        self.driver.refresh()

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        comment_column_item_list[1].click()

        time.sleep(1)
        self.driver.refresh()

        state = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]')
        state.click()
        state_option = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]//*[contains(@class,"Select-option")  and normalize-space()="%s"]' % STATE)
        state_option.click()

        PUBLISHED_DATE = self.driver.find_element_by_xpath("//*[@for='publishedOn']//*[contains(@class,'FormField__inner')]").text

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content.send_keys(CONTENT)
        self.driver.switch_to.default_content()

        save_button = self.driver.find_element_by_xpath("//*[@data-button='update']")
        save_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        self.assertEquals("" if AUTHOR is None else AUTHOR,comment_column_item_list[2].text)
        self.assertEquals(POST,comment_column_item_list[3].text)

        for element in PUBLISHED_DATE.split(' '):
            self.assertTrue(element in comment_column_item_list[4].text)
        self.assertEquals(STATE,comment_column_item_list[5].text)

        comment_column_item_list[1].click()
        select_item_list_in_comment_edit_page = self.driver.find_elements_by_xpath("//*[contains(@class,'Select--single')]//*[contains(@class,'Select-multi-value-wrapper')]")
        self.assertEquals("Select..." if AUTHOR is None else AUTHOR,select_item_list_in_comment_edit_page[0].text)
        self.assertEquals(POST,select_item_list_in_comment_edit_page[1].text)
        self.assertEquals(STATE,select_item_list_in_comment_edit_page[2].text)

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        self.assertEquals(CONTENT,content.text)
        self.driver.switch_to.default_content()

    def test_edit_a_comment_by_ECC_TC005_T4(self):
        AUTHOR = None
        POST = "*-/+8#$^&fgfdE6"
        STATE = "Draft"
        CONTENT = "*-/+8#$^&fgfdE6"

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()

        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys(POST)

        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        comments_list_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-comments"]')
        comments_list_page_button.click()

        create_comment_button = self.driver.find_element_by_xpath('//*[@class="css-h629qq"]')
        create_comment_button.click()

        if AUTHOR is not None:
            author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select--single')]")
            author_option.click()
            selected_author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select-option') and normalize-space()='%s']" % AUTHOR)
            selected_author_option.click()


        post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select--single')]")
        post_option.click()
        selected_post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select-option') and normalize-space()='%s']" % POST)
        selected_post_option.click()

        confrim_create_comment_button = self.driver.find_element_by_xpath("//*[contains(@type,'submit')]")
        confrim_create_comment_button.click()

        time.sleep(1)
        self.driver.refresh()

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        comment_column_item_list[1].click()

        time.sleep(1)
        self.driver.refresh()

        state = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]')
        state.click()
        state_option = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]//*[contains(@class,"Select-option")  and normalize-space()="%s"]' % STATE)
        state_option.click()

        PUBLISHED_DATE = self.driver.find_element_by_xpath("//*[@for='publishedOn']//*[contains(@class,'FormField__inner')]").text

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content.send_keys(CONTENT)
        self.driver.switch_to.default_content()

        save_button = self.driver.find_element_by_xpath("//*[@data-button='update']")
        save_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        self.assertEquals("" if AUTHOR is None else AUTHOR,comment_column_item_list[2].text)
        self.assertEquals(POST,comment_column_item_list[3].text)

        for element in PUBLISHED_DATE.split(' '):
            self.assertTrue(element in comment_column_item_list[4].text)
        self.assertEquals(STATE,comment_column_item_list[5].text)

        comment_column_item_list[1].click()
        select_item_list_in_comment_edit_page = self.driver.find_elements_by_xpath("//*[contains(@class,'Select--single')]//*[contains(@class,'Select-multi-value-wrapper')]")
        self.assertEquals("Select..." if AUTHOR is None else AUTHOR,select_item_list_in_comment_edit_page[0].text)
        self.assertEquals(POST,select_item_list_in_comment_edit_page[1].text)
        self.assertEquals(STATE,select_item_list_in_comment_edit_page[2].text)

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        self.assertEquals(CONTENT,content.text)
        self.driver.switch_to.default_content()

    def test_edit_a_comment_by_BPC_TC005_P1(self):
        AUTHOR = "Demo User"
        POST = "*-/+8#$^&fgfdE6"
        STATE = "Draft"
        CONTENT = "*-/+8#$^&fgfdE6"

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()

        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys(POST)

        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        comments_list_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-comments"]')
        comments_list_page_button.click()

        create_comment_button = self.driver.find_element_by_xpath('//*[@class="css-h629qq"]')
        create_comment_button.click()

        if AUTHOR is not None:
            author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select--single')]")
            author_option.click()
            selected_author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select-option') and normalize-space()='%s']" % AUTHOR)
            selected_author_option.click()


        post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select--single')]")
        post_option.click()
        selected_post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select-option') and normalize-space()='%s']" % POST)
        selected_post_option.click()

        confrim_create_comment_button = self.driver.find_element_by_xpath("//*[contains(@type,'submit')]")
        confrim_create_comment_button.click()

        time.sleep(1)
        self.driver.refresh()

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        comment_column_item_list[1].click()

        time.sleep(1)
        self.driver.refresh()

        state = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]')
        state.click()
        state_option = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]//*[contains(@class,"Select-option")  and normalize-space()="%s"]' % STATE)
        state_option.click()

        PUBLISHED_DATE = self.driver.find_element_by_xpath("//*[@for='publishedOn']//*[contains(@class,'FormField__inner')]").text

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        content.send_keys(CONTENT)
        self.driver.switch_to.default_content()

        save_button = self.driver.find_element_by_xpath("//*[@data-button='update']")
        save_button.click()

        success_prompt = self.driver.find_element_by_xpath("//div[@data-alert-type='success']")
        self.assertTrue("Your changes have been saved successfully" in success_prompt.get_attribute('innerHTML').strip())

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        self.assertEquals("" if AUTHOR is None else AUTHOR,comment_column_item_list[2].text)
        self.assertEquals(POST,comment_column_item_list[3].text)

        for element in PUBLISHED_DATE.split(' '):
            self.assertTrue(element in comment_column_item_list[4].text)
        self.assertEquals(STATE,comment_column_item_list[5].text)

        comment_column_item_list[1].click()
        select_item_list_in_comment_edit_page = self.driver.find_elements_by_xpath("//*[contains(@class,'Select--single')]//*[contains(@class,'Select-multi-value-wrapper')]")
        self.assertEquals("Select..." if AUTHOR is None else AUTHOR,select_item_list_in_comment_edit_page[0].text)
        self.assertEquals(POST,select_item_list_in_comment_edit_page[1].text)
        self.assertEquals(STATE,select_item_list_in_comment_edit_page[2].text)

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        self.assertEquals(CONTENT,content.text)
        self.driver.switch_to.default_content()

    def test_edit_a_comment_by_BPC_TC005_P2(self):
        AUTHOR = "Demo User"
        POST = "*-/+8#$^&fgfdE6"
        STATE = "Draft"
        CONTENT = "*-/+8#$^&fgfdE6"

        posts_page_button = self.driver.find_element_by_xpath("//a[normalize-space()='Posts']")
        posts_page_button.click()

        create_post_button = self.driver.find_element_by_xpath("//button[@data-e2e-list-create-button='no-results']")
        create_post_button.click()

        input_post_title = self.driver.find_element_by_xpath("//input[@class='css-foh633']")
        input_post_title.send_keys(POST)

        create_button = self.driver.find_element_by_xpath("//button[normalize-space()='Create']")
        create_button.click()

        comments_list_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-comments"]')
        comments_list_page_button.click()

        create_comment_button = self.driver.find_element_by_xpath('//*[@class="css-h629qq"]')
        create_comment_button.click()

        if AUTHOR is not None:
            author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select--single')]")
            author_option.click()
            selected_author_option = self.driver.find_element_by_xpath("//*[@for='author']//*[contains(@class,'Select-option') and normalize-space()='%s']" % AUTHOR)
            selected_author_option.click()


        post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select--single')]")
        post_option.click()
        selected_post_option = self.driver.find_element_by_xpath("//*[@for='post']//*[contains(@class,'Select-option') and normalize-space()='%s']" % POST)
        selected_post_option.click()

        confrim_create_comment_button = self.driver.find_element_by_xpath("//*[contains(@type,'submit')]")
        confrim_create_comment_button.click()

        time.sleep(1)
        self.driver.refresh()

        self.go_to_comments_list_page()

        comment_column_item_list = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        comment_column_item_list[1].click()

        time.sleep(1)
        self.driver.refresh()

        author = self.driver.find_element_by_xpath('//*[@for="author"]//*[contains(@class,"Select-multi-value-wrapper")]')
        AUTHOR_BEFROE_EDIT = author.text

        post = self.driver.find_element_by_xpath('//*[@for="post"]//*[contains(@class,"Select-multi-value-wrapper")]')
        POST_BEFROE_EDIT = post.text


        state = self.driver.find_element_by_xpath('//*[@for="commentState"]//*[contains(@class,"Select-multi-value-wrapper")]')
        STATE_BEFROE_EDIT = state.text
        state.click()
        state_option = self.driver.find_element_by_xpath('//*[@for="commentState"]//div[contains(@class,"has-value")]//*[contains(@class,"Select-option")  and normalize-space()="%s"]' % STATE)
        state_option.click()

        PUBLISHED_DATE = self.driver.find_element_by_xpath("//*[@for='publishedOn']//*[contains(@class,'FormField__inner')]").text

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        CONTENT_BEFORE_EDIT = content.text
        content.send_keys(CONTENT)
        self.driver.switch_to.default_content()

        reset_changes_button = self.driver.find_element_by_xpath("//*[@data-button='reset']")
        reset_changes_button.click()
        confirm_reset_changes_button = self.driver.find_element_by_xpath("//*[@data-button-type='confirm']")
        confirm_reset_changes_button.click()

        author = self.driver.find_element_by_xpath('//*[@for="author"]//*[contains(@class,"Select-multi-value-wrapper")]')
        self.assertEquals(AUTHOR_BEFROE_EDIT, author.text)

        post = self.driver.find_element_by_xpath('//*[@for="post"]//*[contains(@class,"Select-multi-value-wrapper")]')
        self.assertEquals(POST_BEFROE_EDIT, post.text)

        state = self.driver.find_element_by_xpath('//*[@for="commentState"]//*[contains(@class,"Select-multi-value-wrapper")]')
        self.assertEquals(STATE_BEFROE_EDIT, state.text)

        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'keystone-html')]"))
        content = self.driver.find_element_by_xpath("//*[contains(@class,'mce-content-body')]")
        self.assertEquals(CONTENT_BEFORE_EDIT,content.text)
        self.driver.switch_to.default_content()

    def tearDown(self) -> None:
        comments_list_page_button = self.driver.find_element_by_xpath('//*[@data-list-path="post-comments"]')
        comments_list_page_button.click()

        comment_itmes = self.driver.find_elements_by_xpath("//*[contains(@class,'ItemList__col')]")
        if len(comment_itmes) is not 0:
            delete_comment_button = self.driver.find_element_by_xpath("//button[contains(@class,'ItemList__control--delete')]")
            delete_comment_button.click()

            confirm_delete_comment_button = self.driver.find_element_by_xpath('//*[@data-button-type="confirm"]')
            confirm_delete_comment_button.click()

        post_list_page_button = self.driver.find_element_by_xpath("//*[@data-list-path='posts']")
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
