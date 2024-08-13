import os

from common.log import logger
from web.boot import app
from config.setting import settings
from config.path_conf import BASE_DIR


def run():
    app.run(
        host=settings.WEB_HOST,
        port=settings.WEB_PORT,
        debug=settings.DEBUG,
        auto_reload=settings.DEBUG,
        workers=settings.WEB_WORKERS,
        reload_dir=[
            os.path.join(BASE_DIR, "game/页面"),
            os.path.join(BASE_DIR, "game/数据"),
        ],
    )


if __name__ == "__main__":
    run()
