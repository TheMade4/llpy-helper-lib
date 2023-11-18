from typing import NoReturn


class HttpRequest:
    """HTTP Request Object"""

    def __init__(self) -> NoReturn: ...

    @property
    def headers(self) -> dict[str, list[str]]:
        """Request headers"""

    @property
    def method(self) -> str:
        """Request method"""

    @property
    def body(self) -> str:
        """Request content"""

    @property
    def path(self) -> str:
        """Request path"""

    @property
    def params(self) -> dict[str, str | list[str]]:
        """Request query parameters"""

    @property
    def query(self) -> dict[str, str | list[str]]:
        """Request query parameters"""

    @property
    def remoteAddr(self) -> str:
        """Request source address"""

    @property
    def remotePort(self) -> int:
        """Request source port"""

    @property
    def version(self) -> str:
        """Request version"""

    @property
    def matches(self) -> list[str]:
        """
        Request path regex matching results

        The first element (`[0]`) is the original text, and subsequent elements are the matching results.
        """

    def getHeader(self, name: str) -> list[str]:
        """
        Get the value of the specified request header

        Args:
            name: Request header name

        Returns:
            Array of values for the request header (returns an empty array if the header is not present)
        """
