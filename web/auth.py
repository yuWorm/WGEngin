import functools

from sanic import Request
from database.base import User


def user_info(func):
    @functools.wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        user_id = request.ctx.session.get("user_id")
        user = None
        if user_id:
            user = await User.filter(id=user_id).first()
            if not user:
                request.ctx.session.pop("user_id")
            else:
                request.ctx.g.是否登录 = True
                request.ctx.g.用户 = user
        resp = await func(request, *args, **kwargs)
        return resp

    return wrapper
