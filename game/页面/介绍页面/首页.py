from game.核心.基础数据类型 import 字典类型
from game.核心.基类.游戏.页面 import 页面基类
from game.核心.数据.注册游戏元素 import 添加页面


class 首页(页面基类):
    页面组 = "介绍页面"

    async def 页面数据(self) -> 字典类型:
        return {}


添加页面(首页)
