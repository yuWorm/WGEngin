from typing import Type, NewType, Any


_整数类型 = int
_任意值 = NewType("_任意值", Any)
_字典类型 = dict
_文本类型 = str
_列表类型 = list
_是或否 = bool
_空 = None


class 整数(int):
    pass


class 小数(float):
    pass


class 文本(str):
    def 分割(self, _分割符: _文本类型, _分割次数: _整数类型 = -1):
        """
        将文本按照分割符分割成几段，返回的是一个列表
        :param _分割符: 分割的依据
        :param _分割次数: 分割的次数，默认-1，也就是文本中有几个分割符号就分几次，如果为1，就只分割一次
        :return:
        """
        return self.split(_分割符, _分割次数)

    def 替换(self, _旧文本: _文本类型, _新文本: _文本类型, _替换次数: _整数类型 = -1):
        """
        使用新的内容，替换掉旧的内容
        :param _旧文本: 被替换的文本
        :param _新文本:
        :param _替换次数:
        :return:
        """
        return self.replace(_旧文本, _新文本, _替换次数)

    def 是否开头为(
        self, _文本: _文本类型, _从第几个字开始: _整数类型 | _空 = 0
    ) -> _是或否:
        """
        判断文本是否以某几个字符开头
        :param _文本: 开头的文本
        :param _从第几个字开始: 默认为0，0就是直接从第一个开始
        :return:
        """
        return self.startswith(_文本, _从第几个字开始)

    def 是否结尾为(self, _文本: _文本类型):
        """
        判断文本是否以某几个字符结尾
        :param _文本: 结尾的文本
        :return:
        """
        return self.endswith(_文本)

    def 去空(self):
        """
        去除开头和结尾的空字符,如空格换行等
        :return:
        """
        return self.strip()


class 元组(tuple):
    pass


class 字典(dict):
    def 取出(self, _键名: _文本类型, _默认值: _任意值 = _空):
        return self.get(_键名, _默认值)

    def 弹出(self):
        pass

    def 更新(self, __新字典: _字典类型):
        """

        :param __新字典:
        :return:
        """
        self.update(__新字典)

    def 键(self):
        """
        返回这个字典中的所有键
        :return: 一个可以循环遍历的对象，可以当他是一个列表
        """
        return self.keys()

    def 值(self):
        """
        返回这个字典用的所有值
        :return: 一个可以循环遍历的对象，可以当他是一个列表
        """
        return self.values()

    def 键值对(self):
        """
        按键值对的形式返回字典中的所有元素，主要是用于循环字典
        :return:
        """
        return self.items()


class 列表(list):
    def 添加(self, __值: object) -> _空:
        """
        往列表中添加一个值
        :param __值: 任意值
        :return: 空
        """
        self.append(__值)

    def 获取值索引(self, __值: _任意值) -> _整数类型:
        """
        根据列表的值获取索引
        :param __值: 需要获取索引的值
        :return: 值在列表中所在的索引
        """
        return self.index(__值)

    def 弹出(self, __索引: _整数类型 = -1) -> _任意值:
        """
        根据索引，把值从列表中删除，并且把删除的值返回去。默认索引为-1，也就是弹出最后一个元素
        :param __索引: 需要弹出值的索引
        :return: 被弹出的值
        """
        return self.pop(__索引)

    def 删除(self, __值: _任意值) -> _空:
        """
        从列表中删除一个值
        :param __值: 任意值
        :return: 空
        """
        return self.remove(__值)
