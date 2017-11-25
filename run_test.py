'''
author= "liyue"
date = "2017-07-16"
生成测试报告、发送邮件；首先需要修改HTMLTestRunner.py模块，放到Lib目录下
'''
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import os ,time ,unittest,smtplib

####################定义邮件######################
def send_mail(file_new):
    f = open(file_new,"rb")
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,"html","utf-8")
    msg['Subject'] = Header("千聊apk自动化测试报告","utf-8")

    msg['from'] = "test0_test1@126.com"
    msg['to'] = "1048355336@qq.com"
    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("test0_test1@126.com","Li123456")
    smtp.sendmail("test0_test1@126.com","1048355336@qq.com",msg.as_string())
    smtp.quit()
    print("已经发送测试报告。")

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn : os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return  file_new
if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = "./qianliao_app_Apk/test_report/" + now + "_result.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,
                            title="千聊apk自动化测试报告",
                            description="环境：Android4.4；appium1.4.3"
                            )
    discover = unittest.defaultTestLoader.discover("./qianliao_app_Apk/test_case",
                                                   pattern="*_case.py"
                                                   )
    runner.run(discover)
    fp.close()
    file_path = new_report("./qianliao_app_Apk/test_report")
    send_mail(file_path)