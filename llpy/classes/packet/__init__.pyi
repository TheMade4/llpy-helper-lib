from typing import NoReturn

from llpy import FloatPos, NativePointer
from llpy.classes.nbt.compound import NbtCompound

class LLSE_Packet:
    """Packet Object"""

    def __init__(self) -> NoReturn: ...

    def asPointer(self) -> NativePointer: ...
    def getName(self) -> str: ...
    def getId(self) -> int: ...


Packet = LLSE_Packet

class BinaryStream:
    """Binary Stream Object"""

    def __init__(self) -> None:
        """Create a binary stream object"""

    def reset(self) -> bool:
        """
        Reset the binary stream

        Returns:
            Whether successful
        """

    def reserve(self, size: int) -> bool:
        """
        Allocate space for the binary stream

        Args:
            size: Number of bytes to allocate

        Returns:
            Whether successful
        """

    def writeBool(self, value: bool) -> bool:
        """
        Write a boolean value to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeByte(self, value: int) -> bool:
        """
        Write a byte to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeDouble(self, value: float) -> bool:
        """
        Write a double-precision floating-point number to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeFloat(self, value: float) -> bool:
        """
        Write a single-precision floating-point number to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeSignedBigEndianInt(self, value: int) -> bool:
        """
        Write a big-endian signed integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeSignedInt(self, value: int) -> bool:
        """
        Write a signed integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeSignedInt64(self, value: int) -> bool:
        """
        Write a signed 64-bit integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeSignedShort(self, value: int) -> bool:
        """
        Write a signed short integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeString(self, value: str) -> bool:
        """
        Write a string to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeUnsignedChar(self, value: int) -> bool:
        """
        Write an unsigned char to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeUnsignedInt(self, value: int) -> bool:
        """
        Write an unsigned integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeUnsignedInt64(self, value: int) -> bool:
        """
        Write an unsigned 64-bit integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeUnsignedShort(self, value: int) -> bool:
        """
        Write an unsigned short integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeUnsignedVarInt(self, value: int) -> bool:
        """
        Write an unsigned variable-length integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeUnsignedVarInt64(self, value: int) -> bool:
        """
        Write an unsigned variable-length 64-bit integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeVarInt(self, value: int) -> bool:
        """
        Write a variable-length integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeVarInt64(self, value: int) -> bool:
        """
        Write a variable-length 64-bit integer to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeVec3(self, value: FloatPos) -> bool:
        """
        Write a three-dimensional vector (coordinates) to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def writeCompoundTag(self, value: NbtCompound) -> bool:
        """
        Write an NBT tag to the binary stream

        Args:
            value: Data to write

        Returns:
            Whether successful
        """

    def createPacket(self, pkt_id: int) -> LLSE_Packet:
        """
        Build a packet from the binary stream

        Args:
            pkt_id: Packet ID

        Returns:
            Packet object
        """

    def getData(self) -> str: ...
