from typing import NoReturn

from llpy import LLSE_Player

from .types import T_ScoreDisplaySlot, T_ScoreSortOrder


class LLSE_Objective:
    """Score Objective Object"""

    def __init__(self) -> NoReturn: ...

    @property
    def name(self) -> str:
        """Score objective name"""

    @property
    def displayName(self) -> str:
        """Display name of the score objective"""

    def setDisplay(
            self,
            slot: T_ScoreDisplaySlot,
            sort_order: T_ScoreSortOrder = 0,
    ) -> bool:
        """
        Set the display status of the score objective

        Args:
            slot: Display slot name string
            sort_order: Sorting order

        Returns:
            Whether the setting was successful
        """

    def setScore(self, target: LLSE_Player | str, score: int) -> int | None:
        """
        Set the score for a specific target

        Note: If the score objective does not exist, it will attempt to create it.
        In this case, it will return `0` (when `target` is a `str`) or `None` (when `target` is an `LLSE_Player`).

        See: [#971](https://github.com/LiteLDev/LiteLoaderBDS/issues/971#issuecomment-1385047649)

        Args:
            target: The target tracked by the score objective, can be a player object or any string
            score: The score to set

        Returns:
            If `None` is returned, the operation failed
        """

    def addScore(self, target: LLSE_Player | str, score: int) -> int | None:
        """
        Increase the score for a specific target

        Note: If the score objective does not exist, it will attempt to create it.
        In this case, it will return `0` (when `target` is a `str`) or `None` (when `target` is an `LLSE_Player`).

        See: [#971](https://github.com/LiteLDev/LiteLoaderBDS/issues/971#issuecomment-1385047649)

        Args:
            target: The target tracked by the score objective, can be a player object or any string
            score: The score to increase

        Returns:
            If `None` is returned, the operation failed
        """

    def reduceScore(self, target: LLSE_Player | str, score: int) -> int | None:
        """
        Decrease the score for a specific target

        Note: If the score objective does not exist, it will attempt to create it.
        In this case, it will return `0` (when `target` is a `str`) or `None` (when `target` is an `LLSE_Player`).

        See: [#971](https://github.com/LiteLDev/LiteLoaderBDS/issues/971#issuecomment-1385047649)

        Args:
            target: The target tracked by the score objective, can be a player object or any string
            score: The score to decrease

        Returns:
            If `None` is returned, the operation failed
        """

    def deleteScore(self, target: LLSE_Player | str) -> bool:
        """
        Stop tracking a specific target

        Stopping tracking will directly delete the score value corresponding to this target.
        Accessing it again will require recreating it.

        Args:
            target: The target tracked by the score objective, can be a player object or any string

        Returns:
            Whether stopping was successful
        """

    def getScore(self, target: LLSE_Player | str) -> int:
        """
        Get the score for a specific tracked target

        Make sure the score objective exists before using

        Args:
            target: The target to query, can be a player object or any string

        Returns:
            The score of the target/player in this score objective
        """


Objective = LLSE_Objective
