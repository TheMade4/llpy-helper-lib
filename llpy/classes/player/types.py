from typing import Any, Callable, Literal, TypedDict
from typing_extensions import deprecated
from llpy import LLSE_Item
from . import LLSE_Player

@deprecated("Please use `LLSE_Player.getInventory()`")
class T_PlayerInventory(TypedDict):
    """Inventory information returned by `LLSE_Player.getAllItems()`"""

    hand: LLSE_Item
    offHand: LLSE_Item
    inventory: list[LLSE_Item]
    armor: list[LLSE_Item]
    endChest: list[LLSE_Item]

T_PermLevel = Literal[0, 1, 2, 3, 4]
"""
Permission level

- 0. Regular member
- 1. OP
- 4. Console
"""

T_GameMode = Literal[0, 1, 2, 6]
"""
Game mode

- 0. Survival
- 1. Creative
- 2. Adventure
- 6. Spectator
"""

T_TextPacketType = Literal[0, 1, 4, 5, 9]
"""
Text message types sent by `LLSE_Player.tell()`

- 0. Normal message (`Raw`)
- 1. Chat message (`Chat`)
- 4. Jukebox message (`Popup`)
- 5. Message above the inventory (`Tip`)
- 9. JSON-formatted message (`JSON`)
"""

T_TitlePacketType = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
"""
Title types sent by `LLSE_Player.setTitle()`

- 0. Clear (`Clear`)
- 1. Reset (`Reset`)
- 2. Main title (`SetTitle`)
- 3. Subtitle (`SetSubTitle`)
- 4. ActionBar (`SetActionBar`)
- 5. Set display time (`SetDurations`)
- 6. JSON-formatted main title (`TitleTextObject`)
- 7. JSON-formatted subtitle (`SubtitleTextObject`)
- 8. JSON-formatted ActionBar (`ActionbarTextObject`)
"""

T_BossEventColor = Literal[0, 1, 2, 3, 4, 5, 6]
"""
Boss bar colors set by `LLSE_Player.setBossBar()`

- 0. Gray (`Gray`)
- 1. Blue (`Blue`)
- 2. Red (`Red`)
- 3. Green (`Green`)
- 4. Yellow (`Yellow`)
- 5. Purple (`Purple`)
- 6. White (`White`)
"""

T_AbilityID = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
"""
Ability IDs set by `LLSE_Player.setAbility()`

- 0. Build (`Build`)
- 1. Mine (`Mine`)
- 2. Doors and Switches (`DoorsAndSwitches`)
- 3. Open Containers (`OpenContainers`)
- 4. Attack Players (`AttackPlayers`)
- 5. Attack Mobs (`AttackMobs`)
- 6. Operator Commands (`OperatorCommands`)
- 7. Teleport (`Teleport`)
- 8. Invulnerable (`Invulnerable`)
- 9. Flying (`Flying`)
- 10. May Fly (`MayFly`)
- 11. Instabuild (`Instabuild`)
- 12. Lightning (`Lightning`)
- 13. Fly Speed (`FlySpeed`)
- 14. Walk Speed (`WalkSpeed`)
- 15. Muted (`Muted`)
- 16. World Builder (`WorldBuilder`)
- 17. No Clip (`NoClip`)
"""

T_ModalFormCallback = Callable[[LLSE_Player, bool | None], Any]
T_SimpleFormCallback = Callable[[LLSE_Player, int | None], Any]
T_CustomFormCallback = Callable[
    [LLSE_Player, list[bool | int | str | None] | None],
    Any,
]

class T_NavigatePath(TypedDict):
    """Return value of `LLSE_Player.simulateNavigateTo()`"""

    isFullPath: bool
    path: list[list[int]]
