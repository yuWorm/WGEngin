from typing import re

from common.context import r
from game.核心.基础属性 import 获取数据长度
from game.核心.基础异常 import 类型检测异常
from game.核心.基础数据类 import 列表, 文本, 字典
from game.核心.基础数据类型 import 字典类型, 文本类型, 列表类型, 是
from game.核心.基类.游戏.用户 import 用户类
from game.核心.基类.游戏.页面 import 页面基类, 页面参数基类
from game.核心.工具方法 import 页面
from game.核心.工具方法.数据 import 判断是否为纯文本或数字
from game.核心.数据.注册游戏元素 import 添加页面
from game.核心.页面.构建 import 页面构建类, 创建页面

from game.页面 import 页面配置


class 注册信息(页面参数基类):
    用户名: 文本类型
    邮箱: 文本类型
    密码: 文本类型
    确认密码: 文本类型

    @staticmethod
    def 校验_用户名(_用户名: 文本类型):
        _用户名 = 文本(_用户名)

        if not _用户名.去空():
            return "用户名不可为空"

        if 获取数据长度(_用户名) < 4:
            return "用户名长度必须大于4"

        if 获取数据长度(_用户名) > 20:
            return "用户名长度不可大于20"

        if not 判断是否为纯文本或数字(_用户名):
            return "用户名必须为字母/字母数字组合/数字"

        return True

    @staticmethod
    def 校验_邮箱(_邮箱: 文本类型):
        _邮箱 = 文本(_邮箱)

        _可使用的邮箱 = [
            # 中国常用邮箱
            "qq.com",
            "163.com",
            "126.com",
            "yeah.net",
            "sina.com",
            "sina.cn",
            "sohu.com",
            "exmail.qq.com",
            "aliyun.com",
            "huawei.com",
            "21cn.com",
            # 国外常用邮箱
            "gmail.com",
            "outlook.com",
            "hotmail.com",
            "yahoo.com",
            "icloud.com",
            "aol.com",
            "protonmail.com",
        ]

        if not _邮箱.去空():
            return "邮箱不可为空"

        _邮箱名_后缀 = _邮箱.分割("@")
        if 获取数据长度(_邮箱名_后缀) != 2:
            return "邮箱格式错误"

        if _邮箱名_后缀[-1] not in _可使用的邮箱:
            return "不支持使用当前邮箱注册"

        return True

    @staticmethod
    def 校验_密码(_密码):
        if 获取数据长度(_密码) < 6:
            return "密码长度必须大于6"

        if 获取数据长度(_密码) > 30:
            return "密码长度必须小于30"

        return True


class 注册(页面基类):

    页面组 = "用户相关"

    页面参数类 = 注册信息
    页面参数: 注册信息

    _异常信息: 列表类型
    _成功信息: 列表类型

    def __init__(self):
        super().__init__()
        self._异常信息 = 列表([])
        self._成功信息 = 列表([])

    def 解析页面参数(self, _参数: 字典类型):
        """

        :param _参数:
        :return:
        """
        if r.method == "GET":
            return
        try:
            self.页面参数 = self.页面参数类(**_参数)
        except 类型检测异常 as e:
            self._异常信息.添加(文本(e))

    async def 注册逻辑处理(self):
        if r.method == "GET":
            return

        if self._异常信息:
            return

        if self.页面参数.密码 != self.页面参数.确认密码:
            self._异常信息.添加("两次输入密码不一致")
            return

        _用户 = await 用户类.通过用户名获取用户(self.页面参数.用户名)
        if _用户:
            self._异常信息.添加("用户名已被占用, 请重新输入")
            return

        _用户 = await 用户类.通过邮箱获取用户(_邮箱=self.页面参数.邮箱)
        if _用户:
            self._异常信息.添加(
                "该邮箱已注册过账号,您是否忘记了密码,请前往找回,请重新输入"
            )
            return

        _用户 = await 用户类.注册(
            self.页面参数.用户名, self.页面参数.密码, self.页面参数.邮箱
        )
        if not _用户:
            self._异常信息.添加("注册失败,请联系管理团队")
            return

        self._成功信息.添加(f"{_用户.用户名}注册成功, 请前往登录")

    async def 内容(self) -> 页面构建类 | None:
        await self.注册逻辑处理()
        _页面 = 创建页面(f"{self.游戏名称}-注册")

        _页面.四级标题(f"{self.游戏名称} - {self.游戏副标题}")
        if self._异常信息:
            for _信息 in self._异常信息:
                _页面.段落(_信息, 样式=字典(字体颜色="红色"))

        if self._成功信息:
            for _信息 in self._成功信息:
                _页面.段落(_信息, 样式=字典(字体颜色="绿色"))

        with _页面.表单(表单提交类型="post", 表单提交地址=""):
            _页面.段落.标签("用户名: ").输入框(
                类型="文本", 输入提示="请输入你的用户名", 名称="用户名", 是否必填=是
            )
            _页面.段落.标签("邮箱: ").输入框(
                类型="邮箱", 输入提示="请输入你的用户名", 名称="邮箱", 是否必填=是
            )
            _页面.段落.标签("密码: ").输入框(
                类型="密码", 输入提示="请输入你的密码", 名称="密码", 是否必填=是
            )
            _页面.段落.标签("确认密码: ").输入框(
                类型="密码", 输入提示="请输入你的密码", 名称="确认密码", 是否必填=是
            )
            _页面.段落.输入框(类型="提交", 值="注册", 样式=字典(左外边距="10px"))
            with _页面.链接(链接地址=页面.获取页面路径(页面配置.登录页面)):
                _页面.输入框(类型="按钮", 值="前往登录", 样式=字典(左外边距="10px"))
        return _页面

    async def 页面数据(self) -> 字典类型:
        await self.注册逻辑处理()
        _登录页面地址 = 页面.获取页面路径(页面配置.登录页面)
        return 字典(
            {
                "异常信息": self._异常信息,
                "成功信息": self._成功信息,
                "登录地址": _登录页面地址,
            }
        )


添加页面(注册)
