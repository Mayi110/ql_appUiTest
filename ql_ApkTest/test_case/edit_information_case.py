import unittest
from modles.function import insert_img
from modles.driver import driver_app
from page_obj.login_page import Login
from page_obj.myself_page import Myself

class Edit_information(unittest.TestCase):
    """我的-修改用户名"""
    def setUp(self):
        self.driver = driver_app()
        self.driver.implicitly_wait(10)
        self.login = Login(self.driver)
        #登录，切换到“我的”页面
        #self.login.loginin()
        self.login.enter_myself()
        self.myself = Myself(self.driver)
    def tearDown(self):
        #退出登录
        #self.login.loginout()
        self.driver.quit()
    def test_rename1(self):
        """修改用户名"""
        self.myself.rename(name="测试用户名")
        insert_img(self.driver,"rename.jpg")
        self.assertEqual(self.myself.get_rename(),"测试用户名")
        #将用户名改回来
        self.myself.rename(name='右右')
    def test_change_head(self):
        """修改用户头像"""
        pass

if __name__ == "__main__":
    unittest.main()