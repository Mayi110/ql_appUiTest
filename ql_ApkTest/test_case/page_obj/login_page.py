from .base import Page
from selenium.webdriver.common.by import By

class Login(Page):
    '''登录页面'''
    #登录页面
    more_loc = (By.ID,"com.thinkwu.live:id/login_for_phone_number")
    phone_login_loc = (By.ID,"com.thinkwu.live:id/btn_phone_login")
    username_loc = (By.ID,"com.thinkwu.live:id/et_phone_number")
    password_loc = (By.ID,"com.thinkwu.live:id/et_password")
    login_button_loc = (By.ID,"com.thinkwu.live:id/btn_login")
    phone_login_text_loc = (By.ID,"com.thinkwu.live:id/text_title")
    def click_more(self):
        return self.webdriver_element(*self.more_loc).click()
    def phone_login(self):
        return self.webdriver_element(*self.phone_login_loc).click()
    def username(self,username):
        return self.webdriver_element(*self.username_loc).send_keys(username)
    def password(self,password):
        return self.webdriver_element(*self.password_loc).send_keys(password)
    def login_button(self):
        return self.webdriver_element(*self.login_button_loc).click()
    def phone_login_text(self):
        return self.webdriver_element(*self.phone_login_text_loc).text
    #进入登录页面
    def login_page(self):
        self.click_more()
        self.phone_login()
    #登录函数
    def loginin(self,username="18819157687",password="123456789"):
        self.click_more()
        self.phone_login()
        self.username(username)
        self.password(password)
        self.login_button()
    #切换到“我的”页面
    my_loc = (By.ID,"com.thinkwu.live:id/bottom_bar_my")
    name_loc = (By.ID,"com.thinkwu.live:id/name")
    #切换到“我的”页面
    def enter_myself(self):
        return self.webdriver_element(*self.my_loc).click()
    #获取登录用户名
    def name(self):
        self.webdriver_element(*self.my_loc).click()
        return self.webdriver_element(*self.name_loc).text
    #退出登录
    setting_loc = (By.ID,"com.thinkwu.live:id/title")
    quit_loc = (By.ID,"com.thinkwu.live:id/rl_exit")
    ensure_quit_loc = (By.ID,"com.thinkwu.live:id/issue")
    #退出函数
    def loginout(self):
        self.swipeup(800)
        self.webdriver_elements(*self.setting_loc)[-1].click()
        self.webdriver_element(*self.quit_loc).click()
        self.webdriver_element(*self.ensure_quit_loc).click()