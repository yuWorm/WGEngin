import os.path
import tomllib
import tomli_w

from game.核心.基础数据类 import 文本
from game.核心.基础数据类型 import 文本类型
from game.核心.基类.数据类 import 基础数据结构


class 游戏配置类(基础数据结构):
    _data: dict
    _toml_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "游戏配置.toml"
    )
    游戏名称: 文本类型
    游戏副标题: 文本类型
    游戏介绍: 文本类型

    def __init__(self):
        data = self.laod()
        self._data = data
        super().__init__(**data)

    def __getattr__(self, name: str):
        if name[0] == "_":
            return object.__getattribute__(self, name)
        return self._data.get(name)

    def __setattr__(self, name: str, value):
        if name[0] == "_":
            return object.__setattr__(self, name, value)

        self._data[name] = value
        self.__dict__[name] = value

    @property
    def data(self):
        return self._data

    def laod(self) -> dict:
        with open(self._toml_file, "r", encoding="utf-8") as f:
            return tomllib.loads(f.read())

    def save(self):
        with open(self._toml_file, "wb", encoding="utf-8") as f:
            tomli_w.dump(self.data, f)

    @classmethod
    def 校验_游戏名称(cls, value: 文本类型):
        if len(value) > 20:
            return "游戏名称不可超过20字"

        return True

    @classmethod
    def 校验_游戏副标题(cls, value: 文本类型):
        if len(value) > 80:
            return "游戏副标题不可超过80字"

        return True

    @classmethod
    def 校验_游戏介绍(cls, value: 文本类型):
        if len(value) > 80:
            return "游戏介绍不可超过200字"

        return True


游戏配置 = 游戏配置类()
