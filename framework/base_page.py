# coding = utf-8
import time
import os.path
from framework.logger import Logger
# from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# create a logger instance
logger = Logger(logger='BasePage').getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 关闭浏览器并结束测试
    def quit_browser(self):
        self.driver.quit()

    # 浏览器刷新
    def refresh(self):
        self.driver.refresh()
        logger.info("Refresh on current page.")

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("Wait for %d seconds.", seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s.", e)

    # 保存图片
    def get_window_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹。screenshots下
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder: /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s", e)
            self.get_window_img()

    # 定位元素方法
    def find_element(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == "i" or selector_by == "id":
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful ""by %s via value: %s",
                            element.text, selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()   # take screenshot
        elif selector_by == "n" or selector_by == "name":
            try:
                element = self.driver.find_element_by_name(selector_value)
                logger.info("Had find the element \' %s \' successful ""by %s via value: %s",
                            element.text, selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "c" or selector_by == "class_name":
            try:
                element = self.driver.find_element_by_class_name(selector_value)
                logger.info("Had find the element \' %s \' successful ""by %s via value: %s",
                            element.text, selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "l" or selector_by == "link_text":
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                logger.info("Had find the element \' %s \' successful ""by %s via value: %s",
                            element.text, selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "p" or selector_by == "partial_link_text":
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                logger.info("Had find the element \' %s \' successful ""by %s via value: %s",
                            element.text, selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "t" or selector_by == "tag_name":
            try:
                element = self.driver.find_element_by_tag_name(selector_value)
                logger.info("Had find the element \' %s \' successful ""by %s via value: %s",
                            element.text, selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "x" or selector_by == "xpath":
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful ""by %s via value: %s",
                            element.text, selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "s" or selector_by == "selector_selector":
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                logger.info("Had find the element \' %s \' successful ""by %s via value: %s",
                            element.text, selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element

    def find_elements(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        elements = ''
        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == "i" or selector_by == "id":
            try:
                elements = self.driver.find_elements_by_id(selector_value)
                logger.info("Had find the element successful ""by %s via value: %s", selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()   # take screenshot
        elif selector_by == "n" or selector_by == "name":
            try:
                elements = self.driver.find_elements_by_name(selector_value)
                logger.info("Had find the elements successful ""by %s via value: %s", selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "c" or selector_by == "class_name":
            try:
                elements = self.driver.find_elements_by_class_name(selector_value)
                logger.info("Had find the elements successful ""by %s via value: %s", selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "l" or selector_by == "link_text":
            try:
                elements = self.driver.find_elements_by_link_text(selector_value)
                logger.info("Had find the elements successful ""by %s via value: %s", selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "p" or selector_by == "partial_link_text":
            try:
                elements = self.driver.find_elements_by_partial_link_text(selector_value)
                logger.info("Had find the elements successful ""by %s via value: %s", selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "t" or selector_by == "tag_name":
            try:
                elements = self.driver.find_elements_by_tag_name(selector_value)
                logger.info("Had find the element successful ""by %s via value: %s", selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "x" or selector_by == "xpath":
            try:
                elements = self.driver.find_elements_by_xpath(selector_value)
                logger.info("Had find the elements successful ""by %s via value: %s", selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        elif selector_by == "s" or selector_by == "selector_selector":
            try:
                elements = self.driver.find_elements_by_css_selector(selector_value)
                logger.info("Had find the elements successful ""by %s via value: %s", selector_by, selector_value)
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s", e)
                self.get_window_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return elements

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox", text)
        except NameError as e:
            logger.error("Failed to type in inputBox with %s", e)
            self.get_window_img()

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clearing text in inputBox before typing.")
        except NameError as e:
            logger.error("Failed to clear in inputBox with %s", e)
            self.get_window_img()

    # 点击
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked.", el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s", e)

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s", self.driver.title)
        return self.driver.title

    # 获取tab页标题
    def get_tab_title(self, selector):
        el = self.find_element(selector)
        tl = el.text
        try:
            logger.info("The tab\'s title is %s.", tl)
            return tl
        except NameError as e:
            logger.error("Failed to find the tab\'s title: %s", e)

    def get_search_result(self, selector):
        li = self.find_elements(selector)
        lis = []
        for i in li:
            lis.append(i.text)
        return lis

    # 等待时间
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds", seconds)
