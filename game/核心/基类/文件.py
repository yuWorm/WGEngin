from typing import TextIO, IO

from game.核心.基础属性 import 数据类型
from game.核心.基础异常 import 文件异常
from game.核心.基础数据类 import 列表, 文本
from game.核心.基础数据类型 import 空, 文本类型, 二进制数据, 任意值, 列表类型, 无


class 文件:
    文件对象: TextIO | IO | 空 = None

    def __init__(self, file: TextIO):
        if not file:
            raise 文件异常("文件对象不存在")
        self.文件对象 = file

    def 读取所有(self) -> 文本类型 | 二进制数据:
        """
        读取文件中的所有内容，如果是文本就返回整个文件的文本，如果是二进制数据，就返回整个文件的二进制。
        :return: 文本 | 二进制数据
        """
        __内容 = self.文件对象.read()
        if 数据类型(__内容) is str:
            return 文本(__内容)

        return __内容

    def 读取一行(self) -> 文本类型 | 二进制数据:
        """
        读取一行数据，读取完一行后，就会将文件读取指针移到下一行，可以理解为下次读就是读下一行，已经读取过的不会在读取了
        :return: 返回一行数据，为文本/二进制
        """
        __行 = self.文件对象.readline()
        if 数据类型(__行) is str:
            return 文本(__行)

        return __行

    def 读取所有行(self) -> 列表[文本类型 | 二进制数据]:
        """
        按行读取所有数据
        :return: 读取出来的是一个列表，存储着每一行数据
        """
        __所有行 = self.文件对象.readlines()
        return 列表(__所有行)

    def 写入(self, _内容: 文本类型 | 二进制数据) -> 无:
        """
        将数据写入到文件中，
        :param _内容: 要写入的内容，普通写入就是文本，二进制写入就是二进制数据
        :return: 无
        """
        self.文件对象.write(_内容)

    def 按行写入(self, _内容: 列表[文本类型 | 二进制数据]):

        self.文件对象.writelines(_内容)

    def 关闭文件(self):
        self.文件对象.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.文件对象:
            self.关闭文件()

    def __del__(self):
        if self.文件对象:
            if not self.文件对象.closed:
                self.关闭文件()
