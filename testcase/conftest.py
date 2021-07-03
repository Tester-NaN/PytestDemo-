# -*- coding: utf-8 -*-
"""
@Time : 2021/6/27 11:58
@Author : 华大大不是大大
@File : conftest.py

1.名称是固定的conftest.py，主要用于单独的存放fixture固件的。
2.级别为package，sesion时，那么可以在多个包甚至多个py文件里面共享前后置。
举例：登录。
模块：模块的共性。
3.发现conftest.py文件里面的fixture不需要导包可以直接使用。
4.conftest。py文件，可以有多个。
作用：出现重复日志，初始化一次日志对象。规避日志重复。连接数据库。关闭数据库。
注意：多个前置同时存在的优先级。
1.conftest.py为函数级别时优先级高于setup/teardown
2.conftest.py为class级别时优先级高于setup_class/teardown_class
3.conftest.py为session级别时优先级高于setup_module/teardown_module
"""
import pytest


# 模拟数据驱动
def yml_data():
    return [['小李', '小张', '小王'], ['小李2', '小张2', '小王2'], ['小李3', '小张3', '小王3']]


# 使用fixture实现前后置，可以设置作用域scope为 function、class、module、package、session
# @pytest.fixture(scope="作用域",params="数据驱动",autouser="自动执行"，ids="自定义参数名称"，name="别名")
# 当设置name时，引用的时候必须使用name名称
# 注意传入数据后，必须要在方法后面引用固定的request接收，否则报错
@pytest.fixture(scope='function', autouse=True, params=yml_data())
def execute_sql(request):
    print('\n', '使用fixture实现前后置，这是前置'.center(50, '-'))
    yield request.param  # 通过yield 实现数据返回，yield后面实现后置方法
    print('\n', '使用fixture实现前后置，这是后置'.center(50, '-'))
