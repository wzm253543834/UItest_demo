# coding = utf-8
from framework.base_page import BasePage


class AreadevicePage(BasePage):

    menu_areadevice = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/div"
    menu_areadevice_area = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[1]"
    menu_areadevice_price = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[2]"
    menu_areadevice_devicelist = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[3]"
    menu_areadevice_deviceInfo = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[4]"
    menu_areadevice_epdevicelist = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[5]"
    menu_areadevice_contract = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[6]"
    menu_areadevice_place = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[7]"
    menu_areadevice_company = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[8]"
    menu_areadevice_rentWarn = "xpath=>//*[@id='app']/div/div/div[2]/aside/ul/li[1]/ul/li[9]"
    tab_area = "xpath=>//*[@id='tab-2']"
    tab_price = "xpath=>//*[@id='tab-3']"
    tab_devicelist = "xpath=>//*[@id='tab-4']"
    tab_deviceInfo = "xpath=>//*[@id='tab-151']"
    tab_epdevicelist = "xpath=>//*[@id='tab-7']"
    tab_contract = "xpath=>//*[@id='tab-109']"
    tab_place = "xpath=>//*[@id='tab-120']"
    tab_company = "xpath=>//*[@id='tab-126']"
    tab_rentWarn = "xpath=>//*[@id='tab-183']"

    """
    网点设备各菜单地址及tab页地址
    """

    # 点击网点设备
    def search_click_areadevice(self):
        self.click(self.menu_areadevice)

    # 点击网点管理
    def search_click_areadevice_area(self):
        self.click(self.menu_areadevice_area)

    # 获取网点管理tab名
    def find_tab_area(self):
        a = self.get_tab_title(self.tab_area)
        return a

    # 点击价格管理
    def search_click_areadevice_price(self):
        self.click(self.menu_areadevice_price)

    # 获取价格管理tab名
    def find_tab_price(self):
        a = self.get_tab_title(self.tab_price)
        return a

    # 点击设备列表
    def search_click_areadevice_devicelist(self):
        self.click(self.menu_areadevice_devicelist)

    # 获取设备列表tab名
    def find_tab_devicelist(self):
        a = self.get_tab_title(self.tab_devicelist)
        return a

    # 点击设备信息
    def search_click_areadevice_deviceinfo(self):
        self.click(self.menu_areadevice_deviceInfo)

    # 获取设备信息tab名
    def find_tab_deviceinfo(self):
        a = self.get_tab_title(self.tab_deviceInfo)
        return a

    # 点击异常设备列表
    def search_click_areadevice_epdevicelist(self):
        self.click(self.menu_areadevice_epdevicelist)

    # 获取异常设备列表tab名
    def find_tab_epdevicelist(self):
        a = self.get_tab_title(self.tab_epdevicelist)
        return a

    # 点击合同预警
    def search_click_areadevice_contract(self):
        self.click(self.menu_areadevice_contract)

    # 获取合同预警tab名
    def find_tab_contract(self):
        a = self.get_tab_title(self.tab_contract)
        return a

    # 点击场地管理
    def search_click_areadevice_place(self):
        self.click(self.menu_areadevice_place)

    # 获取场地管理tab名
    def find_tab_place(self):
        a = self.get_tab_title(self.tab_place)
        return a

    # 点击分公司管理
    def search_click_areadevice_company(self):
        self.click(self.menu_areadevice_company)

    # 获取分公司管理tab名
    def find_tab_company(self):
        a = self.get_tab_title(self.tab_company)
        return a

    # 点击租金提醒
    def search_click_areadevice_rentWarn(self):
        self.click(self.menu_areadevice_rentWarn)

    # 获取租金提醒tab名
    def find_tab_rentWarn(self):
        a = self.get_tab_title(self.tab_rentWarn)
        return a


