import unittest
from modles.function import insert_img
from modles.driver import driver_app
from page_obj.login_page import Login
from page_obj.myself_page import Myself
from page_obj.live_home_page import Live_home
from time import sleep

class New_topic(unittest.TestCase):
    """新建话题测试"""
    def setUp(self):
        self.driver = driver_app()
        self.driver.implicitly_wait(10)
        self.login = Login(self.driver)
        self.myself = Myself(self.driver)
        self.live_home = Live_home(self.driver)
        #self.login.loginin()
        self.login.enter_myself()
        #进入直播间主页
        self.myself.enter_live_room()

    def tearDown(self):
        #self.live_home.back_myself()
        #退出登录
        #self.login.loginout()
        self.driver.quit()
    def test_new_topic_rbDiscussion1(self):
        """新建讲座形式免费,开启介绍页的话题"""
        self.live_home.new_topic_rbDiscussion1()
        sleep(1)
        insert_img(self.driver,"讲座形式免费话题-开启介绍页.jpg")
        #断言
        self.assertEqual(self.live_home.get_topic_name(),"讲座形式免费话题-开启介绍页")
        self.live_home.topic_back()
    def test_new_topic_rbDiscussion2(self):
        """新建讲座形式免费,关闭介绍页的话题"""
        self.live_home.new_topic_rbDiscussion2()
        sleep(1)
        insert_img(self.driver,"讲座形式免费话题-关闭介绍页.jpg")
        #断言
        self.assertEqual(self.live_home.get_topic_name2(),"讲座形式免费话题-关闭介绍页")
        self.live_home.topic_back()
    def test_new_topic_rbDiscussion_pwd(self):
        """新建讲座形式加密话题,开启介绍页"""
        self.live_home.new_topic_rbDiscussion_pwd()
        sleep(1)
        insert_img(self.driver,"讲座形式加密话题-开启介绍页.jpg")
        #断言
        self.assertSequenceEqual(self.live_home.get_topic_name_pwd(),"讲座形式加密话题-开启介绍页")
        self.live_home.topic_back()
    def test_new_topic_rbDiscussion_money(self):
        """新建讲座形式收费话题,开启介绍页"""
        self.live_home.new_topic_rbDiscussion_money()
        sleep(1)
        insert_img(self.driver,"讲座形式收费话题,开启介绍页.jpg")
        #断言
        self.assertEqual(self.live_home.get_topic_name_money(),"讲座形式收费话题,开启介绍页")
        self.live_home.topic_back()
    def test_new_topic_ppt_free1(self):
        """新建PPT形式免费话题,开启介绍页"""
        self.live_home.new_topic_ppt_free1()
        sleep(1)
        insert_img(self.driver,"PPT形式免费话题,开启介绍页.jpg")
        #断言
        self.assertEqual(self.live_home.get_topic_name_ppt_free1(),"PPT形式免费话题,开启介绍页")
        self.live_home.topic_back()
    def test_new_topic_ppt_free2(self):
        """新建PPT形式免费话题，关闭介绍页"""
        self.live_home.new_topic_ppt_free2()
        sleep(1)
        insert_img(self.driver,"PPT形式免费话题，关闭介绍页.jpg")
        #断言
        self.assertEqual(self.live_home.get_topic_name_ppt_free2(),"PPT形式免费话题,关闭介绍页")
        self.live_home.topic_back()
    def test_new_topic_ppt_pwd(self):
        """新建PPT形式加密话题，开启介绍页"""
        self.live_home.new_topic_ppt_pwd()
        sleep(1)
        insert_img(self.driver,"新建PPT形式加密话题，开启介绍页.jpg")
        #断言
        self.assertEqual(self.live_home.get_topic_name_ppt_pwd(),"PPT形式加密话题,开启介绍页")
        self.live_home.topic_back()
    def test_new_topic_ppt_money(self):
        """新建PPT形式收费话题，开启介绍页"""
        self.live_home.new_topic_ppt_money()
        sleep(1)
        insert_img(self.driver,"PPT形式收费话题，开启介绍页.jpg")
        #断言
        self.assertEqual(self.live_home.get_topic_name_ppt_money(),"PPT形式收费话题，开启介绍页")
if __name__ == "__main__":
    unittest.main()