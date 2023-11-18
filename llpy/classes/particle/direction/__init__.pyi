from typing import NoReturn

from ..types import (
    T_PosDirection_NEG_X,
    T_PosDirection_NEG_Y,
    T_PosDirection_NEG_Z,
    T_PosDirection_POS_X,
    T_PosDirection_POS_Y,
    T_PosDirection_POS_Z,
)

class Direction:
    """Particle Spawner Direction Enumeration"""

    def __init__(self) -> NoReturn: ...

    NEG_Y: T_PosDirection_NEG_Y
    """Particle direction enumeration | -Y"""
    POS_Y: T_PosDirection_POS_Y
    """Particle direction enumeration | +Y"""
    NEG_Z: T_PosDirection_NEG_Z
    """Particle direction enumeration | -Z"""
    POS_Z: T_PosDirection_POS_Z
    """Particle direction enumeration | +Z"""
    NEG_X: T_PosDirection_NEG_X
    """Particle direction enumeration | -X"""
    POS_X: T_PosDirection_POS_X
    """Particle direction enumeration | +X"""
