from game.核心.基础数据类型 import 字典类型
from game.核心.基类.游戏.页面 import 页面基类
from game.核心.数据.注册游戏元素 import 添加页面


class 通用异常(页面基类):
    页面组 = "异常页面"

    async def 页面数据(self) -> 字典类型:
        _消息 = self.获取页面消息(_需要的消息类别=["异常"])
        _消息内容 = "<br>".join(_消息)
        return {"异常信息": _消息内容}


添加页面(通用异常)
