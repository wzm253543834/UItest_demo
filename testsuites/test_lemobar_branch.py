# coding = utf-8
# import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.lemobar_login import HomePage
from pageobjects.lemobar_branch import BranchPage
from pageobjects.lemobar_branch import BranchSearch


class BranchPageSearch(unittest.TestCase):

    @classmethod
    # def setUp(self):
    def setUpClass(cls):
        """
        测试固件的setUp()代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    # def tearDown(self):
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上就是关闭浏览器
        :return:
        """
        BrowserEngine.quit_browser(cls)

    def test_a_login_lemobar(self):
        """
        乐摩吧首页账号登录
        :return:
        """
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        """
        homepage = HomePage(self.driver)
        homepage.login()
        homepage.get_window_img()  # 调用基类截图方法
        try:
            assert '乐摩吧数据中心管理系统' in homepage.get_page_title()
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_b_branch_search(self):
        """
        网点管理查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch()
        homepage.sleep(3)
        homepage.search_click_branch_branch()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '网点管理' in homepage.find_tab_branch()
            print('Test Pass')
        except Exception as e:
            print('Test Fail.', format(e))
        newsearch = BranchSearch(self.driver)
        newsearch.branchid_search('22515')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.branchname_search('福州展示仓01')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.officename_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.branchenablestatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.besidebranchstatus_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.partnername_search('直营仓库')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.equipmentmodel_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.partnertype_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.sitename_search('福州展示仓')
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)
        newsearch.iswarehouse_search()
        newsearch.search_button_click()
        newsearch.sleep(2)
        newsearch.clear_button_click()
        newsearch.sleep(2)

    def test_c_price_search(self):
        """
        价格管理查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_price()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '价格管理' in homepage.find_tab_price()
            print('Test Pass')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_d_equipment_search(self):
        """
        设备列表查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_equipment()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '设备列表' in homepage.find_tab_equipment()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

    def test_e_equipmessage_search(self):
        """
        设备信息查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_equipmessage()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '设备信息' in homepage.find_tab_equipmessage()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

    def test_f_abequipment_search(self):
        """
        异常设备列表查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_abequipment()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '异常设备列表' in homepage.find_tab_abequipment()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

    def test_g_contractwarn_search(self):
        """
        合同预警查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_contractwarn()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '合同预警' in homepage.find_tab_contractwarn()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

    def test_h_sitemanage_search(self):
        """
        场地管理查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_sitemanage()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '场地管理' in homepage.find_tab_sitemanage()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))

    def test_i_officemanage_search(self):
        """
        分公司管理查询
        :return:
        """
        homepage = BranchPage(self.driver)
        homepage.search_click_branch_officemanage()
        homepage.sleep(3)
        homepage.get_window_img()
        try:
            assert '分公司管理' in homepage.find_tab_officemanage()
            print('Test Pass')
        except Exception as e:
            print('Test Fail', format(e))


if __name__ == '__main__':
    unittest.main()
