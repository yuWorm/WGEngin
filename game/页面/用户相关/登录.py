from common.context import r
from common.log import logger
from game.核心.基础属性 import 获取数据长度
from game.核心.基础异常 import 类型检测异常, 类参数异常
from game.核心.基础数据类 import 字典, 列表, 文本
from game.核心.基础数据类型 import 字典类型, 文本类型
from game.核心.基类.游戏.页面 import 页面基类, 页面参数基类
from game.核心.工具方法 import 页面
from game.核心.基类.游戏.用户 import 用户类
from game.核心.数据.注册游戏元素 import 添加页面
from game.核心.页面.构建 import 创建页面
from game.游戏配置 import 游戏名称, 游戏副标题
from game.页面 import 页面配置


class 登录信息(页面参数基类):
    用户名: 文本类型
    密码: 文本类型


class 登录(页面基类):
    页面组 = "用户相关"

    _异常信息 = 列表([])
    页面参数类 = 登录信息
    页面参数: 登录信息

    def __init__(self):
        super().__init__()
        self._异常信息 = 列表([])

    def 解析页面参数(self, _参数: 字典类型):
        """
        关闭自动解析页面数据
        :param _参数:
        :return:
        """
        if r.method == "GET":
            return
        try:
            self.页面参数 = self.页面参数类(**_参数)
        except (类型检测异常, 类参数异常) as e:
            self._异常信息.添加(文本(e))

    async def 登录逻辑处理(self):
        if r.method == "GET":
            return

        if 获取数据长度(self._异常信息) > 0:
            return

        _用户 = await 用户类.通过用户名获取用户(self.页面参数.用户名)
        if not _用户:
            self._异常信息.添加("用户名或密码错误")
            return

        if not _用户.校验密码(self.页面参数.密码):
            self._异常信息.添加("用户名或密码错误")
            return

        r.ctx.session["user_id"] = _用户.id
        页面.跳转页面("/")

    async def 内容(self):
        await self.登录逻辑处理()

        _页面 = 创建页面(f"{游戏名称}-登录页面")
        _页面.四级标题(f"{游戏名称} - {游戏副标题}")
        if self._异常信息:
            for _信息 in self._异常信息:
                _页面.段落(_信息, 样式=字典(字体颜色="红色"))
        with _页面.表单(表单提交类型="post", 表单提交地址=""):
            _页面.段落.标签("用户名: ").输入框(
                类型="文本", 输入提示="请输入你的用户名", 名称="用户名"
            )
            _页面.段落.标签("密码: ").输入框(
                类型="密码", 输入提示="请输入你的密码", 名称="密码"
            )
            _页面.段落.输入框(类型="提交", 值="登录", 样式=字典(左外边距="10px"))
            with _页面.链接(链接地址=页面.获取页面路径(页面配置.注册页面)):
                _页面.输入框(类型="按钮", 值="前往注册", 样式=字典(左外边距="10px"))
        return _页面

    async def 页面数据(self) -> 字典类型:
        await self.登录逻辑处理()
        _注册页面地址 = 页面.获取页面路径(页面配置.注册页面)
        return 字典({"异常信息": self._异常信息, "注册地址": _注册页面地址})


添加页面(登录)
