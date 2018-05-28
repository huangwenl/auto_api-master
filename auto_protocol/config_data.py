from core.common import Common


class ConfigData(object):
    # 设置需要提取数据的excel的下标页名字，和地址
    excel_data = Common.api_read_data1('test_approve_accredit',r'D:\PyCharm_WorkSpace\auto_api-master\auto_protocol\api_config\testcase_data.xlsx')
    num = 2
