import unittest
from modles.function import insert_img
from modles.driver import driver_app
from page_obj.login_page import Login
from page_obj.myself_page import Myself
from page_obj.live_home_page import Live_home
from time import sleep

class New_channel(unittest.TestCase):
    """新建系列课测试"""
    def setUp(self):
        self.driver = driver_app()
        self.login = Login(self.driver)
        self.myself = Myself(self.driver)
        self.live_home = Live_home(self.driver)
        #切换到个人中心-》进入直播间主页页面
        self.login.enter_myself()
        self.myself.enter_live_room()
    def tearDown(self):
        self.driver.quit()
    def test_new_channel_free(self):
        """新建免费系列课"""
        self.live_home.new_channel_free()
        sleep(1)
        insert_img(self.driver,"免费系列课.jpg")
        #断言
        self.assertEqual(self.live_home.get_channel_name_free(),"免费系列课")
    def test_new_channel_fix(self):
        """新建固定收费系列课"""
        self.live_home.new_channel_fix()
        sleep(1)
        insert_img(self.driver,"固定收费系列课.jpg")
        #断言
        self.assertEqual(self.live_home.get_channel_name_fix_money(),"固定收费系列课")
    def test_new_channel_ontime(self):
        """新建按时收费系列课"""
        self.live_home.new_channel_ontime()
        sleep(1)
        insert_img(self.driver,"按时收费系列课.jpg")
        #断言
        self.assertEqual(self.live_home.get_channel_name_ontime(),"按时收费系列课")
if __name__ == "__main__":
    unittest.main()