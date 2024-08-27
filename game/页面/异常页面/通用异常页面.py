from game.核心.基础数据类 import 字典
from game.核心.基础数据类型 import 字典类型
from game.核心.基类.游戏.页面 import 页面基类
from game.核心.工具方法 import 页面
from game.核心.数据.注册游戏元素 import 添加页面
from game.核心.页面.构建 import 页面构建类, 创建页面
from game.页面 import 页面配置


class 通用异常(页面基类):

    页面组 = "异常页面"

    async def 内容(self) -> 页面构建类 | None:
        _页面 = 创建页面(f"{self.游戏名称} - 错误")
        _消息列表 = self.获取页面消息(_需要的消息类别=["异常"])
        for _消息 in _消息列表:
            _页面.段落(_消息, 样式=字典(字体颜色="红色"))

        _页面.段落.链接("返回首页", 链接地址="/")
        return _页面


添加页面(通用异常)
