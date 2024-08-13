from tortoise import fields
from database.models.base import BaseTable


class Player(BaseTable):
    uid: int = fields.IntField(description="玩家用户ID")
    pid: int = fields.IntField(unique=True, description="玩家ID")
    nickname: str = fields.CharField(
        unique=True, max_length=255, description="玩家昵称"
    )
    avatar: str = fields.CharField(max_length=255, null=True, description="玩家头像")
    profession: str = fields.CharField(
        max_length=255, null=True, description="玩家职业"
    )
    hp: int = fields.IntField(default=0, description="玩家血条")
    mp: int = fields.IntField(default=0, description="玩家蓝条")
    equipments: dict = fields.JSONField(default={}, description="玩家装备")
    # 玩家关联的技能
    skills: fields.ManyToManyRelation["PlayerSkill"] = fields.ManyToManyField(
        "models.PlayerSkill", related_name="players", through="player_skills"
    )
    # 玩家关联的任务
    tasks: fields.ManyToManyRelation["PlayerSkill"] = fields.ManyToManyField(
        "models.PlayerTask", related_name="players", through="player_tasks"
    )
    # 玩家的宠物们
    pets: fields.ManyToManyRelation["Pet"] = fields.ManyToManyField(
        "models.Pet", related_name="players", through="player_pets"
    )
    level: int = fields.IntField(default=1, description="玩家等级")
    title: list[str] = fields.JSONField(default=[], description="玩家称号，可多个")
    exp: int = fields.BigIntField(default=0, description="玩家经验值")
    # 玩家好友
    friends: fields.ManyToManyRelation["Player"] = fields.ManyToManyField(
        "models.Player",
        related_name="friend_of",
        through="player_friends",
        lazy=True,
    )
    attrs: dict = fields.JSONField(default={}, description="玩家的属性")
    organize = fields.CharField(
        max_length=255,
        null=True,
    )
    team: str = fields.CharField(
        max_length=255,
        null=True,
        description="玩家队伍，队伍存在redis当中，所以只存队伍名称",
    )
    current_position: str = fields.CharField(
        max_length=255,
        description="玩家当前所在地点，地图直接存在内存中，所以直接为存成名字",
    )
    is_instance_dungeon: bool = fields.BooleanField(
        null=True, default=False, description="是否在副本中"
    )
    ext_fields: dict = fields.JSONField(
        default={}, description="玩家拓展字段，可以用于拓展一些信息，添加游戏趣味性"
    )


class PlayerSkill(BaseTable):
    # 玩家拥有的技能表，所有技能原型存在于内存中

    name: str = fields.CharField(
        max_length=255,
        description="技能名称，直接用这个去关联技能，由于技能直接存储在内存中，所以直接使用名字来进行加载",
    )
    level: int = fields.IntField(default=1, description="技能等级")
    exp: int = fields.BigIntField(default=0, description="技能的经验值，也就是熟练度")
    ext_fields: dict = fields.JSONField(
        default={}, description="技能拓展的字段，就看使用方式了"
    )

    class Meta:
        table = "player_skill"


class PlayerTask(BaseTable):
    task = fields.CharField(
        max_length=255,
        description="对应的任务，任务存储在内存中，所以只需要保存任务名称就行了",
    )
    schedule = fields.JSONField(default={}, description="任务进度")
    status = fields.CharField(max_length=255, description="任务状态")
    ext_fields: dict = fields.JSONField(default={}, description="任务拓展的字段")

    class Meta:
        table = "player_task"
