from tortoise import fields

from database.models.base import BaseTable


class Bag(BaseTable):
    capacity: int = fields.IntField(default=0, description="背包容量")
    player_id: int = fields.IntField(description="玩家ID", unique=True)
    used_capacity: int = fields.IntField(default=0, description="已使用的容量")
    items: fields.ManyToManyRelation["BagItem"] = fields.ManyToManyField(
        "models.BagItem", related_name="bags", through="bag_items"
    )
    ext_fields = fields.JSONField(default={}, description="背包拓展字段")


class BagItem(BaseTable):
    item: str = fields.CharField(
        max_length=255,
        description="物品名称，物品是直接加载在内存当中的，所以直接存名称就好了",
    )
    ext_fields = fields.JSONField(default={}, description="物品的拓展字段")
    count = fields.IntField(default=1, description="物品数量，需要可以叠加")

    class Meta:
        table = "bag_item"
