from typing import Literal, overload

from llpy import ParticleColor
from llpy.types import T_Number, T_PosType

from ..types import T_ParticleColor, T_ParticleNumber, T_ParticleSize, T_PosDirection


class ParticleSpawner:
    """Particle Spawner Object"""

    def __init__(
            self,
            display_radius: int,
            high_detail: bool,
            double_side: bool,
    ) -> None:
        """
        Generate a particle spawner object

        Args:
            display_radius: Particle display radius
            high_detail: Requires high-detail lines
            double_side: Requires double-sided particles
        """

    @property
    def displayRadius(self) -> int:
        """Particle display radius"""

    @property
    def highDetail(self) -> bool:
        """Requires high-detail lines"""

    @property
    def doubleSide(self) -> bool:
        """Requires double-sided particles"""

    @displayRadius.setter
    def displayRadius(self, val: int): ...

    @highDetail.setter
    def highDetail(self, val: bool): ...

    @doubleSide.setter
    def doubleSide(self, val: bool): ...

    def spawnParticle(self, pos: T_PosType, name: str) -> Literal[True]:
        """
        Generate a particle with the specified name

        Args:
            pos: Can be floating-point or integer coordinates. Integer coordinates will take the center point of the block.
            name: Particle name

        Returns:
            `True`
        """

    def drawPoint(
            self,
            pos: T_PosType,
            point_size: T_ParticleSize = 4,
            color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        Generate a point particle

        Args:
            pos: Can be floating-point or integer coordinates. Integer coordinates will take the center point of the block.
            point_size: Particle size
            color: Particle color. Should use the `ParticleColor` enum for filling.

        Returns:
            `True`
        """

    def drawNumber(
            self,
            pos: T_PosType,
            num: T_ParticleNumber,
            color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        Generate a number particle

        Args:
            pos: Can be floating-point or integer coordinates. Integer coordinates will take the center point of the block.
            num: Particle content
            color: Particle color. Should use the `ParticleColor` enum for filling.

        Returns:
            `True`
        """

    def drawAxialLine(
            self,
            pos: T_PosType,
            direction: T_PosDirection,
            length: T_Number,
            color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        Generate an axial line segment

        Args:
            pos: Starting point of the line segment. Can be floating-point or integer coordinates. Integer coordinates will take the center point of the block.
            direction: Line segment direction. Should use the `Direction` enum for filling.
            length: Line segment length
            color: Particle color. Should use the `ParticleColor` enum for filling.

        Returns:
            `True`
        """

    def drawOrientedLine(
            self,
            start: T_PosType,
            end: T_PosType,
            line_width: T_ParticleSize = 4,
            min_spacing: T_Number = 1,
            max_particles_num: int = 64,
            color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        Generate an oriented line segment

        Args:
            start: Starting point of the line segment. Can be floating-point or integer coordinates. Integer coordinates will take the center point of the block.
            end: End point of the line segment. Can be floating-point or integer coordinates. Integer coordinates will take the center point of the block.
            line_width: Line segment width
            min_spacing: Minimum spacing between line segment points
            max_particles_num: Maximum number of particles in the line segment. It will automatically increase the spacing after reaching this number.
            color: Particle color. Should use the `ParticleColor` enum for filling.

        Returns:
            `True`
        """

    @overload
    def drawCuboid(
            self,
            pos: T_PosType,
            color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        Generate a cuboid

        Draw a 1×1×1 size cuboid

        Args:
            pos: Can be floating-point or integer coordinates. Integer coordinates will take the bottom corner position of the block.
            color: Particle color. Should use the `ParticleColor` enum for filling.

        Returns:
            `True`
        """

    @overload
    def drawCuboid(
            self,
            pos: T_PosType,
            pos2: T_PosType,
            color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        Generate a cuboid

        Draw a cuboid from the minimum corner `pos` to the maximum corner `pos2`

        Args:
            pos: Can be floating-point or integer coordinates. Integer coordinates will take the bottom corner position of the block.
            pos2: Can be floating-point or integer coordinates. Integer coordinates will take the top corner position of the block.
            color: Particle color. Should use the `ParticleColor` enum for filling.

        Returns:
            `True`
        """

    def drawCircle(
            self,
            pos: T_PosType,
            facing: T_PosDirection,
            radius: T_Number,
            line_width: T_ParticleSize = 4,
            min_spacing: T_Number = 1,
            max_particles_num: int = 64,
            color: T_ParticleColor = ParticleColor.White,
    ) -> Literal[True]:
        """
        Generate a circle

        Args:
            pos: Center of the circle. Can be floating-point or integer coordinates. Integer coordinates will take the center point of the block.
            facing: Facing direction. Should use the `Direction` enum for filling.
            radius: Radius
            line_width: Width of the circular line segment
            min_spacing: Minimum spacing between circular line segment points
            max_particles_num: Maximum number of particles in the circle. It will automatically increase the spacing after reaching this number.
            color: Particle color. Should use the `ParticleColor` enum for filling.

        Returns:
            `True`
        """
