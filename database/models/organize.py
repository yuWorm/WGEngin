from tortoise import fields

from database.models.base import BaseTable


class Organize(BaseTable):
    name = fields.CharField(max_length=255, unique=True, description="组织名称")
    desc = fields.TextField(description="组织介绍")
    # 组织的创建者/或者领导者
    leader = fields.ForeignKeyField(
        "models.Player", related_name="organizes", on_delete=fields.CASCADE
    )


class OrganizeMember(BaseTable):
    oid: int = fields.IntField(description="所属的组织")
    # 组织成员
    player = fields.ForeignKeyField(
        "models.Player", related_name="organize_member", on_delete=fields.CASCADE
    )
    job = fields.CharField(max_length=50, description="成员的职位")

    class Meta:
        table = "organize_member"


class OrganizeApply(BaseTable):
    # 申请的玩家
    player = fields.CharField(max_length=255, description="申请的玩家姓名")
    status = fields.CharField(max_length=10, description="申请的状态")
    reviewer = fields.CharField(max_length=255, description="审核人")

    class Meta:
        table = "organize_apply"
