import contextvars
import functools
import time
from typing import Any

from sanic.request import Request


def bind_context_var(context: contextvars.ContextVar) -> Any | Request:
    class ContextVarBind:
        __slots__ = ()

        def __getattribute__(self, name):
            return getattr(context.get(), name)

        def __setattr__(self, name, value):
            setattr(context.get(), name, value)

        def __delattr__(self, name):
            delattr(context.get(), name)

        def __getitem__(self, index, value):
            return context.get()[index]

        def __setitem__(self, index, value):
            context.get()[index] = value

        def __delitem__(self, index):
            del context.get()[index]

    return ContextVarBind()


class GlobalData:
    _data: dict[str, Any]

    def __init__(self):
        self._data = {}

    def __getattribute__(self, name):
        if name.startswith("_"):
            return super().__getattribute__(name)
        return self._data.get(name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            return super().__setattr__(name, value)
        self._data[name] = value

    def __delattr__(self, name):
        if name.startswith("_"):
            return super().__delattr__(name)
        del self._data[name]

    def __getitem__(self, index, value):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self.data[index]


# 用于游戏的全局请求上下文设置
request_var = contextvars.ContextVar("request")
r: Request = bind_context_var(request_var)

# 用于游戏的全局数据上下文设置
globals_var = contextvars.ContextVar("globals")
g: GlobalData = bind_context_var(globals_var)


def context_bind(func):
    @functools.wraps(func)
    async def wrapper(req: Request, *args, **kwargs):
        start_time = time.time()
        # 注册全局上下文
        request_var_token = request_var.set(req)
        global_var_token = globals_var.set(GlobalData())
        g.start_time = start_time
        resp = await func(r, *args, **kwargs)
        # 注销全局上下文，主要供给游戏使用
        request_var.reset(request_var_token)
        globals_var.reset(global_var_token)
        return resp

    return wrapper
