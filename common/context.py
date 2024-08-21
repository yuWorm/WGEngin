import contextvars
import functools
import time
from types import SimpleNamespace
from typing import Any, Type

from sanic.request import Request
from sanic_session import Session

from database.models.user import User


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
    用户: User
    是否登录: bool

    def __init__(self):
        self._data = {}

    def __getattr__(self, name):
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


class CustomRequestCtx(SimpleNamespace):
    g: GlobalData
    session: dict


class CustomRequest(Request):
    ctx: CustomRequestCtx


# 用于游戏的全局请求上下文设置
request_var = contextvars.ContextVar("request")
r: Type[CustomRequest] = bind_context_var(request_var)


def context_bind(func):
    @functools.wraps(func)
    async def wrapper(req: Request, *args, **kwargs):
        start_time = time.time()
        # 注册全局上下文
        req.ctx.g = GlobalData()
        request_var_token = request_var.set(req)
        req.ctx.g.start_time = start_time
        resp = await func(r, *args, **kwargs)
        # 注销全局上下文，主要供给游戏使用
        request_var.reset(request_var_token)
        return resp

    return wrapper
