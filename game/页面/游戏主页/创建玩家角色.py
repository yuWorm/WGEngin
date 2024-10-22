from common.context import r
from game.核心.基础数据类 import 字典
from game.核心.基础数据类型 import 文本类型, 是, 是或否
from game.核心.基础方法 import 校验数据类型
from game.核心.基类.游戏.页面 import 页面基类, 页面参数基类
from game.核心.数据.注册游戏元素 import 添加页面
from game.核心.页面.构建 import 页面构建类, 创建页面
from game.核心.基类.游戏.玩家 import 玩家类


class 角色信息(页面参数基类):
    昵称: 文本类型
    性别: 文本类型


class 创建角色(页面基类):
    页面组 = "用户基类"
    # 页面参数类 = 角色信息
    # 页面参数: 角色信息

    async def 创建角色(self):
        return False

    @classmethod
    def 创建角色表单(cls, _页面: 页面构建类):
        with _页面.表单(表单提交类型="post", 表单提交地址=""):
            _页面.段落.标签("昵称: ").输入框(
                类型="文本", 输入提示="请输入你的昵称", 名称="昵称", 是否必填=是
            )
            _页面.段落.标签("性别: ").输入框(
                "男",
                类型="单选框",
                输入提示="请输入你的昵称",
                名称="性别",
                值="男",
                是否必填=是,
            ).输入框(
                "女",
                类型="单选框",
                输入提示="请输入你的昵称",
                名称="性别",
                值="女",
                是否必填=是,
            ).输入框(
                "未知",
                类型="单选框",
                输入提示="请输入你的昵称",
                名称="性别",
                值="未知",
                是否必填=是,
            )
            _页面.段落.输入框(类型="提交", 值="创建角色", 样式=字典(左外边距="50px"))

    async def 内容(self) -> 页面构建类 | None:
        # 如果请求为post, 执行创建操作
        if r.method == "POST":
            _创建返回信息 = self.创建角色()

            if 校验数据类型(_创建返回信息, 是或否):
                pass
        _页面 = 创建页面(f"{self.游戏名称}-创建角色")
        _页面.三级标题("创建角色")
        _页面.段落("你还没有创建角色,请先创建角色")
        self.创建角色表单(_页面)
        return _页面


添加页面(创建角色)
