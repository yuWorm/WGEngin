from common.context import r
from game.核心.基础数据类型 import 字典类型, 是
from game.核心.基类.游戏.页面 import 页面基类
from game.核心.工具方法 import 页面
from game.核心.数据.注册游戏元素 import 添加页面
from game.页面 import 页面配置


class 登出(页面基类):

    页面组 = "用户相关"
    无输出页面 = 是

    async def 页面数据(self) -> 字典类型:
        _用户ID = r.ctx.session.get("user_id")
        if _用户ID:
            r.ctx.session.pop("user_id")
        页面.跳转页面(页面配置.登录页面)


添加页面(登出)
