# -*- coding: utf-8 -*-
"""
@Time : 2021/6/20 12:24
@Author : 华大大不是大大
@File : test_demo1.py
@内容 : 用例标签markers、用例执行顺序order、用例跳过skip、skipif，用例前后置 setup、teardown、setup_class、teardown_class、setup_module、teardown_module
"""
import allure
import pytest


# 模块级别的前置方法
def setup_module():
    print('\n', '设置模块用例前置，当前模块执行'.center(50, '-'))


# 模块级别的后置方法
def teardown_module():
    print('\n', '设置模块用例后置，当前模块执行'.center(50, '-'))


@allure.epic('pytestdemo项目')  # 定制allure报告的项目名称
@allure.feature('模块名称：TestDemo1')  # 定制allure报告的模块名称
class TestDemo1:
    # 设置class级别的前置
    def setup_class(self):
        print('\n', '设置class用例前置，当前类执行'.center(50, '-'))

    # 设置class级别的后置
    def teardown_class(self):
        print('\n', '设置class用例后置，当前类执行'.center(50, '-'))

    # 设置函数级别的前置
    def setup(self):
        print('\n', '设置用例前置'.center(50, '-'))

    # 设置函数级别的后置
    def teardown(self):
        print('\n', '设置用例后置'.center(50, '-'))

    @pytest.mark.smoke  # 定义用例的标签
    @pytest.mark.run(order=3)  # 定义用例的执行顺序
    @pytest.mark.skipif(3 > 4, reason='设置有条件跳过用例')  # 设置有条件跳过用例
    @allure.story('test_fun1')  # 定制allure报告的用例名称
    @allure.title('测试用例标题test_fun1')  # 定制allure报告的用例标题
    @allure.severity(allure.severity_level.BLOCKER)  # 设置用例的严重程度
    @allure.description('测试用例描述：这是测试用例1  smoke标签')  # 定制allure报告的描述信息
    @allure.link(name='接口地址', url='www.baid1.com')  # 定制allure报告的url链接
    @allure.issue(name='bug地址', url='www.baidu.com')  # 定制allure报告的bug地址
    @allure.testcase(name='测试用例地址', url='www.baidu.com') # 定制allure报告的测试用例地址
    def test_fun1(self):
        # 附件的定制
        with open('F:\\视频图片\\图片\头像\\oe4awi223m4F3n6.png', mode='rb') as f:
            allure.attach(body=f.read(), name='头像', attachment_type=allure.attachment_type.PNG) # 定制allure报告右边的图片附件
        allure.attach(body="www.baidu.com", name='请求url', attachment_type=allure.attachment_type.TEXT)  # 定制allure右边接口信息展示
        # 定制allure报告右边的测试步骤
        with allure.step('测试用例步骤1'):
            print('\n测试用例 —— 1 --markers=smoke')
        with allure.step('测试用例步骤2'):
            print('设置执行顺序 order=3')
        with allure.step('测试用例步骤3'):
            print('已设置有条件跳过，不满足条件')

    @pytest.mark.test_one
    @pytest.mark.run(order=2)
    @pytest.mark.skip(reason='设置无条件跳过用例')
    @allure.story('test_fun2')
    @allure.title('测试用例标题test_fun2')
    def test_fun2(self):
        print('\n测试用例 —— 2 --markers=test_one')
        print('设置执行顺序 order=2')

    @pytest.mark.test_two
    @pytest.mark.run(order=1)
    @allure.story('test_fun3')
    def test_fun3(self, execute_sql):
        allure.dynamic.title('测试用例标题test_fun3' + str(execute_sql))
        print('\n测试用例 —— 3 --mark=test_two')
        print('设置执行顺序 order=1')

    @allure.story('test_fun4')
    def test_fun4(self):
        print('\n测试用例 —— 4 --未定义标签mark')


@pytest.mark.smoke
@allure.epic('pytestdemo项目')
@allure.feature('模块名称：TestDemo2')
class TestDemo2:

    @allure.story('test_fun5')
    def test_fun5(self):
        print('\n测试用例 —— 5 --定义类标签mark=smoke')

    @allure.story('test_fun6')
    def test_fun6(self):
        print('\n测试用例 —— 6 --定义类标签mark=smoke')
