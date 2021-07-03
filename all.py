# -*- coding: utf-8 -*-
"""
@Time : 2021/6/20 12:21
@Author : 华大大不是大大
@File : all.py
"""
import os
import time
import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    # 通过临时文件生成allure报告
    os.system('allure generate reports/temps -o reports/allures --clean')