class AreaSearch(BasePage):

    area_areaid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    area_areaname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    area_areawithdrawal_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    area_companyname_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    area_areaenablestatus_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div/input"
    area_besideareastatus_search = "xpath=>//*[@id='search_list']/div[6]/div/div/div/input"
    area_partnername_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    area_devicemodel_search = "xpath=>//*[@id='search_list']/div[9]/div/div/div/input"
    area_partnertype_search = "xpath=>//*[@id='search_list']/div[10]/div/div/div/input"
    area_placename_search = "xpath=>//*[@id='search_list']/div[11]/div/div/input"
    area_iswarehouse_search = "xpath=>//*[@id='search_list']/div[12]/div/div/div/input"
    area_search_button = "xpath=>//*[@id='search_list']/div[7]/div/button"
    area_empty_button = "xpath=>//*[@id='search_list']/div[13]/div/button"
    area_areawithdrawal = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    area_companyname = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    area_areaenablestatus = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    area_besideareastatus = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    area_devicemodel = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    area_partnertype = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"
    area_iswarehouse = "xpath=>/html/body/div[8]/div[1]/div[1]/ul/li[1]"

    """
    网点管理各筛选项
    """

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.area_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.area_areaname_search, text)

    # 网点提现查询
    def areawithdrawal_search(self):
        self.click(self.area_areawithdrawal_search)
        self.sleep(2)
        self.click(self.area_areawithdrawal)

    # 分公司名称查询
    def companyname_search(self):
        self.click(self.area_companyname_search)
        self.sleep(2)
        self.click(self.area_companyname)

    # 网点启用状态查询
    def areaenablestatus_search(self):
        self.click(self.area_areaenablestatus_search)
        self.sleep(2)
        self.click(self.area_areaenablestatus)

    # 周边网点状态查询
    def besideareastatus_search(self):
        self.click(self.area_besideareastatus_search)
        self.sleep(2)
        self.click(self.area_besideareastatus)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.area_partnername_search, text)

    # 设备型号查询
    def devicemodel_search(self):
        self.click(self.area_devicemodel_search)
        self.sleep(2)
        self.click(self.area_devicemodel)

    # 合作类型查询
    def partnertype_search(self):
        self.click(self.area_partnertype_search)
        self.sleep(2)
        self.click(self.area_partnertype)

    # 场地名称查询
    def placename_search(self, text):
        self.type(self.area_placename_search, text)

    # 是否仓库查询
    def iswarehouse_search(self):
        self.click(self.area_iswarehouse_search)
        self.sleep(2)
        self.click(self.area_iswarehouse)

    # 查询按钮
    def search_button_click(self):
        self.click(self.area_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.area_empty_button)

    # 测试结果断言
    result_areaid = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[3]/div"
    result_areaname = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[4]/div"
    result_companyname = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[6]/div"
    result_areaenablestatus = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[19]/div/i"
    result_besideareastatus = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[18]/div/i"
    result_partnername = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[8]/div"
    result_devicemodel = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[17]/div"
    result_partnertype = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[9]/div"
    result_placename = "xpath=>//*[@id='area_fixed']/div[2]/div/div[3]/table/tbody/tr/td[7]/div"
    # result_iswarehouse = "xpath=>"

    # 断言网点ID查询结果
    def find_result_areaid(self):
        a = self.get_search_result(self.result_areaid)
        return a

    # 断言网点名称查询结果
    def find_result_areaname(self):
        a = self.get_search_result(self.result_areaname)
        return a

    # 断言分公司名称查询结果
    def find_result_companyname(self):
        a = self.get_search_result(self.result_companyname)
        return a

    # 断言网点启用状态查询结果
    def find_result_areaenablestatus(self):
        a = self.get_search_result_icon(self.result_areaenablestatus)
        return a

    # 断言周边网点状态查询结果
    def find_result_besideareastatus(self):
        a = self.get_search_result_icon(self.result_besideareastatus)
        return a

    # 断言合伙人查询结果
    def find_result_partnername(self):
        a = self.get_search_result(self.result_partnername)
        return a

    # 断言设备型号查询结果
    def find_result_devicemodel(self):
        a = self.get_search_result(self.result_devicemodel)
        return a

    # 断言合作类型查询结果
    def find_result_partnertype(self):
        a = self.get_search_result(self.result_partnertype)
        return a

    # 断言场地名称查询结果
    def find_result_placename(self):
        a = self.get_search_result(self.result_placename)
        return a


