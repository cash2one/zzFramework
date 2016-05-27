# -*- coding: utf-8 -*-
"""从xml中获取页面链接"""
from xml.etree.ElementTree import ElementTree
from .logger import log
import config


class ReadXML:

    def __init__(self, xml='urls.xml'):
        # 读取配置
        try:
            path = config.Config().get('data', 'path')
        except config.ConfigException:
            # 如果从配置文件中读取路径失败，则用默认data层路径
            from .path import DATA_PATH
            path = DATA_PATH
        self.xml = path + '/' + xml

    def get_url(self, api):
        # 获取xml树
        try:
            tree = ElementTree(file=self.xml)
        except Exception, e:
            log('read_xml', e)
        # 获取元素并拼接地址
        try:
            return tree.find('baseurl').text + tree.find(api).text
        except Exception, e:
            log('read_xml find_element', e)
            return None


if __name__ == '__main__':
    print ReadXML(xml='zhigou.xml').get_url('CheckCode')