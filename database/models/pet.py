# 宠物相关
from tortoise import fields

from database.models.base import BaseTable


class Pet(BaseTable):

    name: str = fields.CharField(max_length=255, description="宠物名称")
    image: str = fields.CharField(max_length=255, null=True, description="宠物图片")
    skills: fields.ManyToManyRelation["PetSkill"] = fields.ManyToManyField(
        "models.PetSkill", related_name="pets", through="pet_skills"
    )
    atts: dict = fields.JSONField(default={}, description="宠物的属性")
    ext_fields: dict = fields.JSONField(
        default={}, description="宠物拓展字段，用于添加一些拓展数据"
    )
    equipments: dict = fields.JSONField(default={}, description="宠物装备")


class PetSkill(BaseTable):
    name: str = fields.CharField(
        max_length=255,
        description="宠物技能名称，技能存储在内存中，所以只需要存储名称就好了",
    )
    level: int = fields.IntField(default=1, description="宠物技能等级")
    exp: int = fields.IntField(default=0, description="宠物技能经验")
    ext_fields: dict = fields.JSONField(
        default={}, description="宠物技能拓展字段，用于添加一些拓展数据"
    )

    class Meta:
        table = "pet_skill"
