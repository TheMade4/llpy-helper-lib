from typing import NoReturn


class LLSE_Device:
    """Player device information object"""

    def __init__(self) -> NoReturn: ...

    @property
    def ip(self) -> str:
        """Player device's IP address and port (format: `114.51.45.191:9810`)"""

    @property
    def avgPing(self) -> int:
        """Player's average network latency time (ms)"""

    @property
    def avgPacketLoss(self) -> float:
        """Player's average network packet loss rate (%)"""

    @property
    def lastPing(self) -> int:
        """Player's network latency time (ms)"""

    @property
    def lastPacketLoss(self) -> float:
        """Player's network packet loss rate (%)"""

    @property
    def os(self) -> str:
        """
        Player device's operating system type

        Possible return values:

        - `Android` | Google Android for mobile phones
        - `iOS` | Apple iOS for mobile phones/iPadOS for tablets
        - `OSX` | Apple macOS for computers
        - `Amazon` | Amazon FireOS for tablets/TVs
        - `GearVR` | Samsung GearVR for headsets
        - `Hololens` | Microsoft HoloLens for headsets
        - `Windows10` | Microsoft Windows for computers
        - `Win32` | Microsoft Win32 for computers (Education Edition?)
        - `TVOS` | Apple tvOS for set-top boxes
        - `PlayStation` | Sony PlayStation for consoles
        - `Nintendo` | Nintendo Switch for handheld consoles
        - `Xbox` | Microsoft Xbox for consoles
        - `WindowsPhone` | Microsoft Windows Mobile for mobile phones
        - `Unknown` | Unknown system
        """

    @property
    def inputMode(self) -> int:
        """
        Player's input mode

        - 1. Mouse (`Mouse`)
        - 2. Touch (`Touch`)
        - 3. Gamepad (`GamePad`)
        - 4. Motion Controller (`MotionController`)
        """

    @property
    def playMode(self) -> int:
        """
        Player's play mode

        (Translated by GPT-3.5)

        - 0. Normal mode (`Normal`)
        - 1. Teaser mode (`Teaser`)
        - 2. Screen mode (`Screen`)
        - 3. Viewer mode (`Viewer`)
        - 4. VR mode (`VR`)
        - 5. Placement mode (`Placement`)
        - 6. Living room mode (`LivingRoom`)
        - 7. Exit level mode (`ExitLevel`)
        - 8. Exit level living room mode (`ExitLevelLivingRoom`)
        """

    @property
    def serverAddress(self) -> str:
        """Address to which the player is connected"""

    @property
    def clientId(self) -> str:
        """Identification code ID of the player's client"""


Device = LLSE_Device
