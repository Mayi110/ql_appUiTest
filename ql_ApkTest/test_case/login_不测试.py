import unittest
from time import sleep
from modles.function import insert_img
from modles.driver import driver_app
from modles import myunit
from page_obj.login_page import Login

class Login_test(unittest.TestCase):
    """登录页面"""
    def setUp(self):
        self.driver = driver_app()
        self.driver.implicitly_wait(10)
        self.login = Login(self.driver)
    def tearDown(self):
        self.driver.quit()
    def login_verify(self,username="",password=""):
        self.login.loginin(username,password)
    def test_login_success(self):
        '''登录成功'''
        self.login_verify(username="18819157687",password="123456789")
        self.assertEqual(self.login.name(),"右右")
        insert_img(self.driver,"login_success.jpg")
        #退出登录
        self.login.loginout()
    def test_login_pwderr(self):
        """用户名正确，密码错误"""
        self.login_verify(username="18819157687",password="1234ddsd")
        insert_img(self.driver,"login_pwderr.jpg")
        self.assertEqual(self.login.phone_login_text(),"手机号码登录")
    def test_login_usernameerr(self):
        """用户名错误，密码正确"""
        self.login_verify(username="18888888888",password="123456789")
        insert_img(self.driver,"login_usernameerr.jpg")
        self.assertEqual(self.login.phone_login_text(),"手机号码登录")


if __name__ == "__main__":
    unittest.main()