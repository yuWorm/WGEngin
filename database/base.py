"""
基本数据表，后面会实现根据某些表来进行覆盖
"""

from .models.player import Player, PlayerSkill, PlayerTask
from .models.user import User, UserGroup, Permission
from .models.pet import Pet, PetSkill
from .models.bag import Bag, BagItem
from .models.chat import PrivateChat, PublicChat
from .models.organize import Organize, OrganizeMember, OrganizeApply
from game.db.rewirte import *

__all__ = [
    "User",
    "UserGroup",
    "Permission",
    "Player",
    "PlayerSkill",
    "PlayerTask",
    "Bag",
    "BagItem",
    "Pet",
    "PetSkill",
    "PrivateChat",
    "PublicChat",
    "Organize",
    "OrganizeMember",
    "OrganizeApply",
]
