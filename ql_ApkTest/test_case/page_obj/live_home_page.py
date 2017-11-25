from .base import Page
from selenium.webdriver.common.by import By

class Live_home(Page):
    '''直播间主页'''
    ################################新建话题#################################
    new_topic_loc = (By.ID,"com.thinkwu.live:id/btn_new_topic")
    #直播主题
    live_name_loc = (By.ID,"com.thinkwu.live:id/etName")
    #直播开始时间
    live_start_time_loc = (By.ID,"com.thinkwu.live:id/text_time")
    live_start_time_year_loc = (By.ID,"com.thinkwu.live:id/year")
    live_start_time_month_loc = (By.ID,"com.thinkwu.live:id/month")
    live_start_time_day_loc = (By.ID,"com.thinkwu.live:id/day")
    live_start_time_hour_loc = (By.ID,"com.thinkwu.live:id/hour")
    live_start_time_min_loc = (By.ID,"com.thinkwu.live:id/min")
    #确认选择
    live_start_time_submit_loc = (By.ID,"com.thinkwu.live:id/btnSubmit")
    #直播形式
    live_style_ppt_loc = (By.ID,"com.thinkwu.live:id/rbPPT")
    #下一步
    next_step_loc = (By.ID,"com.thinkwu.live:id/text_next")
    #直播类型
    live_pwd_loc = (By.ID,"com.thinkwu.live:id/image_live_pwd")
    live_pwd_edit_loc = (By.ID,"com.thinkwu.live:id/edit_gd_pwd")
    live_money_loc = (By.ID,"com.thinkwu.live:id/image_live_money")
    live_money_edit_loc = (By.ID,"com.thinkwu.live:id/edit_money")
    #开启介绍页
    public_switch_loc = (By.ID,"com.thinkwu.live:id/public_switch")
    #完成
    btn_finish_loc = (By.ID,"com.thinkwu.live:id/btn_finish")
    #新建成功的话题名称
    topic_title_loc = (By.ID,"com.thinkwu.live:id/toolbar_title")

    #返回个人中心按钮
    back_mysel_loc = (By.ID,"com.thinkwu.live:id/ivBack")
    def back_myself(self):
        return self.webdriver_element(*self.back_mysel_loc).click()
    #####################新建讲座形式免费话题,开启介绍页############################

    def new_topic_rbDiscussion1(self,live_name="讲座形式免费话题-开启介绍页" ):
        self.webdriver_element(*self.new_topic_loc).click()
        self.webdriver_element(*self.live_name_loc).send_keys(live_name)
        #输入开始时间
        #点击打开popupwindow
        self.webdriver_element(*self.live_start_time_loc).click()
        self.webdriver_element(*self.live_start_time_min_loc).click()
        self.driver.swipe(660,1120,660,1020)
        self.webdriver_element(*self.live_start_time_submit_loc).click()
        self.webdriver_element(*self.next_step_loc).click()
        #开启介绍页
        self.webdriver_element(*self.public_switch_loc).click()
        self.webdriver_element(*self.btn_finish_loc).click()
    #断言是否新建成功
    topic_name_loc = (By.ID,"com.thinkwu.live:id/tv_topic_name")
    def get_topic_name(self):
        return self.webdriver_element(*self.topic_name_loc).text
    #返回直播间主页
    topic_back_loc = (By.ID,"com.thinkwu.live:id/btn_back")
    def topic_back(self):
        self.webdriver_element(*self.topic_back_loc).click()
    ##################### 新建讲座形式免费话题,关闭介绍页###########################
    def new_topic_rbDiscussion2(self,live_name="讲座形式免费话题-关闭介绍页"):
        self.webdriver_element(*self.new_topic_loc).click()
        self.webdriver_element(*self.live_name_loc).send_keys(live_name)
        self.webdriver_element(*self.live_start_time_loc).click()
        self.webdriver_element(*self.live_start_time_hour_loc).click()
        self.driver.swipe(550,1110,550,1030)
        self.webdriver_element(*self.live_start_time_submit_loc).click()
        self.webdriver_element(*self.next_step_loc).click()
        self.webdriver_element(*self.btn_finish_loc).click()
    #断言是否新建成功
    topic_name2_loc = (By.ID,"com.thinkwu.live:id/toolbar_title")
    def get_topic_name2(self):
        return self.webdriver_element(*self.topic_name2_loc).text
    ####################### 新建讲座形式加密话题,开启介绍页########################
    def new_topic_rbDiscussion_pwd(self,live_name="讲座形式加密话题-开启介绍页"):
        self.webdriver_element(*self.new_topic_loc).click()
        self.webdriver_element(*self.live_name_loc).send_keys(live_name)
        self.webdriver_element(*self.live_start_time_loc).click()
        self.webdriver_element(*self.live_start_time_min_loc).click()
        self.driver.swipe(660,1120,660,1020)
        self.webdriver_element(*self.live_start_time_submit_loc).click()
        self.webdriver_element(*self.next_step_loc).click()
        self.webdriver_element(*self.live_pwd_loc).click()
        self.webdriver_element(*self.live_pwd_edit_loc).send_keys("123456")
        self.webdriver_element(*self.btn_finish_loc).click()
    #断言是否成功
    def get_topic_name_pwd(self):
        return self.webdriver_element(*self.topic_name_loc).text
    ###################### 新建讲座形式收费话题,开启介绍页#############################
    def new_topic_rbDiscussion_money(self,live_name="讲座形式收费话题,开启介绍页"):
        self.webdriver_element(*self.new_topic_loc).click()
        self.webdriver_element(*self.live_name_loc).send_keys(live_name)
        self.webdriver_element(*self.live_start_time_loc).click()
        self.webdriver_element(*self.live_start_time_min_loc).click()
        self.driver.swipe(660,1120,660,1020)
        self.webdriver_element(*self.live_start_time_submit_loc).click()
        self.webdriver_element(*self.next_step_loc).click()
        self.webdriver_element(*self.live_money_loc).click()
        self.webdriver_element(*self.live_money_edit_loc).send_keys("1")
        self.webdriver_element(*self.btn_finish_loc).click()
    #断言
    def get_topic_name_money(self):
        return self.webdriver_element(*self.topic_name_loc).text
    #####################新建PPT形式免费话题,开启介绍页##############################
    def new_topic_ppt_free1(self,live_name="PPT形式免费话题,开启介绍页"):
        self.webdriver_element(*self.new_topic_loc).click()
        self.webdriver_element(*self.live_name_loc).send_keys(live_name)
        self.webdriver_element(*self.live_start_time_loc).click()
        self.webdriver_element(*self.live_start_time_min_loc).click()
        self.driver.swipe(660,1120,660,1020)
        self.webdriver_element(*self.live_start_time_submit_loc).click()
        self.webdriver_element(*self.live_style_ppt_loc).click()
        self.webdriver_element(*self.next_step_loc).click()
        self.webdriver_element(*self.public_switch_loc).click()
        self.webdriver_element(*self.btn_finish_loc).click()
    #断言
    def get_topic_name_ppt_free1(self):
        return self.webdriver_element(*self.topic_name_loc).text

    #####################新建PPT形式免费话题,关闭介绍页##############################
    def new_topic_ppt_free2(self,live_name="PPT形式免费话题,关闭介绍页"):
        self.webdriver_element(*self.new_topic_loc).click()
        self.webdriver_element(*self.live_name_loc).send_keys(live_name)
        self.webdriver_element(*self.live_start_time_loc).click()
        self.webdriver_element(*self.live_start_time_min_loc).click()
        self.driver.swipe(660,1120,660,1020)
        self.webdriver_element(*self.live_start_time_submit_loc).click()
        self.webdriver_element(*self.live_style_ppt_loc).click()
        self.webdriver_element(*self.next_step_loc).click()
        self.webdriver_element(*self.btn_finish_loc).click()
    #断言
    def get_topic_name_ppt_free2(self):
        return self.webdriver_element(*self.topic_name2_loc).text
    #####################新建PPT形式加密话题,开启介绍页##############################
    def new_topic_ppt_pwd(self,live_name="PPT形式加密话题,开启介绍页"):
        self.webdriver_element(*self.new_topic_loc).click()
        self.webdriver_element(*self.live_name_loc).send_keys(live_name)
        self.webdriver_element(*self.live_start_time_loc).click()
        self.webdriver_element(*self.live_start_time_min_loc).click()
        self.driver.swipe(660,1120,660,1020)
        self.webdriver_element(*self.live_start_time_submit_loc).click()
        self.webdriver_element(*self.live_style_ppt_loc).click()
        self.webdriver_element(*self.next_step_loc).click()
        self.webdriver_element(*self.live_pwd_loc).click()
        self.webdriver_element(*self.live_pwd_edit_loc).send_keys("123456")
        self.webdriver_element(*self.btn_finish_loc).click()
    #断言
    def get_topic_name_ppt_pwd(self):
        return self.webdriver_element(*self.topic_name_loc).text
    #####################新建PPT形式加收费题,开启介绍页##############################
    def new_topic_ppt_money(self,live_name="PPT形式收费话题，开启介绍页"):
        self.webdriver_element(*self.new_topic_loc).click()
        self.webdriver_element(*self.live_name_loc).send_keys(live_name)
        self.webdriver_element(*self.live_start_time_loc).click()
        self.webdriver_element(*self.live_start_time_hour_loc).click()
        self.driver.swipe(660,1120,660,1020)
        self.webdriver_element(*self.live_start_time_submit_loc).click()
        self.webdriver_element(*self.live_style_ppt_loc).click()
        self.webdriver_element(*self.next_step_loc).click()
        self.webdriver_element(*self.live_money_loc).click()
        self.webdriver_element(*self.live_money_edit_loc).send_keys("1")
        self.webdriver_element(*self.btn_finish_loc).click()
    #断言
    def get_topic_name_ppt_money(self):
        return self.webdriver_element(*self.topic_name_loc).text


    ###########################新建系列课#################################
    new_channel_loc = (By.ID,"com.thinkwu.live:id/btn_new_channel")
    #系列课名称
    channel_name_loc = (By.ID,"com.thinkwu.live:id/rlChannelName")
    enter_channel_name_loc = (By.ID,"com.thinkwu.live:id/live_topic")
    submit_channel_name_loc = (By.ID,"com.thinkwu.live:id/issue")
    #排课计划
    queuecourse_loc = (By.ID,"com.thinkwu.live:id/rlQueueCourse")
    enter_queuecourse_loc = (By.ID,"com.thinkwu.live:id/edit")
    submit_queuecourse_loc = (By.ID,"com.thinkwu.live:id/ok")
    #系列课分类
    channel_classify_loc = (By.ID,"com.thinkwu.live:id/rlChannelClassify")
    submit_channel_classify_loc = (By.ID,"com.thinkwu.live:id/btn_commit")
    #选择收费方式
    fix_loc = (By.ID,"com.thinkwu.live:id/rbFix")
    fix_momey_loc = (By.ID,"com.thinkwu.live:id/etFixMoney")
    submit_fix_money_loc = (By.ID,"com.thinkwu.live:id/btnSubmit")
    ontime_loc = (By.ID,"com.thinkwu.live:id/rbOnTime")
    month_loc = (By.ID,"com.thinkwu.live:id/etMonthNum")
    money_loc =(By.ID,"com.thinkwu.live:id/etMoney")
    submit_ontime_loc = (By.ID,"com.thinkwu.live:id/btnSubmit")
    #确定
    submit_loc = (By.ID,"com.thinkwu.live:id/btnSubmit")
             ##############新建免费系列课################
    def new_channel_free(self,channel_name="免费系列课",queuecourse="5"):
        self.webdriver_element(*self.new_channel_loc).click()
        self.webdriver_element(*self.channel_name_loc).click()
        self.webdriver_element(*self.enter_channel_name_loc).send_keys(channel_name)
        self.webdriver_element(*self.submit_channel_name_loc).click()
        self.webdriver_element(*self.queuecourse_loc).click()
        self.webdriver_element(*self.enter_queuecourse_loc).send_keys(queuecourse)
        self.webdriver_element(*self.submit_queuecourse_loc).click()
        self.webdriver_element(*self.channel_classify_loc).click()
        self.webdriver_element(*self.submit_channel_classify_loc).click()
        self.webdriver_element(*self.fix_loc).click()
        self.webdriver_element(*self.fix_momey_loc).send_keys("0")
        self.webdriver_element(*self.submit_fix_money_loc).click()
        self.webdriver_element(*self.submit_loc).click()
    #断言
    get_channel_name_loc = (By.ID,"com.thinkwu.live:id/channel_name")
    def get_channel_name_free(self):
        return self.webdriver_element(*self.get_channel_name_loc).text
                ###################新建固定收费系列课####################
    def new_channel_fix(self,channel_name="固定收费系列课"):
        self.webdriver_element(*self.new_channel_loc).click()
        self.webdriver_element(*self.channel_name_loc).click()
        self.webdriver_element(*self.enter_channel_name_loc).send_keys(channel_name)
        self.webdriver_element(*self.submit_channel_name_loc).click()
        self.webdriver_element(*self.queuecourse_loc).click()
        self.webdriver_element(*self.enter_queuecourse_loc).send_keys("5")
        self.webdriver_element(*self.submit_queuecourse_loc).click()
        self.webdriver_element(*self.channel_classify_loc).click()
        self.webdriver_element(*self.submit_channel_classify_loc).click()
        self.webdriver_element(*self.fix_loc).click()
        self.webdriver_element(*self.fix_momey_loc).send_keys("1")
        self.webdriver_element(*self.submit_fix_money_loc).click()
        self.webdriver_element(*self.submit_loc).click()
    #断言
    def get_channel_name_fix_money(self):
        return self.webdriver_element(*self.get_channel_name_loc).text
        ###################新建按时收费系列课####################
    def new_channel_ontime(self,channel_name="按时收费系列课"):
        self.webdriver_element(*self.new_channel_loc).click()
        self.webdriver_element(*self.channel_name_loc).click()
        self.webdriver_element(*self.enter_channel_name_loc).send_keys(channel_name)
        self.webdriver_element(*self.submit_channel_name_loc).click()
        self.webdriver_element(*self.queuecourse_loc).click()
        self.webdriver_element(*self.enter_queuecourse_loc).send_keys("5")
        self.webdriver_element(*self.submit_queuecourse_loc).click()
        self.webdriver_element(*self.channel_classify_loc).click()
        self.webdriver_element(*self.submit_channel_classify_loc).click()
        self.webdriver_element(*self.ontime_loc).click()
        self.webdriver_element(*self.month_loc).send_keys("1")
        self.webdriver_element(*self.money_loc).send_keys("1")
        self.webdriver_element(*self.submit_ontime_loc).click()
        self.webdriver_element(*self.submit_loc).click()
    #断言
    def get_channel_name_ontime(self):
        return self.webdriver_element(*self.get_channel_name_loc).text