class PriceSearch(BasePage):

    price_wakeupbodyprice_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    price_passbreathbloodprice_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    price_diastolemeridiansprice_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    price_priceid_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    price_isenable_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div/input"
    price_wakeupbodytime_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    price_passbreathbloodtime_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    price_diastolemeridianstime_search = "xpath=>//*[@id='search_list']/div[9]/div/div/input"
    price_pricename_search = "xpath=>//*[@id='search_list']/div[10]/div/div/input"
    price_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    price_empty_button = "xpath=>//*[@id='search_list']/div[11]/div/button"
    price_isenable = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    价格管理各筛选项
    """

    # 唤醒身体价格查询
    def wakeupbodyprice_search(self, text):
        self.type(self.price_wakeupbodyprice_search, text)

    # 通行气血价格查询
    def passbreathbloodprice_search(self, text):
        self.type(self.price_passbreathbloodprice_search, text)

    # 舒张筋骨价格查询
    def diastolemeridiansprice_search(self, text):
        self.type(self.price_diastolemeridiansprice_search, text)

    # 价格ID查询
    def priceid_search(self, text):
        self.type(self.price_priceid_search, text)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.price_isenable_search)
        self.sleep(2)
        self.click(self.price_isenable)

    # 唤醒身体时长查询
    def wakeupbodytime_search(self, text):
        self.type(self.price_wakeupbodytime_search, text)

    # 通行气血时长查询
    def passbreathbloodtime_search(self, text):
        self.type(self.price_passbreathbloodtime_search, text)

    # 舒张筋骨时长查询
    def diastolemeridianstime_search(self, text):
        self.type(self.price_diastolemeridianstime_search, text)

    # 价格名称查询
    def pricename_search(self, text):
        self.type(self.price_pricename_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.price_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.price_empty_button)

    # 测试结果断言
    result_wakeupbodyprice = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[4]/div"
    result_passbreathbloodprice = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[6]/div"
    result_diastolemeridiansprice = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[8]/div"
    result_priceid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_isenable = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[10]/div/i"
    result_wakeupbodytime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[5]/div"
    result_passbreathbloodtime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[7]/div"
    result_diastolemeridianstime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[9]/div"
    result_pricename = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"

    # 断言唤醒身体价格查询结果
    def find_result_wakeupbodyprice(self):
        a = self.get_search_result(self.result_wakeupbodyprice)
        return a

    # 断言通行气血价格查询结果
    def find_result_passbreathbloodprice(self):
        a = self.get_search_result(self.result_passbreathbloodprice)
        return a

    # 断言舒张筋骨价格查询结果
    def find_result_diastolemeridiansprice(self):
        a = self.get_search_result(self.result_diastolemeridiansprice)
        return a

    # 断言价格ID查询结果
    def find_result_priceid(self):
        a = self.get_search_result(self.result_priceid)
        return a

    # 断言是否启用查询结果
    def find_result_isenable(self):
        a = self.get_search_result_icon(self.result_isenable)
        return a

    # 断言唤醒身体时长查询结果
    def find_result_wakeupbodytime(self):
        a = self.get_search_result(self.result_wakeupbodytime)
        return a

    # 断言通行气血时长查询结果
    def find_result_passbreathbloodtime(self):
        a = self.get_search_result(self.result_passbreathbloodtime)
        return a

    # 断言舒张筋骨时长查询结果
    def find_result_diastolemeridianstime(self):
        a = self.get_search_result(self.result_diastolemeridianstime)
        return a

    # 断言价格名称查询结果
    def find_result_pricename(self):
        a = self.get_search_result(self.result_pricename)
        return a


class DevicelistSearch(BasePage):

    devicelist_deviceid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    devicelist_devicename_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    devicelist_devicemodel_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    devicelist_areaid_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    devicelist_areaname_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    devicelist_partnername_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    devicelist_devicestatus_search = "xpath=>//*[@id='search_list']/div[8]/div/div/div/input"
    devicelist_delivertime_search = "xpath=>//*[@id='search_list']/div[9]/div/div/input[1]"
    devicelist_deviceisenablestatus_search = "xpath=>//*[@id='search_list']/div[10]/div/div/div/input"
    devicelist_movetime_search = "xpath=>//*[@id='search_list']/div[11]/div/div/input"
    devicelist_isinwarehouse_search = "xpath=>//*[@id='search_list']/div[13]/div/div/div/input"
    devicelist_tag_search = "xpath=>//*[@id='search_list']/div[14]/div/div/input"
    devicelist_isscrap_search = "xpath=>//*[@id='search_list']/div[15]/div/div/div/input"
    devicelist_areawithdrawal_search = "xpath=>//*[@id='search_list']/div[16]/div/div/div/input"
    devicelist_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    devicelist_empty_button = "xpath=>//*[@id='search_list']/div[12]/div/button"
    devicelist_devicemodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    devicelist_devicestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    devicelist_delivertime = "xpath=>/html/body/div[4]/div[1]/div/div[1]/table/tbody/tr[5]/td[3]"
    devicelist_deviceisenablestatus = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"
    devicelist_isinwarehouse = "xpath=>/html/body/div[6]/div[1]/div[1]/ul/li[1]"
    devicelist_isscrap = "xpath=>/html/body/div[7]/div[1]/div[1]/ul/li[1]"
    devicelist_areawithdrawal = "xpath=>/html/body/div[8]/div[1]/div[1]/ul/li[1]"

    """
    设备列表各筛选项
    """

    # 设备ID查询
    def deviceid_search(self, text):
        self.type(self.devicelist_deviceid_search, text)

    # 设备名称查询
    def devicename_search(self, text):
        self.type(self.devicelist_devicename_search, text)

    # 设备型号查询
    def devicemodel_search(self):
        self.click(self.devicelist_devicemodel_search)
        self.sleep(2)
        self.click(self.devicelist_devicemodel)

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.devicelist_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.devicelist_areaname_search, text)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.devicelist_partnername_search, text)

    # 设备状态查询
    def devicestatus_search(self):
        self.click(self.devicelist_devicestatus_search)
        self.sleep(2)
        self.click(self.devicelist_devicestatus)

    # 发货时间查询
    def delivertime_search(self):
        self.click(self.devicelist_delivertime_search)
        self.sleep(2)
        self.click(self.devicelist_delivertime)
        self.click(self.devicelist_delivertime)

    # 设备启用状态查询
    def deviceisenablestatus_search(self):
        self.click(self.devicelist_deviceisenablestatus_search)
        self.sleep(2)
        self.click(self.devicelist_deviceisenablestatus)

    # 移机时间（大于）查询
    def movetime_search(self, text):
        self.type(self.devicelist_movetime_search, text)

    # 是否在仓查询
    def isinwarehouse_search(self):
        self.click(self.devicelist_isinwarehouse_search)
        self.sleep(2)
        self.click(self.devicelist_isinwarehouse)

    # 标签查询
    def tag_search(self, text):
        self.type(self.devicelist_tag_search, text)

    # 是否报废查询
    def isscrap_search(self):
        self.click(self.devicelist_isscrap_search)
        self.sleep(2)
        self.click(self.devicelist_isscrap)

    # 网点提现查询
    def areawithdrawal_search(self):
        self.click(self.devicelist_areawithdrawal_search)
        self.sleep(2)
        self.click(self.devicelist_areawithdrawal)

    # 查询按钮
    def search_button_click(self):
        self.click(self.devicelist_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.devicelist_empty_button)

    # 测试结果断言
    result_deviceid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/a"
    result_devicename = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[3]/div"
    result_devicemodel = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[4]/div"
    result_areaid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[9]/div"
    result_areaname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[8]/div"
    result_partnername = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[10]/div"
    result_devicestatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[5]/div"
    result_delivertime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[11]/div"
    result_deviceisenablestatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[20]/div/i"
    result_movetime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[12]/div"
    # result_iswarehouse = "xpath=>"
    result_tag = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[5]/div"
    result_isscrap = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[21]/div/i"

    # 断言设备ID查询结果
    def find_result_deviceid(self):
        a = self.get_search_result(self.result_deviceid)
        return a

    # 断言设备名称查询结果
    def find_result_devicename(self):
        a = self.get_search_result(self.result_devicename)
        return a

    # 断言设备型号查询结果
    def find_result_devicemodel(self):
        a = self.get_search_result(self.result_devicemodel)
        return a

    # 断言网点ID查询结果
    def find_result_areaid(self):
        a = self.get_search_result(self.result_areaid)
        return a

    # 断言网点名称查询结果
    def find_result_areaname(self):
        a = self.get_search_result(self.result_areaname)
        return a

    # 断言合伙人查询结果
    def find_result_partnername(self):
        a = self.get_search_result(self.result_partnername)
        return a

    # 断言设备状态查询结果
    def find_result_devicestatus(self):
        a = self.get_search_result(self.result_devicestatus)
        return a

    # 断言发货时间查询结果
    def find_result_delivertime(self):
        a = self.get_search_result(self.result_delivertime)
        return a

    # 断言设备启用状态查询结果
    def find_result_deviceisenablestatus(self):
        a = self.get_search_result_icon(self.result_deviceisenablestatus)
        return a

    # 断言移机时间（大于）查询结果
    def find_result_movetime(self):
        a = self.get_search_result(self.result_movetime)
        return a

    # 断言标签查询结果
    def find_result_tag(self):
        a = self.get_search_result(self.result_tag)
        return a

    # 断言是否报废查询结果
    def find_result_isscrap(self):
        a = self.get_search_result_icon(self.result_isscrap)
        return a


class DeviceInfoSearch(BasePage):

    deviceInfo_deviceid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    deviceInfo_devicemodel_search = "xpath=>//*[@id='search_list']/div[2]/div/div/div/input"
    deviceInfo_areaid_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    deviceInfo_areaname_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    deviceInfo_devicestatus_search = "xpath=>//*[@id='search_list']/div[6]/div/div/div/input"
    deviceInfo_isenable_search = "xpath=>//*[@id='search_list']/div[7]/div/div/div/input"
    deviceInfo_simcardnumber_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input"
    deviceInfo_areawithdrawal_search = "xpath=>//*[@id='search_list']/div[9]/div/div/input"
    deviceInfo_search_button = "xpath=>//*[@id='search_list']/div[5]/div/button"
    deviceInfo_empty_button = "xpath=>//*[@id='search_list']/div[10]/div/button"
    deviceInfo_devicemodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    deviceInfo_devicestatus = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    deviceInfo_isenable = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"
    deviceInfo_areawithdrawal = "xpath=>/html/body/div[5]/div[1]/div[1]/ul/li[1]"

    """
    设备信息各筛选项
    """

    # 设备ID查询
    def deviceid_search(self, text):
        self.type(self.deviceInfo_deviceid_search, text)

    # 设备型号查询
    def devicemodel_search(self):
        self.click(self.deviceInfo_devicemodel_search)
        self.sleep(2)
        self.click(self.deviceInfo_devicemodel)

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.deviceInfo_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.deviceInfo_areaname_search, text)

    # 设备状态查询
    def devicestatus_search(self):
        self.click(self.deviceInfo_devicestatus_search)
        self.sleep(2)
        self.click(self.deviceInfo_devicestatus)

    # 是否启用查询
    def isenable_search(self):
        self.click(self.deviceInfo_isenable_search)
        self.sleep(2)
        self.click(self.deviceInfo_isenable)

    # SIM卡号查询
    def simcardnumber_search(self, text):
        self.type(self.deviceInfo_simcardnumber_search, text)

    # 网点提现查询
    def areawithdrawal_search(self):
        self.click(self.deviceInfo_areawithdrawal_search)
        self.sleep(2)
        self.click(self.deviceInfo_areawithdrawal)

    # 查询按钮
    def search_button_click(self):
        self.click(self.deviceInfo_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.deviceInfo_empty_button)

    # 测试结果断言
    result_deviceid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div/a"
    result_devicemodel = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[4]/div"
    result_areaid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[8]/div"
    result_areaname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[7]/div"
    result_devicestatus = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[5]/div"
    result_isenable = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[14]/div/i"
    result_simcardnumber =  "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[13]/div"

    # 断言设备ID查询结果
    def find_result_deviceid(self):
        a = self.get_search_result(self.result_deviceid)
        return a

    # 断言设备型号查询结果
    def find_result_devicemodel(self):
        a = self.get_search_result(self.result_devicemodel)
        return a

    # 断言网点ID查询结果
    def find_result_areaid(self):
        a = self.get_search_result(self.result_areaid)
        return a

    # 断言网点名称查询结果
    def find_result_areaname(self):
        a = self.get_search_result(self.result_areaname)
        return a

    # 断言设备状态查询结果
    def find_result_devicestatus(self):
        a = self.get_search_result(self.result_devicestatus)
        return a

    # 断言是否启用查询结果
    def find_result_isenable(self):
        a = self.get_search_result_icon(self.result_isenable)
        return a

    # 断言SIM卡号查询结果
    def find_result_simcardnumber(self):
        a = self.get_search_result(self.result_simcardnumber)
        return a


class EpdevicelistSearch(BasePage):

    epdevicelist_deviceid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    epdevicelist_devicename_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    epdevicelist_devicemodel_search = "xpath=>//*[@id='search_list']/div[3]/div/div/div/input"
    epdevicelist_areaid_search = "xpath=>//*[@id='search_list']/div[4]/div/div/input"
    epdevicelist_areaname_search = "xpath=>//*[@id='search_list']/div[5]/div/div/input"
    epdevicelist_partnername_search = "xpath=>//*[@id='search_list']/div[7]/div/div/input"
    epdevicelist_delivertime_search = "xpath=>//*[@id='search_list']/div[8]/div/div/input[1]"
    epdevicelist_areawithdrawal_search = "xpath=>//*[@id='search_list']/div[9]/div/div/input"
    epdevicelist_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button"
    epdevicelist_empty_button = "xpath=>//*[@id='search_list']/div[10]/div/button"
    epdevicelist_devicemodel = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    epdevicelist_delivertime = "xpath=>/html/body/div[3]/div[1]/div/div[1]/table/tbody/tr[5]/td[3]"
    epdevicelist_areawithdrawal = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[1]"

    """
    异常设备列表各筛选项
    """

    # 设备ID查询
    def deviceid_search(self, text):
        self.type(self.epdevicelist_deviceid_search, text)

    # 设备名称查询
    def devicename_search(self, text):
        self.type(self.epdevicelist_devicename_search, text)

    # 设备型号查询
    def devicemodel_search(self):
        self.click(self.epdevicelist_devicemodel_search)
        self.sleep(2)
        self.click(self.epdevicelist_devicemodel)

    # 网点ID查询
    def areaid_search(self, text):
        self.type(self.epdevicelist_areaid_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.epdevicelist_areaname_search, text)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.epdevicelist_partnername_search, text)

    # 发货时间查询
    def delivertime_search(self):
        self.click(self.epdevicelist_delivertime_search)
        self.sleep(2)
        self.click(self.epdevicelist_delivertime)
        self.click(self.epdevicelist_delivertime)

    # 网点提现查询
    def areawithdrawal_search(self):
        self.click(self.epdevicelist_areawithdrawal_search)
        self.sleep(2)
        self.click(self.epdevicelist_areawithdrawal)

    # 查询按钮
    def search_button_click(self):
        self.click(self.epdevicelist_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.epdevicelist_empty_button)

    # 测试结果断言
    result_deviceid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[2]/div"
    result_devicename = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[3]/div"
    result_devicemodel = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[4]/div"
    result_areaid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[9]/div"
    result_areaname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[8]/div"
    result_partnername = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[10]/div"
    result_delivertime = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[11]/div"

    # 断言设备ID查询结果
    def find_result_deviceid(self):
        a = self.get_search_result(self.result_deviceid)
        return a

    # 断言设备名称查询结果
    def find_result_devicename(self):
        a = self.get_search_result(self.result_devicename)
        return a

    # 断言设备型号查询结果
    def find_result_devicemodel(self):
        a = self.get_search_result(self.result_devicemodel)
        return a

    # 断言网点ID查询结果
    def find_result_areaid(self):
        a = self.get_search_result(self.result_areaid)
        return a

    # 断言网点名称查询结果
    def find_result_areaname(self):
        a = self.get_search_result(self.result_areaname)
        return a

    # 断言合伙人查询结果
    def find_result_partnername(self):
        a = self.get_search_result(self.result_partnername)
        return a

    # 断言发货时间查询结果
    def find_result_delivertime(self):
        a = self.get_search_result(self.result_delivertime)
        return a


class ContractSearch(BasePage):

    contract_partnername_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    contract_areaname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    contract_areawithdrawal_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    contract_search_button = "xpath=>//*[@id='search_list']/div[4]/div/button[1]"
    contract_empty_button = "xpath=>//*[@id='search_list']/div[4]/div/button[2]"
    contract_areawithdrawal = "xpath=>/html/body/div[2]/div[1]/div[1]/ul/li[1]"

    """
    合同预警各筛选项
    """

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.contract_partnername_search, text)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.contract_areaname_search, text)

    # 网点提现查询
    def areawithdrawal_search(self):
        self.click(self.contract_areawithdrawal_search)
        self.sleep(2)
        self.click(self.contract_areawithdrawal)

    # 查询按钮
    def search_button_click(self):
        self.click(self.contract_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.contract_empty_button)

    # 测试结果断言
    result_partnername = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[5]/div"
    result_areaname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[4]/div"

    # 断言合伙人查询结果
    def find_result_partnername(self):
        a = self.get_search_result(self.result_partnername)
        return a

    # 断言网点名称查询结果
    def find_result_areaname(self):
        a = self.get_search_result(self.result_areaname)
        return a


class PlaceSearch(BasePage):

    place_placeid_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    place_placename_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    place_partnername_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    place_search_button = "xpath=>//*[@id='search_list']/div[4]/div/button[1]"
    place_empty_button = "xpath=>//*[@id='search_list']/div[4]/div/button[2]"

    """
    场地管理各筛选项
    """

    # 场地ID查询
    def placeid_search(self, text):
        self.type(self.place_placeid_search, text)

    # 场地名称查询
    def placename_search(self, text):
        self.type(self.place_placename_search, text)

    # 合伙人查询
    def partnername_search(self, text):
        self.type(self.place_partnername_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.place_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.place_empty_button)

    # 测试结果断言
    result_placeid = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"
    result_placename = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[3]/div"
    result_partnername = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[4]/div"

    # 断言场地ID查询结果
    def find_result_placeid(self):
        a = self.get_search_result(self.result_placeid)
        return a

    # 断言场地名称查询结果
    def find_result_placename(self):
        a = self.get_search_result(self.result_placename)
        return a

    # 断言合伙人查询结果
    def find_result_partnername(self):
        a = self.get_search_result(self.result_partnername)
        return a


class CompanySearch(BasePage):

    company_companyname_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    company_search_button = "xpath=>//*[@id='search_list']/div[2]/div/button[1]"
    company_empty_button = "xpath=>//*[@id='search_list']/div[2]/div/button[2]"

    """
    分公司管理各筛选项
    """

    # 分公司名称查询
    def companyname_search(self, text):
        self.type(self.company_companyname_search, text)

    # 查询按钮
    def search_button_click(self):
        self.click(self.company_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.company_empty_button)

    # 测试结果断言
    result_companyname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[1]/div[3]/table/tbody/tr/td[2]/div"

    # 断言分公司名称查询结果
    def find_result_companyname(self):
        a = self.get_search_result(self.result_companyname)
        return a


class RentWarnSearch(BasePage):

    rentWarn_rentmonth_search = "xpath=>//*[@id='search_list']/div[1]/div/div/input"
    rentWarn_areaname_search = "xpath=>//*[@id='search_list']/div[2]/div/div/input"
    rentWarn_fieldname_search = "xpath=>//*[@id='search_list']/div[3]/div/div/input"
    rentWarn_status_search = "xpath=>//*[@id='search_list']/div[4]/div/div/div/input"
    rentWarn_paymethod_search = "xpath=>//*[@id='search_list']/div[5]/div/div/div/input"
    rentWarn_search_button = "xpath=>//*[@id='search_list']/div[6]/div/button[1]"
    rentWarn_empty_button = "xpath=>//*[@id='search_list']/div[6]/div/button[2]"
    rentWarn_rentmonth = "xpath=>/html/body/div[2]/div[1]/div/div[2]/table[3]/tbody/tr[1]/td[1]/a"
    rentWarn_status = "xpath=>/html/body/div[3]/div[1]/div[1]/ul/li[1]"
    rentWarn_paymethod = "xpath=>/html/body/div[4]/div[1]/div[1]/ul/li[2]"

    """
    租金提醒各筛选项
    """

    # 租金月份查询
    def rentmonth_search(self):
        self.click(self.rentWarn_rentmonth_search)
        self.sleep(2)
        self.click(self.rentWarn_rentmonth)

    # 网点名称查询
    def areaname_search(self, text):
        self.type(self.rentWarn_areaname_search, text)

    # 场地方名称查询
    def fieldname_search(self, text):
        self.type(self.rentWarn_fieldname_search, text)

    # 状态查询
    def status_search(self):
        self.click(self.rentWarn_status_search)
        self.sleep(2)
        self.click(self.rentWarn_status)

    # 支付方式查询
    def paymethod_search(self):
        self.click(self.rentWarn_paymethod_search)
        self.sleep(2)
        self.click(self.rentWarn_paymethod)

    # 查询按钮
    def search_button_click(self):
        self.click(self.rentWarn_search_button)

    # 清空按钮
    def empty_button_click(self):
        self.click(self.rentWarn_empty_button)

    # 测试结果断言
    result_rentmonth = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[10]/div"
    result_areaname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[4]/div"
    result_fieldname = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[5]/div"
    result_status = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[18]/div"
    result_paymethod = "xpath=>//*[@id='app']/div/div/div[2]/div/div[2]/section/div[2]/div/div[3]/table/tbody/tr/td[15]/div"

    # 断言租金月份查询结果
    def find_result_rentmonth(self):
        a = self.get_search_result(self.result_rentmonth)
        return a

    # 断言网点名称查询结果
    def find_result_areaname(self):
        a = self.get_search_result(self.result_areaname)
        return a

    # 断言场地方名称查询结果
    def find_result_fieldname(self):
        a = self.get_search_result(self.result_fieldname)
        return a

    # 断言状态查询结果
    def find_result_status(self):
        a = self.get_search_result(self.result_status)
        return a

    # 断言支付方式查询结果
    def find_result_paymethod(self):
        a = self.get_search_result(self.result_paymethod)
        return a
