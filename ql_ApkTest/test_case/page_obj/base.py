from selenium.webdriver.support.ui import WebDriverWait
class Page():
    '''基础类用于所有页面的继承'''
    def __init__(self,driver):
        self.driver = driver
        self.timeout = 30
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    #隐式等待定位元素
    def webdriver_element(self,*loc):
        return WebDriverWait(self.driver,20).until(lambda driver:self.find_element(*loc))
    def webdriver_elements(self,*loc):
        return WebDriverWait(self.driver,20).until(lambda driver:self.find_elements(*loc))
    #滑动函数
    def getsize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x,y)
    #向上滑动
    def swipeup(self,t):
        l = self.getsize()
        x = int(l[0]*0.5)
        y1 = int(l[1]*0.8)
        y2 = int(l[1]*0.4)
        return self.driver.swipe(x,y1,x,y2,t)
    #向下滑动
    def swipedown(self,t):
        l = self.getsize()
        x = int(l[0]*0.5)
        y1 = int(l[1]*0.3)
        y2 = int(l[1]*0.8)
        return self.driver.swipe(x,y1,x,y2,t)
    #向左滑动
    def swipeleft(self,t):
        l = self.getsize()
        x1 = int(l[0]*0.8)
        x2 = int(l[0]*0.3)
        y = int(l[1]*0.5)
        return self.driver.swipe(x1,y,x2,y,t)
    #向右滑动
    def swiperight(self,t):
        l = self.getsize()
        x1 = int(l[0]*0.3)
        x2 = int(l[0]*0.8)
        y = int(l[1]*0.5)
        return self.driver.swipe(x1,y,x2,y,t)