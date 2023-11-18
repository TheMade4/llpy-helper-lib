from typing import TypedDict

class T_TimeObj(TypedDict):
    """Time object obtained from `system.getTimeObj()`"""

    Y: int
    """Year value (4 digits)"""
    M: int
    """Month value"""
    D: int
    """Day value"""
    h: int
    """Hour value (24-hour format)"""
    m: int
    """Minute value"""
    s: int
    """Second value"""
    ms: int
    """Millisecond value"""
