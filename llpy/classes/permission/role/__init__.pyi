from typing import overload

from llpy.types import T_ToJsonDict

from ..types import T_PermInfo

class Role:
    """Role group object"""

    @overload
    def __init__(self, name: str) -> None:
        """
        Create a role group

        Display name defaults to `name`

        Raises:
            Invalid parameter / Invalid name / The role group already exists

        Args:
            name: Role group name, must be unique. Cannot contain `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\n` `\t` `\r` `\f` `\v`
        """
    @overload
    def __init__(self, name: str, display_name: str) -> None:
        """
        Create a role group

        Raises:
            Invalid parameter / Invalid name / The role group already exists

        Args:
            name: Role group name, must be unique. Cannot contain `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\n` `\t` `\r` `\f` `\v`
            display_name: Role group display name
        """
    @property
    def name(self) -> str:
        """Role group name"""
    @name.setter
    def name(self, val: str): ...
    @property
    def displayName(self) -> str:
        """Role group display name"""
    @displayName.setter
    def displayName(self, val: str): ...
    @property
    def priority(self) -> int:
        """Role group priority, higher is more priority"""
    @priority.setter
    def priority(self, val: int): ...
    @property
    def members(self) -> list[str]:
        """XUIDs of members in the role group"""
    @members.setter
    def members(self, val: list[str]): ...
    @property
    def permissions(self) -> list[T_PermInfo]:
        """Permissions owned by the role group"""
    @permissions.setter
    def permissions(self, val: list[T_ToJsonDict]):
        """
        Set permissions owned by the role group

        The dictionaries in the list must have `name` (`str`) and `enabled` (`bool`) items,
        other items will be treated as `extra`
        """
    def hasMember(self, xuid: str) -> bool:
        """
        Check if the role group has a specified member

        Args:
            xuid: XUID of the member (player)

        Raises:
            Invalid parameter / Role group instance has been destroyed

        Returns:
            Whether the member is present
        """
    def addMember(self, xuid: str) -> None:
        """
        Add a member to the role group

        Args:
            xuid: XUID of the member (player)

        Raises:
            Invalid parameter / Role group instance has been destroyed / Member already exists
        """
    def removeMember(self, xuid: str) -> None:
        """
        Remove a member from the role group

        Args:
            xuid: XUID of the member (player)

        Raises:
            Invalid parameter / Role group instance has been destroyed / Member not found
        """
    def hasPermission(self, name: str) -> bool:
        """
        Check if the role group has a specified permission

        Note: Extra data of the permission will be ignored, this method returns `True` if the `enabled` field is `True`

        Args:
            name: Permission name

        Raises:
            Invalid parameter / Role group instance has been destroyed

        Returns:
            Whether the permission is present
        """
    @overload
    def setPermission(self, name: str, enabled: bool) -> None:
        """
        Set a permission for the role group

        If the specified permission is not found in the role group, it will be added with the specified value

        Args:
            name: Permission name, must be registered
            enabled: Whether the permission is enabled

        Raises:
            Invalid parameter / Invalid extra data / Invalid permission name / Role group instance has been destroyed
        """
    @overload
    def setPermission(
        self,
        name: str,
        enabled: bool,
        extra_data: T_ToJsonDict,
    ) -> None:
        """
        Set a permission for the role group

        If the specified permission is not found in the role group, it will be added with the specified value

        Args:
            name: Permission name, must be registered
            enabled: Whether the permission is enabled
            extra_data: Extra data for the permission

        Raises:
            Invalid parameter / Invalid extra data / Invalid permission name / Role group instance has been destroyed
        """
    def removePermission(self, name: str) -> None:
        """
        Remove a permission from the role group

        Args:
            name: Permission name

        Raises:
            Invalid parameter / Role group instance has been destroyed / Specified permission not found
        """
    def permissionExists(self, name: str) -> bool:
        """
        Check if a permission exists in the role group

        Unlike `hasPermission`, this method returns `True` as long as the permission exists in the role group, but the permission may not be enabled.

        Args:
            name: Permission name

        Raises:
            Invalid parameter / Role group instance has been destroyed

        Returns:
            Whether the permission already exists in the role group
        """
    def isValid(self) -> bool:
        """
        Check if the role group instance is valid

        Returns:
            Whether the role group instance is valid
        """
