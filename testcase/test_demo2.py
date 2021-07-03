# -*- coding: utf-8 -*-
"""
@Time : 2021/6/27 11:29
@Author : 华大大不是大大
@File : test_demo2.py
"""
import allure
import pytest


# def yml_data():
#     return [['小李', '小张', '小王'], ['小李2', '小张2', '小王2'], ['小李3', '小张3', '小王3']]
#
#
# # 使用fixture实现前后置，可以设置作用域scope为 function、class、module、package、session
# # @pytest.fixture(scope="作用域",params="数据驱动",autouser="自动执行"，ids="自定义参数名称"，name="别名")
# # 当设置name时，引用的时候必须使用name名称
# # 注意传入数据后，必须要在方法后面引用固定的request接收，否则报错
# @pytest.fixture(scope='function', autouse=True, params=yml_data())
# def execute_sql(request):
#     print('\n', '使用fixture实现前后置，这是前置'.center(50, '-'))
#     yield request.param
#     print('\n', '使用fixture实现前后置，这是后置'.center(50, '-'))


@pytest.mark.smoke
@allure.epic('pytestdemo项目')
@allure.feature('模块名称：TestDemo3')
class TestDemo3:

    @allure.story('test_fun7')
    def test_fun7(self, execute_sql):
        print('测试用例 —— 7 --定义类标签mark=smoke' + "  |   返回的数据:", execute_sql)

    @allure.story('test_fun8')
    def test_fun8(self):
        print('测试用例 —— 8 --定义类标签mark=smoke')


@pytest.mark.usefixtures("execute_sql")
@pytest.mark.smoke
@allure.epic('pytestdemo项目')
@allure.feature('模块名称：TestDemo4')
class TestDemo4:

    @allure.story('test_fun9')
    def test_fun9(self, execute_sql):
        allure.dynamic.story('这是用例标题')
        print('测试用例 —— 9 --定义类标签mark=smoke' + "  |   返回的数据:")
        # assert execute_sql[0] == '小李'

    @allure.story('test_fun10')
    def test_fun10(self):
        print('测试用例 —— 10 --定义类标签mark=smoke')

