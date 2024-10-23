"""
程序的全局配置文件，从.env文件中读取
"""

import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from config.path_conf import BASE_DIR


class Settings(BaseSettings):
    # 从文件中读取配置
    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # 是否开启DEBUG，仅限于开发模式
    DEBUG: bool = False

    # 环境，dev开发环境，pro生产环境
    ENVIRONMENT: Literal["dev", "pro"]

    # 加密的一些配置
    USER_PASSWORD_SALT: str = "sdjne329@($)ASH@)@%&SDbqop234"  # 用户密码加盐字符
    GAME_DATA_SECRET: str  # 游戏url加密秘钥

    # web 服务配置
    WEB_HOST: str = "127.0.0.1"
    WEB_PORT: int = 6000
    WEB_DOMAIN: str = "127.0.0.1"
    WEB_WORKERS: int = 1  # web服务的进程数

    # 数据库配置
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_CHARSET: str = "utf8mb4"

    # REDIS配置
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_DATABASE: int
    REDIS_TIMEOUT: int = 5
    SESSION_EXPIRE_TIME: int = 60 * 60 * 2

    # mongodb 配置
    MONGO_HOST: str = "127.0.0.1"
    MONGO_PORT: int = 27017
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_DATABASE: str = "wgengine"

    # JWT Token 相关配置
    TOKEN_SECRET_KEY: str  # 登录token的加密秘钥
    TOKEN_ALGORITHM: str = "HS256"  # 算法
    TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 1  # 过期时间，单位：秒
    TOKEN_REFRESH_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # 刷新过期时间，单位：秒
    TOKEN_REDIS_PREFIX: str = "admin_token"
    TOKEN_REFRESH_REDIS_PREFIX: str = "admin_refresh_token"


@lru_cache
def get_settings() -> Settings:
    """获取全局配置"""
    return Settings()


# 创建配置实例
settings = get_settings()
