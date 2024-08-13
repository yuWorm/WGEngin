from tortoise import fields

from database.models.base import BaseTable


class PrivateChat(BaseTable):
    # 私信表

    sender = fields.IntField(description="发送的用户")
    content = fields.TextField(description="消息内容")
    reciver = fields.IntField(description="接收的用户")
    status = fields.IntField(description="消息状态")

    class Meta:
        table = "private_chat"


class PublicChat(BaseTable):
    # 公聊消息

    content = fields.TextField(description="消息内容")
    channels = fields.CharField(max_length=255, description="消息频道")
    sender = fields.IntField(description="发送者, 0为系统")

    class Meta:
        table = "public_chat"
