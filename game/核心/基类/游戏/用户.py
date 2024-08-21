import hashlib
from datetime import datetime

from config.setting import settings
from game.核心.基础数据类型 import 文本类型, 是或否


class 用户:
    用户名: 文本类型
    密码: 文本类型
    是否禁用: 是或否
    上次登录时间: datetime
    上次登录IP: 文本类型
    注册时间: datetime

    def 注册(self):
        pass

    @classmethod
    def 对密码加密(cls, _未加密的密码: 文本类型):
        password_with_salt = f"{_未加密的密码}{settings.USER_PASSWORD_SALT}"
        sha256 = hashlib.sha256()
        sha256.update(password_with_salt.encode("utf-8"))
        return sha256.hexdigest()

    def 校验密码(self, _密码):
        return self.密码 == self.对密码加密(_密码)

    def 通过用户名获取用户(self):
        pass

    def 通过邮箱获取用户(self):
        pass
