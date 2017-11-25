import unittest
from .driver import driver_app

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = driver_app()
        self.driver.implicitly_wait(20)
        #登录操作
    def tearDown(self):
        pass
        #退出登录操作