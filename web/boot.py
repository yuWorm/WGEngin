# 启动文件夹
from sanic import Sanic
from . import listener
from . import middlewares
from . import router
from . import exts
from . import db

app = Sanic("WGEngineHttpService")
db.init(app)
listener.init(app)
middlewares.init(app)
router.init(app)
exts.init(app)
