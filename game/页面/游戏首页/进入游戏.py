from bson import ObjectId

from common.context import g
from game.核心.基础数据类 import 字典
from game.核心.基础数据类型 import 字典类型
from game.核心.基类.游戏.玩家 import 玩家类
from game.核心.基类.游戏.页面 import 页面基类
from game.核心.工具方法 import 页面
from game.核心.数据.注册游戏元素 import 添加页面
from game.核心.页面.构建 import 页面构建类, 创建页面
from game.页面 import 页面配置


class 进入游戏(页面基类):

    页面组 = "游戏首页"

    async def 检测玩家是否存在(self):
        """
        如果有多个区, 就可以在这里做查询获取区分
        :return:
        """
        _角色 = await 玩家类.获取({"用户ID", ObjectId(g.用户.用户ID)})
        if not _角色:
            页面.跳转页面(页面.获取页面路径(页面配置.创建角色))

    async def 内容(self) -> 页面构建类 | None:
        # await self.检测玩家是否存在()
        _页面 = 创建页面(f"{self.游戏名称}-进入游戏")
        _页面.段落("即将进入游戏").文本("4", id="second").文本("...")
        _页面.链接("立即进入", 链接地址=页面配置.游戏主页, 样式=字典(左外边距="10px"))

        _页面.添加JS(
            """
            let second = 4
            const secondEl = document.getElementById('second');
            let interval = setInterval(function(){
                second--;
                secondEl.innerText = second;
                if(second < 1){
                    interval = null;
                    window.open('<游戏主页>','_self')
                }
            }, 1000)
            """.replace(
                "<游戏主页>", 页面.获取页面路径(页面配置.游戏主页)
            )
        )
        return _页面


添加页面(进入游戏)
