# -*- coding: utf-8 -*-
"""从xls中获取参数化数据，返回列表"""
from xlrd import open_workbook
from .config import Config, ConfigException


class ReadXls:

    def __init__(self, book_name, sheet_index=0, sheet_name=None):
        self.book_name = book_name
        self.sheet_index = sheet_index
        self.sheet_name = sheet_name

    def get_data(self):
        """从指定xls中读取信息，返回列表，其中存放着不同行与第一行组成的字典"""

        # read config, if something wrong, we'll get data_path from tools.path instead
        try:
            path = Config().get('data', 'path')
        except ConfigException:
            from .path import DATA_PATH
            path = DATA_PATH
        book = path + '/' + self.book_name

        work_book = open_workbook(book)

        # which sheet we will read
        if self.sheet_name is None:
            sheet = work_book.sheet_by_index(self.sheet_index)
        else:
            sheet = work_book.sheet_by_name(self.sheet_name)

        # first line of the excel file is title
        title = sheet.row_values(0)
        data = list()

        # 循环其他行，与第一行组成字典，追加到列表data中
        for col in range(1, sheet.nrows):
            s1 = sheet.row_values(col)
            s2 = [unicode(s).encode('utf-8') for s in s1]  # switch to utf-8 encoding
            data.append(dict(zip(title, s2)))
        return data


if __name__ == '__main__':
    print ReadXls('phone.xlsx').get_data()