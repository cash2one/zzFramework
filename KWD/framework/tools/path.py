# -*- coding: utf-8 -*-
"""获取各层的绝对路径"""
import os
path = os.path.split(os.path.realpath(__file__))[0]
# config层
CONFIG_PATH = path + '\\..\\config\\'
# data层
DATA_PATH = path + '\\..\\data\\'
# log层
LOG_PATH = path + '\\..\\log\\'
# report层
REPORT_PATH = path + '\\..\\report\\'
# tools层
TOOLS_PATH = path + '\\..\\tools\\'
# test层
TEST_PATH = path + '\\..\\test\\'
