from appium import webdriver

def driver_app(platformVersion='22',deviceName="7N3HPX159H051514",udid="7N3HPX159H051514"):
    desire_caps = {}
    desire_caps['platformName'] = "Android"
    desire_caps['platformVersion'] = platformVersion
    desire_caps['deviceName'] = deviceName
    desire_caps['udid'] = udid
    desire_caps['appPackage'] = 'com.thinkwu.live'
    desire_caps['appActivity'] = '.ui.activity.InitActivity'
    #desire_caps['appWaitActivity']='.ui.activity.InitActivity'
    desire_caps['unicodeKeyboard'] = "True"
    desire_caps['resetKeyboard'] = "True"
    desire_caps['newCommandTimeout'] = "60"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_caps)
    return driver

if __name__ == "__main__":
    import time
    driver = driver_app(platformVersion="22")
    time.sleep(5)
    driver.quit()
