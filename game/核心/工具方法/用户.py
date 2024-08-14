from game.核心.基础数据类型 import 是或否, 整数类型, 文本类型, 空
from database.base import User


async def 通过ID获取用户(_用户ID: 整数类型) -> User | 空:
    return await User.filter(id=_用户ID).first()


async def 通过用户名获取用户(_用户名: 文本类型) -> User | 空:
    return await User.filter(username=_用户名).first()


async def 通过邮箱获取用户(_邮箱: 文本类型) -> User | 空:
    return await User.filter(username=_邮箱).first()


def 校验用户密码是否正确(_用户: User, _密码: 文本类型) -> 是或否:
    return _用户.verify_password(_密码)


async def 注册用户(_用户名: 文本类型, _用户密码: 文本类型, _用户邮箱: 文本类型):
    return await User.register_game_user(_用户名, _用户邮箱, _用户密码)
