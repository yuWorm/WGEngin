import abc

from game.核心.基础属性 import 基础类, 类基础属性, 类基础方法, 类属性

from game.核心.基础数据类型 import 文本类型, 整数类型, 是或否, 是
from game.核心.基类.元类 import 固定属性元类


class 技能基类(基础类, metaclass=固定属性元类):
    技能名称: 文本类型
    技能介绍: 文本类型
    技能最大等级: 整数类型
    技能图标: 文本类型

    _需要的属性 = ["技能名称", "技能介绍", "技能最大等级"]

    __是否为基类: 是或否 = 是

    @abc.abstractmethod
    def 学习要求检测(self):
        """
        检测是否符合学习技能的要求
        :return:
        """

    @abc.abstractmethod
    def 施放(self):
        """
        施放技能，效果啥的都在里面，这个技能能干嘛都在这里面
        :return:
        """

    @abc.abstractmethod
    def 升级(self):
        """
        用于技能升级的时候调用，可以在里面写条件，写一些要求
        :return:
        """

    @property
    @abc.abstractmethod
    def 是否可升级(self) -> 是或否:
        """
        这里用来写判断，写判断是否可以进行升级
        :return:
        """
