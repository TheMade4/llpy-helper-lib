from typing import NoReturn, overload

from .role import Role
from .types import T_PermInfo


class Permission:
    """Permission system API"""

    def __init__(self) -> NoReturn: ...

    @overload
    @staticmethod
    def createRole(name: str) -> Role:
        """
        Create a role group

        Display name defaults to `name`

        Args:
            name: Role group name, must be unique. Cannot contain `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\n` `\t` `\r` `\f` `\v`
            display_name: Role group display name

        Raises:
            Invalid parameter / Invalid name / The role group already exists

        Returns:
            Role group instance
        """

    @overload
    @staticmethod
    def createRole(name: str, display_name: str) -> Role:
        """
        Create a role group

        Args:
            name: Role group name, must be unique. Cannot contain `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\n` `\t` `\r` `\f` `\v`
            display_name: Role group display name

        Raises:
            Invalid parameter / Invalid name / The role group already exists

        Returns:
            Role group instance
        """

    @staticmethod
    def roleExists(name: str) -> bool:
        """
        Check if a role group exists

        Args:
            name: Role group name

        Raises:
            Invalid parameter

        Returns:
            Whether the role group exists
        """

    @staticmethod
    def getRole(name: str) -> Role:
        """
        Get an existing role group

        Args:
            name: Role group name

        Raises:
            Invalid parameter / Role group not found

        Returns:
            Role group instance
        """

    @staticmethod
    def getOrCreateRole(name: str) -> Role:
        """
        Create or get a role group instance

        Args:
            name: Role group name, must be unique. Cannot contain `@` `#` `[` `]` `{` `}` `<` `>` `(` `)` `/` `|` `$` `%` `^` `&` `*` `!` `~` `"` `'` `+` `=` `?` `\n` `\t` `\r` `\f` `\v`

        Raises:
            Invalid parameter / Invalid name

        Returns:
            Role group instance
        """

    @staticmethod
    def deleteRole(name: str) -> None:
        """
        Delete a role group

        Args:
            name: Role group name

        Raises:
            Invalid parameter / Role group does not exist
        """

    @staticmethod
    def registerPermission(name: str, desc: str) -> None:
        """
        Register a permission

        Args:
            name: Permission name, unique and does not contain `space` `\n` `\t` `\r` `\f` `\v`
            desc: Permission description

        Raises:
            Invalid parameter / Invalid permission name / Permission already exists
        """

    @staticmethod
    def deletePermission(name: str) -> None:
        """
        Delete a permission

        Args:
            name: Permission name

        Raises:
            Invalid parameter / Permission does not exist
        """

    @staticmethod
    def permissionExists(name: str) -> bool:
        """
        Check if a permission exists

        Args:
            name: Permission name

        Raises:
            Invalid parameter

        Returns:
            Whether the permission exists
        """

    @staticmethod
    def checkPermission(xuid: str, perm_name: str) -> bool:
        """
        Check if a player has a specified permission

        Note: Extra data of the permission will be ignored, this method returns `True` if the `enabled` field is `True`

        Args:
            xuid: Player XUID
            perm_name: Permission name

        Raises:
            Invalid parameter / Player not found / Permission not found

        Returns:
            Whether the player has the specified permission
        """

    @staticmethod
    def isMemberOf(xuid: str, role_name: str) -> bool:
        """
        Check if a player is a member of a specified role group

        Note: If the specified role group is not found, this method will return `False`.

        Args:
            xuid: Player XUID
            role_name: Role group name

        Raises:
            Invalid parameter / Player not found

        Returns:
            Whether the player is a member of the specified role group
        """

    @staticmethod
    def getPlayerRoles(xuid: str) -> list[Role]:
        """
        Get a list of role groups for a player

        Args:
            xuid: Player XUID

        Returns:
            List of role groups for this player
        """

    @staticmethod
    def getPlayerPermissions(xuid: str) -> list[T_PermInfo]:
        """
        Get a list of permissions for a player

        Args:
            xuid: Player XUID

        Returns:
            List of permissions for this player
        """

    @staticmethod
    def saveData() -> None:
        """
        Save data

        Data will be automatically saved every 100 game ticks
        """
