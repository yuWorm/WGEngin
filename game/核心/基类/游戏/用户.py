import hashlib
from datetime import datetime

from config.setting import settings
from game.核心.基础数据类 import 字典
from game.核心.基础数据类型 import 文本类型, 是或否
from game.核心.基类.数据库映射 import 数据库映射类
from game.核心.工具方法.数据库 import 数据库工具


class 用户类(数据库映射类):
    _表名 = "用户"

    用户名: 文本类型
    密码: 文本类型
    是否禁用: 是或否
    上次登录时间: datetime
    上次登录IP: 文本类型
    注册时间: datetime

    @classmethod
    async def 注册(cls, _用户名: 文本类型, _密码: 文本类型, _邮箱: 文本类型):
        _用户数据 = {"用户名": _用户名, "邮箱": _邮箱, "密码": cls.对密码加密(_密码)}
        _添加结果 = await 数据库工具[cls._表名].添加一条数据(_用户数据)
        _用户 = cls()
        _用户.解析数据(字典(_用户数据))
        return _用户

    @classmethod
    def 对密码加密(cls, _未加密的密码: 文本类型):
        password_with_salt = f"{_未加密的密码}{settings.USER_PASSWORD_SALT}"
        sha256 = hashlib.sha256()
        sha256.update(password_with_salt.encode("utf-8"))
        return sha256.hexdigest()

    def 校验密码(self, _密码):
        return self.密码 == self.对密码加密(_密码)

    @classmethod
    async def 通过用户名获取用户(cls, _用户名: 文本类型):
        return await cls.获取({"用户名": _用户名})

    @classmethod
    async def 通过邮箱获取用户(cls, _邮箱: 文本类型):
        return await cls.获取({"邮箱": _邮箱})

    @classmethod
    async def 数据库设置(cls):
        await 数据库工具[cls._表名].设置索引({"用户名": 1, "邮箱": 1}, {"unique": True})
