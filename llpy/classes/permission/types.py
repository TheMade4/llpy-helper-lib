from typing import TypedDict

from llpy.types import T_ToJsonDict


class T_PermInfo(TypedDict):
    """Permission Information"""

    name: str
    """Permission name"""
    enabled: bool
    """Whether it is enabled"""
    extra: T_ToJsonDict | None
    """Additional data"""
