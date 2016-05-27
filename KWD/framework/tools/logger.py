# -*- coding: utf-8 -*-
"""创建一个自定义日志类，将代码中的错误格式化输出到统一的文件中"""
import logging
import traceback
import config
import datetime


def log(location, message, level='error'):
    """logger模块的log方法，提供标准输出到指定的日志，接受三个参数，报错位置、错误信息以及错误级别"""
    # 读取配置，获取日志配置：输出级别以及日志文件位置
    cf = config.Config()
    log_level = cf.get('log', 'level').upper()
    # 获取当前日期并拼接到日志文件文件名
    date = datetime.date.today()
    try:
        log_file = cf.get('log', 'path') + 'test.' + str(date) + '.log'
    except config.ConfigException:
        # 如果获取配置文件中的log路径失败，则使用默认log层路径
        from .path import LOG_PATH
        log_file = LOG_PATH + 'test.' + str(date) + '.log'
    # 生成logging对象，将logger名称设置为参数location
    logger = logging.getLogger(location)
    logger.setLevel(log_level)
    # 文件输出与控制台输出，文件输出级别在配置文件中指定，控制台输出用于调试，级别为ERROR
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)
    # 格式化日志输出
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    # 判断级别并输出日志
    error_level = level.lower()
    if error_level == 'critical':
        logger.critical(message)
    elif error_level == 'error':
        logger.error(message)
    elif error_level == 'warning':
        logger.warning(message)
    elif error_level == 'info':
        logger.info(message)
    else:
        logger.debug(message)
    # 如果不是自定义字符串，是exception的话，输出traceback
    if type(message) != str and type(message) != unicode:
        with open(log_file, 'a') as f:
            traceback.print_stack(file=f)
        traceback.print_stack()


if __name__ == '__main__':
    # 简单测试日志输出
    log('Parser', '这儿出错了', 'error')
    try:
        a
    except NameError, e:
        log('logger', e, level='error')