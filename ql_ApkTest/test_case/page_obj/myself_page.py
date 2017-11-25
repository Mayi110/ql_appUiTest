from .base import Page
from selenium.webdriver.common.by import By

class Myself(Page):
    '''我的页面'''
    #修改用户名
    name_loc = (By.ID,"com.thinkwu.live:id/name")
    name2_loc = (By.ID,"com.thinkwu.live:id/rlName")
    dele_name2_loc = (By.ID,"com.thinkwu.live:id/ivDelete")
    input_name_loc = (By.ID,"com.thinkwu.live:id/etUserName")
    btn_issue_loc = (By.ID,"com.thinkwu.live:id/btn_issue")
    ivback_loc = (By.ID,"com.thinkwu.live:id/iv_back")

    #修改用户名，返回我的页面
    def rename(self,name):
        self.webdriver_element(*self.name_loc).click()
        self.webdriver_element(*self.name2_loc).click()
        self.webdriver_element(*self.dele_name2_loc).click()
        self.webdriver_element(*self.input_name_loc).send_keys(name)
        self.webdriver_element(*self.btn_issue_loc).click()
        self.webdriver_element(*self.ivback_loc).click()
    #获取修改后用户名
    def get_rename(self):
        return self.webdriver_element(*self.name_loc).text

    #修改头像
    head_loc = (By.ID,"com.thinkwu.live:id/head")
    rlHeader_loc = (By.ID,"com.thinkwu.live:id/rlHeader")
    openPhones_loc = (By.ID,"com.thinkwu.live:id/openPhones")
    def change_head(self):
        self.webdriver_element(*self.head_loc).click()
        self.webdriver_element(*self.rlHeader_loc).click()
        self.webdriver_element(*self.openPhones_loc).click()
        #下面需要从安卓本地上传图片APP
        #。。。。。。
        #。。。。。。

    myself_buttons_loc = (By.ID,"com.thinkwu.live:id/title")
    #进入直播间主页
    def enter_live_room(self):
        return self.webdriver_elements(*self.myself_buttons_loc)[0].click()
    #进入直播间后台
    def enter_live_background(self):
        return self.webdriver_elements(*self.myself_buttons_loc)[1].click()
    #进入我的下载
    def enter_mydownload(self):
        return self.webdriver_elements(*self.myself_buttons_loc)[2].click()
    #进入我的收藏
    def enter_mycollections(self):
        return self.webdriver_elements(*self.myself_buttons_loc)[3].click()
    #进入关注的直播间
    def enter_like_lives(self):
        return self.webdriver_elements(*self.myself_buttons_loc)[4].click()
    #进入看过的直播间
    def enter_looked_lives(self):
        return self.webdriver_elements(*self.myself_buttons_loc)[5].click()
    #进入我的钱包
    def enter_mymoney_packet(self):
        self.swipeup(800)
        return self.webdriver_elements(*self.myself_buttons_loc)[-3].click()
    #进入分销推广
    def enter_distribution(self):
        self.swipeup(800)
        return self.webdriver_elements(*self.myself_buttons_loc)[-2].click()
    #进入设置页面
    def enter_setting(self):
        self.swipeup(800)
        return self.webdriver_elements(*self.myself_buttons_loc)[-1].click()
