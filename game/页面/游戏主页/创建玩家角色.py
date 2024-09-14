from game.核心.基础数据类型 import 文本类型
from game.核心.基类.游戏.页面 import 页面基类, 页面参数基类
from game.核心.页面.构建 import 页面构建类


class 角色信息(页面参数基类):
    玩家昵称: 文本类型


class 创建角色(页面基类):
    页面组 = "用户基类"

    async def 内容(self) -> 页面构建类 | None:
        pass
