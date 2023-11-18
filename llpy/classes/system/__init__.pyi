from typing import Any, Callable, NoReturn

from llpy.types import T_TimeObj


class system:
    """System call API"""

    def __init__(self) -> NoReturn: ...

    @staticmethod
    def getTimeStr() -> str:
        """
        Get the current time as a string

        Returns:
            Current time as a string, using the local timezone and 24-hour format.
            Format example: `2021-04-03 19:15:01`
        """

    @staticmethod
    def getTimeObj() -> T_TimeObj:
        """
        Get the current time object

        Returns:
            Current time object
        """

    @staticmethod
    def randomGuid() -> str:
        """
        Generate a random GUID string

        Returns:
            A randomly generated unique identifier (GUID)
        """

    @staticmethod
    def cmd(
            cmd: str,
            callback: Callable[[int, str], Any],
            time_limit: int = -1,
    ) -> bool:
        """
        Call the shell to execute a specific system command

        Note! This executes commands outside of the Minecraft command system.

        This function works asynchronously, it does not wait for the system to complete the command
        before returning. Instead, the engine automatically calls the provided callback function
        to return the results.

        Callback Args:
            exitcode (int): Shell exit code
            output (str): Content of standard output and standard error output

        Args:
            cmd: The system command to execute
            callback: Callback function used to return data after the shell process ends
            time_limit: Maximum time limit for command execution, in milliseconds.
                        Default is `-1`, meaning no time limit.

        Returns:
            Whether the command was successfully launched
        """

    @staticmethod
    def newProcess(
            process: str,
            callback: Callable[[int, str], Any],
            time_limit: int = -1,
    ) -> bool:
        """
        Run a specified program at a given location

        This function works asynchronously, it does not wait for the system to complete the command
        before returning. Instead, the engine automatically calls the provided callback function
        to return the results.

        Callback Args:
            exitcode (int): Exit code of the program process
            output (str): Content of standard output and standard error output of the program

        Args:
            process: Path to the program to run (along with command line arguments)
            callback: Callback function used to return data after the program process ends
            time_limit: Maximum time limit for program process execution, in milliseconds.
                        Default is `-1`, meaning no time limit.

        Returns:
            Whether the program was successfully launched
        """
