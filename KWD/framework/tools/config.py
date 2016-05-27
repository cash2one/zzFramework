# -*- coding: utf-8 -*-
"""解析config.ini文件，获取配置"""
import ConfigParser
from .path import CONFIG_PATH


class ConfigException(Exception):
    """自定义读取配置文件失败的异常，输出读取配置文件失败"""
    def __init__(self, message=u'读取配置文件失败！'):
        self.message = message
        print self.message


class Config:
    """Config类读取配置文件，获取配置文件相应配置项"""
    def __init__(self, path=CONFIG_PATH + 'config.ini'):
        """初始化Config类，默认读取config.ini文件"""
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

    def get(self, field, key):
        """从文件中获取某个field中的某个key对应的value值"""
        try:
            result = self.cf.get(field, key)
        except:
            message = '读取配置文件 %s 失败！' % self.path
            raise ConfigException(message)
        return result

    def set(self, field, key, value):
        """设置某个field中某个key的value值"""
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w'))
        except:
            message = '修改配置文件 %s 失败！' % self.path
            raise ConfigException(message)
        return True

    def get_mysql_connect(self):
        """获取sqlalchemy可用的数据库链接字符串"""
        return 'mysql+{0}://{1}:{2}@{3}:{4}/{5}?charset=utf8'.format(
            self.get('db', 'driver'), self.get('db', 'user'), self.get('db', 'pwd'),
            self.get('db', 'host'), self.get('db', 'port'), self.get('db', 'db_name'))

    def get_oracle_connect(self):
        """获取Oracle数据库的链接串"""
        return '{0}/{1}@{2}:{3}/{4}'.format(
            self.get('db', 'user'), self.get('db', 'pwd'), self.get('db', 'host'),
            self.get('db', 'port'), self.get('db', 'db_name'))


if __name__ == '__main__':
    # 简单测试类的各方法
    cf = Config()
    print cf.get('db', 'port')
    # cf.set('db', 'port', '3318')
    print cf.get_oracle_connect()
    # cf.set('db', 'port', '3306')

