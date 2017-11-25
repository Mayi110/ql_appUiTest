class Swipe():
    def __init__(self,driver):
        self.driver = driver
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