from typing import Any, Literal, NoReturn, overload

from typing_extensions import deprecated

from llpy import (
    DirectionAngle,
    FloatPos,
    IntPos,
    LLSE_Block,
    LLSE_Container,
    LLSE_CustomForm,
    LLSE_Device,
    LLSE_Entity,
    LLSE_Item,
    LLSE_Packet,
    LLSE_SimpleForm,
    NativePointer,
    NbtCompound,
)
from llpy.types import T_DimID, T_EffectID, T_MoneyHistory, T_Number, T_PosType

from .types import (
    T_BossEventColor,
    T_CustomFormCallback,
    T_GameMode,
    T_ModalFormCallback,
    T_NavigatePath,
    T_PermLevel,
    T_PlayerInventory,
    T_SimpleFormCallback,
    T_TextPacketType,
    T_TitlePacketType,
)


class LLSE_Player:
    """Player object"""

    def __init__(self) -> NoReturn: ...

    @property
    def name(self) -> str:
        """Player name"""

    @property
    def pos(self) -> FloatPos:
        """Player's perspective height coordinates"""

    @property
    def feetPos(self) -> FloatPos:
        """Player's leg position coordinates (coordinates displayed in the game)"""

    @property
    def blockPos(self) -> IntPos:
        """Player's block coordinates"""

    @property
    def lastDeathPos(self) -> IntPos:
        """Coordinates of the player's last death"""

    @property
    def realName(self) -> str:
        """Player's real name"""

    @property
    def xuid(self) -> str:
        """Player's XUID string"""

    @property
    def uuid(self) -> str:
        """Player's UUID string"""

    @property
    def permLevel(self) -> T_PermLevel:
        """Player's operational permission level"""

    @property
    def gameMode(self) -> T_GameMode:
        """Player's game mode"""

    @property
    def canSleep(self) -> bool:
        """Whether the player can sleep"""

    @property
    def canFly(self) -> bool:
        """Whether the player can fly"""

    @property
    def canBeSeenOnMap(self) -> bool:
        """Whether the player can be seen on the map"""

    @property
    def canFreeze(self) -> bool:
        """Whether the player can be frozen"""

    @property
    def canSeeDaylight(self) -> bool:
        """Whether the player can see daylight"""

    @property
    def canShowNameTag(self) -> bool:
        """Whether the player can show a name tag"""

    @property
    def canStartSleepInBed(self) -> bool:
        """Whether the player can start sleeping in a bed"""

    @property
    def canPickupItems(self) -> bool:
        """Whether the player can pick up items"""

    @property
    def maxHealth(self) -> int:
        """Player's maximum health"""

    @property
    def health(self) -> int:
        """Player's current health"""

    @property
    def inAir(self) -> bool:
        """Whether the player is currently airborne"""

    @property
    def inWater(self) -> bool:
        """Whether the player is currently in water"""

    @property
    def inLava(self) -> bool:
        """Whether the player is in lava"""

    @property
    def inRain(self) -> bool:
        """Whether the player is in the rain"""

    @property
    def inSnow(self) -> bool:
        """Whether the player is in snow"""

    @property
    def inWall(self) -> bool:
        """Whether the player is on a wall"""

    @property
    def inWaterOrRain(self) -> bool:
        """Whether the player is in water or rain"""

    @property
    def inWorld(self) -> bool:
        """Whether the player is in the world"""

    @property
    def inClouds(self) -> bool:
        """Whether the player is above the clouds"""

    @property
    def speed(self) -> float:
        """Player's current speed"""

    @property
    def direction(self) -> DirectionAngle:
        """Player's current direction"""

    @property
    def uniqueId(self) -> str:
        """Unique identifier for the player (entity)"""

    @property
    def langCode(self) -> str:
        """Identifier for the language set by the player (e.g., `zh_CN`)"""

    @property
    def isLoading(self) -> bool:
        """Whether the player is currently loading"""

    @property
    def isInvisible(self) -> bool:
        """Whether the player is currently invisible"""

    @property
    def isInsidePortal(self) -> bool:
        """Whether the player is inside a portal"""

    @property
    def isHurt(self) -> bool:
        """Whether the player is hurt"""

    @property
    def isTrusting(self) -> bool:
        """Whether the player is trusted"""

    @property
    def isTouchingDamageBlock(self) -> bool:
        """Whether the player is on a block that can cause damage"""

    @property
    def isHungry(self) -> bool:
        """Whether the player is hungry"""

    @property
    def isOnFire(self) -> bool:
        """Whether the player is on fire"""

    @property
    def isOnGround(self) -> bool:
        """Whether the player is on the ground"""

    @property
    def isOnHotBlock(self) -> bool:
        """Whether the player is on a hot block (e.g., lava)"""

    @property
    def isTrading(self) -> bool:
        """Whether the player is trading"""

    @property
    def isAdventure(self) -> bool:
        """Whether the player is in adventure mode"""

    @property
    def isGliding(self) -> bool:
        """Whether the player is gliding"""

    @property
    def isSurvival(self) -> bool:
        """Whether the player is in survival mode"""

    @property
    def isSpectator(self) -> bool:
        """Whether the player is in spectator mode"""

    @property
    def isRiding(self) -> bool:
        """Whether the player is riding"""

    @property
    def isDancing(self) -> bool:
        """Whether the player is dancing"""

    @property
    def isCreative(self) -> bool:
        """Whether the player is in creative mode"""

    @property
    def isFlying(self) -> bool:
        """Whether the player is flying"""

    @property
    def isSleeping(self) -> bool:
        """Whether the player is currently sleeping"""

    @property
    def isMoving(self) -> bool:
        """Whether the player is currently moving"""

    @property
    def isSneaking(self) -> bool:
        """Whether the player is currently sneaking"""

    def isOP(self) -> bool:
        """
        Check if the player is an OP (operator)

        Returns:
            Whether the player is an OP
        """

    def setPermLevel(self, level: T_PermLevel) -> bool:
        """
        Modify the player's operational permission level

        Args:
            level: Target permission level

        Returns:
            Whether the modification was successful
        """

    def setGameMode(self, mode: T_GameMode) -> bool:
        """
        Modify the player's game mode

        Args:
            mode: Target game mode

        Returns:
            Whether the modification was successful
        """

    def runcmd(self, cmd: str) -> bool:
        """
        Execute a command as the player

        Args:
            cmd: The command to be executed

        Returns:
            Whether the execution was successful
        """

    @overload
    def teleport(self, pos: T_PosType) -> bool:
        """
        Teleport the player to a specified position

        Maintain the player's orientation before teleportation

        Args:
            pos: Target position coordinates

        Returns:
            Whether the teleportation was successful
        """

    @overload
    def teleport(self, pos: T_PosType, rot: DirectionAngle) -> bool:
        """
        Teleport the player to a specified position

        Args:
            pos: Target position coordinates
            rot: Orientation of the player after teleportation

        Returns:
            Whether the teleportation was successful
        """

    @overload
    def teleport(
            self,
            x: T_Number,
            y: T_Number,
            z: T_Number,
            dim_id: T_DimID,
    ) -> bool:
        """
        Teleport the player to a specified position

        Maintain the player's orientation before teleportation

        Args:
            x: Target position X coordinate
            y: Target position Y coordinate
            z: Target position Z coordinate
            dim_id: Target dimension ID

        Returns:
            Whether the teleportation was successful
        """

    @overload
    def teleport(
            self,
            x: T_Number,
            y: T_Number,
            z: T_Number,
            dim_id: T_DimID,
            rot: DirectionAngle,
    ) -> bool:
        """
        Teleport the player to a specified position

        Args:
            x: Target position X coordinate
            y: Target position Y coordinate
            z: Target position Z coordinate
            dim_id: Target dimension ID
            rot: Orientation of the player after teleportation

        Returns:
            Whether the teleportation was successful
        """

    def kill(self) -> bool:
        """
        Kill the player

        Returns:
            Whether the execution was successful
        """

    @overload
    def kick(self) -> bool:
        """
        Disconnect the player

        Returns:
            Whether the disconnection was successful
        """

    @overload
    def kick(self, msg: str) -> bool:
        """
        Disconnect the player

        Args:
            msg: Reason displayed to the kicked player

        Returns:
            Whether the disconnection was successful
        """

    @overload
    def disconnect(self) -> bool:
        """
        Disconnect the player

        Returns:
            Whether the disconnection was successful
        """

    @overload
    def disconnect(self, msg: str) -> bool:
        """
        Disconnect the player

        Args:
            msg: Reason displayed to the kicked player

        Returns:
            Whether the disconnection was successful
        """

    def tell(self, msg: str, msg_type: T_TextPacketType = 0) -> bool:
        """
        Send a text message to the player

        Args:
            msg: Text to be sent
            msg_type: Type of the text message being sent

        Returns:
            Whether the sending was successful
        """

    def sendText(self, msg: str, msg_type: T_TextPacketType = 0) -> bool:
        """
        Send a text message to the player

        Args:
            msg: Text to be sent
            msg_type: Type of the text message being sent

        Returns:
            Whether the sending was successful
        """

    @overload
    def talkAs(self, text: str) -> bool:
        """
        Speak as the player

        Args:
            text: Simulated speech content

        Returns:
            Whether the execution was successful
        """

    @overload
    def talkAs(self, target: LLSE_Player, text: str) -> bool:
        """
        Speak as the player to another player

        Args:
            target: Player to simulate speaking to
            text: Simulated speech content

        Returns:
            Whether the execution was successful
        """

    @overload
    def setTitle(self, content: str, title_type: T_TitlePacketType = 2) -> bool:
        """
        Set the player's display title

        Args:
            content: Desired title content
            title_type: Type of the title being set

        Returns:
            Whether the sending was successful
        """

    @overload
    def setTitle(
            self,
            content: str,
            title_type: T_TitlePacketType,
            fade_in_time: int,
            stay_time_int: int,
            fade_out_time: int,
    ) -> bool:
        """
        Set the player's display title

        Args:
            content: Desired title content
            title_type: Type of the title being set
            fade_in_time: Fade-in time, in ticks
            stay_time_int: Stay time, in ticks
            fade_out_time: Fade-out time, in ticks

        Returns:
            Whether the sending was successful
        """

    def rename(self, new_name: str) -> bool:
        """
        Rename the player

        Args:
            new_name: Player's new name

        Returns:
            Whether the renaming was successful
        """

    def setFire(self, time: int, is_effect: bool) -> bool:
        """
        Set the specified player on fire

        Args:
            time: Duration of being on fire, in seconds
            is_effect: Whether there will be a fire effect

        Returns:
            Whether setting on fire was successful
        """

    def stopFire(self) -> bool:
        """
        Extinguish the player

        Returns:
            Whether the player has been extinguished
        """

    def transServer(self, server: str, port: int) -> bool:
        """
        Teleport the player to a specified server

        Args:
            server: Target server IP/domain
            port: Target server port

        Returns:
            Whether the teleportation was successful
        """

    def crash(self) -> bool:
        """
        Cause the player's client to crash

        Returns:
            Whether the execution was successful
        """

    def hurt(self, damage: int) -> bool:
        """
        Inflict damage on the player

        The damage inflicted here is true damage and cannot be reduced by protective equipment such as armor

        Args:
            damage: Numeric value of damage inflicted on the player

        Returns:
            Whether the damage was inflicted
        """

    def heal(self, health: int) -> bool:
        """
        Heal the player

        Args:
            health: Number of hearts to heal

        Returns:
            Whether the healing was successful
        """

    def setHealth(self, health: int) -> bool:
        """
        Set the player's health

        Args:
            health: Health value

        Returns:
            Whether the setting was successful
        """

    def setMaxHealth(self, health: int) -> bool:
        """
        Set the player's maximum health

        Args:
            health: Health value

        Returns:
            Whether the setting was successful
        """

    def setAbsorption(self, value: int) -> bool:
        """
        Set the damage absorption attribute for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setAttackDamage(self, value: int) -> bool:
        """
        Set the attack damage attribute for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setMaxAttackDamage(self, value: int) -> bool:
        """
        Set the maximum attack damage attribute for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setFollowRange(self, value: int) -> bool:
        """
        Set the follow range for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setKnockbackResistance(self, value: int) -> bool:
        """
        Set the knockback resistance attribute for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setLuck(self, value: int) -> bool:
        """
        Set the luck attribute for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setMovementSpeed(self, value: int) -> bool:
        """
        Set the movement speed attribute for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setUnderwaterMovementSpeed(self, value: int) -> bool:
        """
        Set the underwater movement speed attribute for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setLavaMovementSpeed(self, value: int) -> bool:
        """
        Set the lava movement speed attribute for the player

        Args:
            value: New value

        Returns:
            Whether setting the attribute value for the player was successful
        """

    def setHungry(self, hunger: int) -> bool:
        """
        Set the player's hunger level

        Args:
            hunger: Hunger value

        Returns:
            Whether the setting was successful
        """

    def refreshChunks(self) -> bool:
        """
        Refresh all chunks loaded by the player

        Returns:
            Whether the refresh was successful
        """

    @overload
    def giveItem(self, item: LLSE_Item) -> bool:
        """
        Give the player an item

        If the player's inventory is full, excess items will be thrown away

        Args:
            item: Item object to be given

        Returns:
            Whether the giving was successful
        """

    @overload
    def giveItem(self, item: LLSE_Item, amount: int) -> bool:
        """
        Give the player an item

        If the player's inventory is full, excess items will be thrown away

        Args:
            item: Item object to be given
            amount: Quantity of the item to be given, the `Count` attribute of the item object itself will be ignored

        Returns:
            Whether the giving was successful
        """

    def clearItem(self, item_type: str, count: int = 1) -> int:
        """
        Clear items of a specified type from the player's inventory

        Compares the `type` attribute of all items in the player's inventory, main hand, off hand, and armor slots with this string,
        and clears the item if they are equal.

        Args:
            item_type: Type name of the item to be cleared
            count: Quantity to be cleared

        Returns:
            Number of cleared items
        """

    def isSprinting(self) -> bool:
        """
        Get the player's sprinting state

        Returns:
            Player's sprinting state
        """

    def setSprinting(self, sprinting: bool) -> bool:
        """
        Set the player's sprinting state

        Args:
            sprinting: Whether the player is in a sprinting state

        Returns:
            Whether the setting was successful
        """

    def sendToast(self, title: str, message: str) -> bool:
        """
        Display a message at the top of the screen

        Similar to achievement completion

        Args:
            title: Title to be sent
            message: Text to be sent

        Returns:
            Whether the message was successfully sent
        """

    def distanceTo(self, pos: LLSE_Entity | LLSE_Player | T_PosType) -> T_Number:
        """
        Get the distance from the player to a coordinate

        If the player's coordinates and the target's coordinates are not in the same dimension, the maximum integer value will be returned

        Args:
            pos: Target position

        Returns:
            Distance to the coordinate (blocks)
        """

    def distanceToSqr(
            self,
            pos: LLSE_Entity | LLSE_Player | T_PosType,
    ) -> T_Number:
        """
        Get the squared distance from the player to a coordinate

        If the player's coordinates and the target's coordinates are not in the same dimension, the maximum integer value will be returned

        Args:
            pos: Target position

        Returns:
            Squared distance to the coordinate (blocks)
        """

    def getBlockStandingOn(self) -> LLSE_Block:
        """
        Get the block on which the player is currently standing

        Returns:
            Block object on which the player is currently standing
        """

    def getDevice(self) -> LLSE_Device:
        """
        Get the device information object corresponding to the player

        Returns:
            Device information object corresponding to the player
        """

    def getHand(self) -> LLSE_Item:
        """
        Get the item object in the player's main hand

        The item object obtained here is a reference.
        In other words, modifying the item object returned here or using its API is equivalent to directly manipulating the item in the player's main hand

        Returns:
            Item object in the player's main hand
        """

    def getOffHand(self) -> LLSE_Item:
        """
        Get the item object in the player's off hand

        The item object obtained here is a reference.
        In other words, modifying the item object returned here or using its API is equivalent to directly manipulating the item in the player's off hand

        Returns:
            Item object in the player's off hand
        """

    def getPlayerInventoryContainer(self) -> LLSE_Container:
        """
        Get the container object corresponding to the player's inventory

        Returns:
            Container object corresponding to the player's inventory
        """

    def getArmor(self) -> LLSE_Container:
        """
        Get the container object corresponding to the player's armor slots

        Returns:
            Container object corresponding to the player's armor slots
        """

    def getEnderChest(self) -> LLSE_Container:
        """
        Get the container object corresponding to the player's ender chest

        Returns:
            Container object corresponding to the player's ender chest
        """

    def getRespawnPosition(self) -> IntPos:
        """
        Get the player's respawn coordinates

        Returns:
            Respawn point coordinates
        """

    @overload
    def setRespawnPosition(self, pos: IntPos) -> bool:
        """
        Modify the player's respawn coordinates

        Args:
            pos: Respawn coordinates

        Returns:
            Whether the modification was successful
        """

    @overload
    def setRespawnPosition(self, x: int, y: int, z: int, dim_id: T_DimID) -> bool:
        """
        Modify the player's respawn coordinates

        Args:
            x: Respawn X coordinate
            y: Respawn Y coordinate
            z: Respawn Z coordinate
            dim_id: Respawn dimension ID

        Returns:
            Whether the modification was successful
        """

    def refreshItems(self) -> bool:
        """
        Refresh the player's inventory and armor slots

        After modifying the player's items, to make it take effect on the client, all of the player's items need to be refreshed

        Returns:
            Whether the refresh was successful
        """

    def getScore(self, name: str) -> int:
        """
        Get the score of the online player for a scoreboard item

        Before using, make sure that the corresponding scoreboard item exists

        Args:
            name: Scoreboard item name

        Returns:
            Numeric value on the scoreboard
        """

    def setScore(self, name: str, value: int) -> bool:
        """
        Set the score of the online player for a scoreboard item

        If the scoreboard item does not exist, it will return `False` and create the scoreboard item

        Args:
            name: Scoreboard item name
            value: Value to be set

        Returns:
            Numeric value on the scoreboard
        """

    def addScore(self, name: str, value: int) -> bool:
        """
        Increase the score of the online player for a scoreboard item

        If the scoreboard item does not exist, it will return `False` and create the scoreboard item

        Args:
            name: Scoreboard item name
            value: Value to be added

        Returns:
            Numeric value on the scoreboard
        """

    def reduceScore(self, name: str, value: int) -> bool:
        """
        Decrease the score of the online player for a scoreboard item

        If the scoreboard item does not exist, it will return `False` and create the scoreboard item

        Args:
            name: Scoreboard item name
            value: Value to be reduced

        Returns:
            Numeric value on the scoreboard
        """

    def deleteScore(self, name: str) -> bool:
        """
        Stop tracking the scoreboard item for the player

        Before using, make sure that the corresponding scoreboard item exists

        Args:
            name: Scoreboard item name

        Returns:
            Whether the removal was successful
        """

    def setSidebar(
            self,
            title: str,
            data: dict[str, int],
            sort_order: Literal[0, 1] = 1,
    ) -> bool:
        """
        Set a custom sidebar for the player

        Args:
            title: Sidebar title
            data: Content object of the sidebar object. Each key-value pair in the object will be set as a line of the sidebar content
            sort_order: Sorting order of the sidebar content. `0` for ascending order by score, `1` for descending order by score

        Returns:
            _description_
        """

    def removeSidebar(self) -> bool:
        """
        Remove the custom sidebar for the player

        Returns:
            Whether the removal was successful
        """

    @overload
    def setBossBar(
            self,
            title: str,
            percent: int,
            color: T_BossEventColor = 2,
    ) -> bool:
        """
        Set a custom Boss bar visible to the player

        Args:
            title: Custom bar title
            percent: Percentage of health in the bar, valid range is 0 ~ 100
            color: Bar color

        Returns:
            Whether the setting was successful
        """

    @overload
    def setBossBar(
            self,
            uid: int,
            title: str,
            percent: int,
            color: T_BossEventColor = 2,
    ) -> bool:
        """
        Set a custom Boss bar visible to the player

        Args:
            uid: Unique identifier, must not conflict! One uid corresponds to one line of BossBar
            title: Custom bar title
            percent: Percentage of health in the bar, valid range is 0 ~ 100
            color: Bar color

        Returns:
            Whether the setting was successful
        """

    @overload
    def removeBossBar(self) -> bool:
        """
        Remove the player's custom specified Boss bar

        Returns:
            Whether the removal was successful
        """

    @overload
    def removeBossBar(self, uid: int) -> bool:
        """
        Remove the player's custom specified Boss bar

        Args:
            uid: Identifier corresponding to `setBossBar`

        Returns:
            Whether the removal was successful
        """

    def addLevel(self, count: int) -> bool:
        """
        Increase the player's experience level

        Args:
            count: Experience level to increase

        Returns:
            Whether the setting was successful
        """

    def reduceLevel(self, count: int) -> bool:
        """
        Decrease the player's experience level

        Args:
            count: Experience level to decrease

        Returns:
            Whether the setting was successful
        """

    def getLevel(self) -> int:
        """
        Get the player's experience level

        Returns:
            Player's experience level
        """

    def setLevel(self, count: int) -> bool:
        """
        Set the player's experience level

        Args:
            count: Experience level to set

        Returns:
            Whether the setting was successful
        """

    def resetLevel(self) -> bool:
        """
        Reset the player's experience

        Returns:
            Whether the setting was successful
        """

    def addExperience(self, count: int) -> bool:
        """
        Increase the player's experience points

        Args:
            count: Experience points to increase

        Returns:
            Whether the setting was successful
        """

    def reduceExperience(self, count: int) -> bool:
        """
        Decrease the player's experience points

        Args:
            count: Experience points to decrease

        Returns:
            Whether the setting was successful
        """

    def getCurrentExperience(self) -> int:
        """
        Get the player's current experience points

        Returns:
            Player's total experience points
        """

    def setCurrentExperience(self, count: int) -> bool:
        """
        Set the player's current experience points

        Args:
            count: Experience points to set

        Returns:
            Whether the setting was successful
        """

    def getTotalExperience(self) -> int:
        """
        Get the player's total experience points

        Returns:
            Player's total experience points
        """

    def setTotalExperience(self, count: int) -> bool:
        """
        Set the player's total experience points

        Args:
            count: Experience points to set

        Returns:
            Whether the setting was successful
        """

    def getXpNeededForNextLevel(self) -> int:
        """
        Get the experience points needed for the player to level up

        Note that this method ignores the current experience points

        Returns:
            Experience points needed for the player to level up
        """

    def setScale(self, scale: int) -> bool:
        """
        Resize the player

        Args:
            scale: New player volume

        Returns:
            Whether the player was successfully resized
        """

    def setAbility(self, ability_id: int, value: bool) -> bool:
        """
        Set the player's Ability attribute

        Args:
            ability_id: ID of the Ability
            value: Whether to enable

        Returns:
            No effect
        """

    def getBiomeId(self) -> int:
        """
        Get the biome ID where the player is located

        Returns:
            Biome ID
        """

    def getBiomeName(self) -> str:
        """
        Get the name of the biome where the player is located

        Returns:
            Biome name
        """

    def getAllEffects(self) -> list[T_EffectID] | None:
        """
        Get the status effects on the player

        Returns:
            List of status effect IDs. Returns `None` if the player has no status effects
        """

    def addEffect(self, effect_id: T_EffectID, tick: int, level: int) -> bool:
        """
        Add a status effect to the player

        Args:
            effect_id: Numeric ID of the status effect
            tick: Duration in `Ticks`
            level: Effect level

        Returns:
            Whether the effect was successfully added
        """

    def removeEffect(self, effect_id: T_EffectID) -> bool:
        """
        Remove a status effect from the player

        Args:
            effect_id: Numeric ID of the status effect

        Returns:
            Whether the effect was successfully removed
        """

    def sendModalForm(
            self,
            title: str,
            content: str,
            confirm_button: str,
            cancel_button: str,
            callback: T_ModalFormCallback,
    ) -> int | None:
        """
        Send a modal form to the player

        The modal form contains a title, a text display box, and two buttons

        Callback Args:
            player (LLSE_Player): Player object interacting with the form
            result (bool | None): `True` if the player clicks the confirm button, `False` for the cancel button. If `None`, it means the player canceled the form

        Args:
            title: Form title
            content: Form content
            confirm_button: String for button 1 (confirm)
            cancel_button: String for button 2 (cancel)
            callback: Callback function called after the player clicks a button

        Returns:
            ID of the sent form. Returns `None` if sending fails
        """

    def sendSimpleForm(
            self,
            title: str,
            content: str,
            buttons: list[str],
            images: list[str],
            callback: T_SimpleFormCallback,
    ) -> int | None:
        """
        Send a simple form to the player

        Callback Args:
            player (LLSE_Player): Player object interacting with the form
            button_id (int | None): Index of the form button that the player clicked, numbered from `0`. If `None`, it means the player canceled the form

        Args:
            title: Form title
            content: Form content
            buttons: Array of strings for each button
            images: Array of image paths corresponding to each button. Leave as an empty string if no image is needed
                Element format: `textures/items/apple` (texture pack path) or `https://1919810.work/apple.png` (full URL)
            callback: Callback function called after the player clicks a button

        Returns:
            ID of the sent form. Returns `None` if sending fails
        """

    def sendCustomForm(self, json: str, callback: T_CustomFormCallback) -> int | None:
        """
        Send a custom form to the player (in JSON format)

        Callback Args:
            player (LLSE_Player): Player object interacting with the form
            data (list[bool | int | str | None] | None): Array of returned form content.
                The first item in the array must be `None`. Starting from the second item, it stores the content of each control in the order of the form.
                If `data` is only `None`, it means the player canceled the form

        Args:
            json: JSON string of the custom form
            callback: Callback function called after the player submits the form

        Returns:
            ID of the sent form. Returns `None` if sending fails
        """

    @overload
    def sendForm(
            self,
            form: LLSE_SimpleForm,
            callback: T_SimpleFormCallback,
    ) -> int | None:
        """
        Send a simple form to the player

        Callback Args:
            player (LLSE_Player): Player object interacting with the form
            button_id (int | None): Index of the form button that the player clicked, numbered from `0`. If `None`, it means the player canceled the form

        Args:
            form: Configured form object
            callback: Callback function called after the player interacts with the form elements

        Returns:
            ID of the sent form. Returns `None` if sending fails
        """

    @overload
    def sendForm(
            self,
            form: LLSE_CustomForm,
            callback: T_CustomFormCallback,
    ) -> int | None:
        """
        Send a custom form to the player

        Callback Args:
            player (LLSE_Player): Player object interacting with the form
            data (list[bool | int | str | None] | None): Array of returned form content.
                The array stores the content of each control in the order of the form.
                If `data` is only `None`, it means the player canceled the form

        Args:
            form: Configured form object
            callback: Callback function called after the player interacts with the form elements

        Returns:
            ID of the sent form. Returns `None` if sending fails
        """

    def sendPacket(self, packet: LLSE_Packet) -> bool:
        """
        Send a packet to the player

        Args:
            packet: Packet object

        Returns:
            Whether the sending was successful
        """

    def setExtraData(self, name: str, data: Any) -> bool:
        """
        Store player-bound data

        Args:
            name: Name to store the data in
            data: Data to store

        Returns:
            Whether the storing was successful
        """

    def getExtraData(self, name: str) -> Any | None:
        """
        Get player-bound data

        Args:
            name: Name of the data to read

        Returns:
            Stored bound data. Returns `None` if the specified bound data is not found or the data is empty
        """

    def delExtraData(self, name: str) -> bool:
        """
        Delete player-bound data

        Args:
            name: Name of the data to delete

        Returns:
            Whether the deletion was successful
        """

    def setNbt(self, nbt: NbtCompound) -> bool:
        """
        Write to the NBT object corresponding to the online player

        Args:
            nbt: NBT object

        Returns:
            Whether writing was successful
        """

    def getNbt(self) -> NbtCompound:
        """
        Get the NBT object corresponding to the online player

        Returns:
            Player's NBT object
        """

    def addTag(self, tag: str) -> bool:
        """
        Add a tag to the player

        Args:
            tag: Tag string to add

        Returns:
            Whether the setting was successful
        """

    def removeTag(self, tag: str) -> bool:
        """
        Remove a tag from the player

        Args:
            tag: Tag string to remove

        Returns:
            Whether the removal was successful
        """

    def hasTag(self, tag: str) -> bool:
        """
        Check if the player has a specific tag

        Args:
            tag: Tag string to check

        Returns:
            Whether the player has the specified tag
        """

    def getAllTags(self) -> list[str]:
        """
        Get a list of all tags the player has

        Returns:
            List of all tag strings the player has
        """

    def getAbilities(self) -> dict[str, Any]:
        """
        Get the player's Abilities ability list (from player NBT)

        Returns:
            Key-value pairs of all ability information for the player
        """

    def getAttributes(self) -> list[dict[str, Any]]:
        """
        Get the player's Attributes attribute list (from player NBT)

        Returns:
            Array of all attribute objects for the player
        """

    def getEntityFromViewVector(self, max_distance: float = 5.25) -> LLSE_Entity | None:
        """
        Get the entity in the line of sight

        Args:
            max_distance: Maximum search distance

        Returns:
            Entity in the line of sight. Returns `None` if unsuccessful
        """

    def getBlockFromViewVector(
            self,
            include_liquid: bool = False,
            solid_only: bool = False,
            max_distance: float = 5.25,
            full_only: bool = False,
    ) -> LLSE_Block | None:
        """
        Get the block in the line of sight

        Args:
            include_liquid: Whether to include liquid blocks
            solid_only: Whether to only allow `Solid` type blocks
            max_distance: Maximum search distance
            full_only: Whether to only allow full blocks

        Returns:
            Block in the line of sight. Returns `None` if unsuccessful
        """

    def quickEvalMolangScript(self, exp: str) -> float:
        """
        Quickly execute Molang expressions

        For detailed usage of Molang, please refer to [MOLANG documentation on bedrock.dev](https://bedrock.dev/zh/docs/stable/Molang)

        Args:
            exp: Molang expression

        Returns:
            Result of the expression execution
        """

    def getMoney(self) -> int:
        """
        Get the player's deposit amount

        Returns:
            Player's monetary amount
        """

    def setMoney(self, value: int) -> bool:
        """
        Set the player's deposit amount

        Args:
            value: Amount to set

        Returns:
            Whether the setting was successful
        """

    def addMoney(self, value: int) -> bool:
        """
        Increase the player's deposit

        Args:
            value: Amount to increase

        Returns:
            Whether the setting was successful
        """

    def reduceMoney(self, value: int) -> bool:
        """
        Decrease the player's deposit

        Args:
            value: Amount to decrease

        Returns:
            Whether the setting was successful
        """

    @overload
    def transMoney(self, target: LLSE_Player | str, money: int) -> bool: ...

    @overload
    def transMoney(self, target: LLSE_Player | str, money: int, note: str) -> bool:
        """
        Perform a money transfer

        Args:
            target: Player object or XUID identifier of the payee
            money: Amount to pay
            note: Additional text explanation for this transfer

        Returns:
            Whether the transfer was successful
        """

    def getMoneyHistory(self, time: int) -> list[T_MoneyHistory]:
        """
        Query transaction history

        Args:
            time: Records from now backward for `time` seconds

        Returns:
            Array of query result objects
        """

    def isSimulatedPlayer(self) -> bool:
        """
        Check if it is a simulated player

        Returns:
            Whether it is a simulated player
        """

    def simulateSneak(self) -> bool:
        """
        Simulate sneaking

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateAttack(self) -> bool:
        """
        Simulate an attack

        Default attack on the entity in the line of sight

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateAttack(self, target: LLSE_Entity) -> bool:
        """
        Simulate an attack

        Args:
            target: Attack target

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateDestroy(self, pos: IntPos) -> bool:
        """
        Simulate destruction

        Default destroy the block in the line of sight

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateDestroy(self, pos: IntPos, face: int = 0) -> bool:
        """
        Simulate destruction

        Args:
            pos: Coordinates of the block to destroy
            face: From which side to destroy

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateDestroy(self, block: LLSE_Block, face: int = 0) -> bool:
        """
        Simulate destruction

        Args:
            block: Block to destroy
            face: From which side to destroy

        Returns:
            Whether the simulation was successful
        """

    def simulateDisconnect(self) -> bool:
        """
        Simulate disconnection

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateInteract(self) -> bool:
        """
        Simulate interaction

        Default interact with the block or entity in the line of sight

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateInteract(self, target: LLSE_Entity) -> bool:
        """
        Simulate interaction

        Args:
            block: Simulated interaction target

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateInteract(self, pos: IntPos, face: int = 0) -> bool:
        """
        Simulate interaction

        Args:
            block: Coordinates of the simulated interaction target
            face: Face of the simulated interaction target coordinates

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateInteract(self, block: LLSE_Block, face: int = 0) -> bool:
        """
        Simulate interaction

        Args:
            block: Simulated interaction target block
            face: Face of the simulated interaction target block

        Returns:
            Whether the simulation was successful
        """

    def simulateRespawn(self) -> bool:
        """
        Simulate respawn

        Returns:
            Whether the simulation was successful
        """

    def simulateJump(self) -> bool:
        """
        Simulate jumping

        Returns:
            Whether the simulation was successful
        """

    def simulateLocalMove(self, pos: T_PosType, speed: T_Number = 1) -> bool:
        """
        Move in the player's coordinate system

        Args:
            pos: Movement direction
            speed: Movement speed

        Returns:
            Whether the movement request was successful
        """

    def simulateWorldMove(self, pos: T_PosType, speed: T_Number = 1) -> bool:
        """
        Move in the world coordinate system

        Args:
            pos: Movement direction
            speed: Movement speed

        Returns:
            Whether the movement request was successful
        """

    def simulateMoveTo(self, pos: T_PosType, speed: T_Number = 1) -> bool:
        """
        Move in a straight line to coordinates

        If automatic pathfinding is required, consider using `simulateNavigateTo()`.

        Args:
            pos: Movement direction
            speed: Movement speed

        Returns:
            Whether the movement request was successful
        """

    def simulateLookAt(self, target: T_PosType | LLSE_Entity | LLSE_Block) -> bool:
        """
        Simulate looking at a block or entity

        Args:
            target: Coordinates / entity / block to look at

        Returns:
            Whether the simulation was successful
        """

    def simulateSetBodyRotation(self, rot: T_Number) -> bool:
        """
        Simulate setting body rotation

        Args:
            rot: Angle to set

        Returns:
            Whether the simulation was successful
        """

    def simulateNavigateTo(
            self,
            target: T_PosType | LLSE_Entity,
            speed: T_Number = 1,
    ) -> T_NavigatePath:
        """
        Simulate navigation movement

        Args:
            target: Navigation target
            speed: Movement speed

        Returns:
            Whether it is possible to reach the specified position and navigation path
        """

    @overload
    def simulateUseItem(self) -> bool:
        """
        Simulate using an item

        The used item defaults to the selected item.
        Target coordinates default to the coordinates of the facing block.
        Target block face defaults to `0`.
        Offset coordinates default to `(0.5, 0.5, 0.5)`.

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateUseItem(self, item: int | LLSE_Item) -> bool:
        """
        Simulate using an item

        Target coordinates default to the coordinates of the facing block.
        Target block face defaults to `0`.
        Offset coordinates default to `(0.5, 0.5, 0.5)`.

        Args:
            item: Item to use / slot ID where the item is located

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateUseItem(self, item: int | LLSE_Item, pos: IntPos) -> bool:
        """
        Simulate using an item

        Target block face defaults to `0`.
        Offset coordinates default to `(0.5, 0.5, 0.5)`.

        Args:
            item: Item to use / slot ID where the item is located
            pos: Target coordinates

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateUseItem(
            self,
            item: int | LLSE_Item,
            pos: IntPos,
            face: int,
    ) -> bool:
        """
        Simulate using an item

        Offset coordinates default to `(0.5, 0.5, 0.5)`.

        Args:
            item: Item to use / slot ID where the item is located
            pos: Target coordinates
            face: Face of the target block

        Returns:
            Whether the simulation was successful
        """

    @overload
    def simulateUseItem(
            self,
            item: int | LLSE_Item,
            pos: IntPos,
            face: int,
            relative: FloatPos,
    ) -> bool:
        """
        Simulate using an item

        Args:
            item: Item to use / slot ID where the item is located
            pos: Target coordinates
            face: Face of the target block
            relative: Relative block offset coordinates

        Returns:
            Whether the simulation was successful
        """

    def simulateStopDestroyingBlock(self) -> bool:
        """
        Simulate stopping block destruction

        Returns:
            Whether the simulation was successful
        """

    def simulateStopInteracting(self) -> bool:
        """
        Simulate stopping interaction

        Returns:
            Whether the simulation was successful
        """

    def simulateStopMoving(self) -> bool:
        """
        Simulate stopping movement

        Returns:
            Whether the simulation was successful
        """

    def simulateStopUsingItem(self) -> bool:
        """
        Simulate stopping item usage

        Returns:
            Whether the simulation was successful
        """

    def simulateStopSneaking(self) -> bool:
        """
        Simulate stopping sneaking

        Returns:
            Whether the simulation was successful
        """

    def asPointer(self) -> NativePointer:
        ...

    @deprecated("Please use `LLSE_Player.isSneaking`")
    @property
    def sneaking(self) -> bool:
        ...

    @deprecated("Please use `LLSE_Player.getDevice()`")
    @property
    def ip(self) -> str:
        ...

    @deprecated("Please use `LLSE_Player.setNbt()`")
    def setTag(self, nbt: NbtCompound) -> bool:
        ...

    @deprecated("Please use `LLSE_Player.getNbt()`")
    def getTag(self) -> NbtCompound:
        ...

    @deprecated("Please use `LLSE_Player.setFire()`")
    def setOnFire(self, time: int) -> bool:
        ...

    @deprecated("Please use `LLSE_Player.getInventory()`")
    def removeItem(self, inventory_id: int, count: int) -> bool:
        ...

    @deprecated("Please use `LLSE_Player.getInventory()`")
    def getAllItems(self) -> T_PlayerInventory:
        ...

    @deprecated("Please use `LLSE_Player.deleteScore()`")
    def removeScore(self, name: str) -> bool:
        ...

    @deprecated("Please use `LLSE_Player.distanceTo()`")
    def distanceToPos(self, pos: LLSE_Entity | LLSE_Player | T_PosType) -> T_Number:
        ...

    Player = LLSE_Player
