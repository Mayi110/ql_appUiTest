from .driver import driver_app
import os

def insert_img(driver,file_name):
    base_dir = os.path.dirname(__file__)
    base_dir = str(base_dir)
    base_dir = base_dir.replace("\\","/")
    base = base_dir.split("/test_case/modles")[0]
    file_path = base + "/test_report/image/" + file_name
    driver.get_screenshot_as_file(file_path)
if __name__ == "__main__":
    import time
    driver = driver_app()
    time.sleep(5)
    insert_img(driver,"test.jpg")
    driver.quit()