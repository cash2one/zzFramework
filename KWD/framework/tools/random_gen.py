# -*- coding: utf-8 -*-
"""随机产生手机号，随机产生字符串"""
import random
import string


def random_phone_number():
    """随机产生手机号"""
    return random.choice(['139', '136', '151', '158']) + ''.join(random.choice('0123456789') for i in range(8))


def random_string(length=1):
    """随机产生长度为length的字符串"""
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def random_number_str(length=1):
    """随机产生长度为length的数字串"""
    return ''.join(random.sample(string.digits, length))

if __name__ == '__main__':
    print random_phone_number()
    print random_string()
    print random_string(8)
    print random_number_str(9)