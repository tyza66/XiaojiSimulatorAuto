#by:洮羱芝闇 appium范例 小鸡模拟器启动fc游戏文件夹下第一个游戏
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

info={
"platformName" : "Android",
"platformVerson" : "5.1",
"deviceName" : "127.0.0.1:7555",
"appPackage" : "com.xiaoji.emulator",
"appActivity" : ".ui.activity.AppStoreActivity",
"unicodeKeyboard" : True,
"resetKeyboard" : True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",info)
time.sleep(5)

if driver.is_app_installed("com.xiaoji.emulator"):
print("这台手机有模拟器！")
time.sleep(2)
def giao_play():
driver.implicitly_wait(100)
driver.find_element_by_xpath("//*[@text='跳过']").click()
for i in range(10):
play_1 = WebDriverWait(driver,5).until(lambda x : x.find_elements_by_class_name("android.widget.RelativeLayout"))
if len(play_1) == 25:
play_1[21].click()
break
print("我giao！？没找到控件！？")
time.sleep(1)
TouchAction(driver).tap(x=1394, y=675,count=1).perform()
time.sleep(1)
TouchAction(driver).tap(x=746, y=754).perform()
time.sleep(1)
TouchAction(driver).tap(x=1368, y=193).perform()
time.sleep(1)
TouchAction(driver).tap(x=710, y=745).perform()

giao_play()
time.sleep(5)
def giao_pr():
print(driver.current_package)
print(driver.current_activity)
giao_pr()
def giao_exit():
driver.__exit__()

giao_exit()