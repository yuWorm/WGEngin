import hashlib

from tortoise import fields

from config.setting import settings
from database.models.base import BaseTable


class Permission(BaseTable):
    tag: str = fields.CharField(max_length=255, description="权限标签", unique=True)
    name = fields.CharField(max_length=255, description="权限名称")


class UserGroup(BaseTable):
    name: str = fields.CharField(max_length=100, description="用户组名称")
    permissions: fields.ManyToManyRelation["Permission"] = fields.ManyToManyField(
        "models.Permission", related_name="groups", through="user_permissions"
    )

    class Meta:
        table = "user_group"


class User(BaseTable):
    id = fields.IntField(pk=True, description="用户ID")
    uid = fields.IntField(unique=True, description="用户唯一ID，如100001")
    username = fields.CharField(
        unique=True, max_length=20, description="用户名，用于登录"
    )
    password = fields.CharField(max_length=255, null=True, description="密码")
    email = fields.CharField(
        unique=True, max_length=100, description="邮箱，主要用于找回密码"
    )
    is_staff = fields.BooleanField(default=False, description="是否禁用")
    can_login_admin = fields.BooleanField(default=False, description="是否可以登录后台")
    is_superuser = fields.BooleanField(default=False, description="是否是超级管理员")
    last_login = fields.DatetimeField(null=True)
    last_login_ip = fields.CharField(max_length=20, null=True)
    group: fields.ForeignKeyRelation["UserGroup"] = fields.ForeignKeyField(
        "models.UserGroup",
        related_name="users",
        null=True,
        on_delete=fields.OnDelete.SET_NULL,
    )

    def verify_password(self, password: str) -> bool:
        """
        验证密码是否正确
        :param password: 用户明文密码
        :return:
        """
        en_password = self.make_password(password)
        return en_password == self.password

    @classmethod
    def make_password(cls, password: str) -> str:
        """
        对用户密码进行加密存储
        :param password: 用户明文密码
        :return:
        """
        password_with_salt = f"{password}{settings.USER_PASSWORD_SALT}"
        sha256 = hashlib.sha256()
        sha256.update(password_with_salt.encode("utf-8"))
        return sha256.hexdigest()

    @classmethod
    async def register(
        cls, username, email, password, is_staff=False, is_superuser=False, group=None
    ):
        """
        注册游戏用户
        :return:
        """
        return await cls.create(
            username=username,
            email=email,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            group=group,
        )

    @classmethod
    async def register_game_user(cls, username, email, password):
        """
        注册游戏用户
        :param username: 用户名
        :param email: 用户邮箱
        :param password: 用户密码(明文)
        :return:
        """
        return await cls.register(username, email, password)
