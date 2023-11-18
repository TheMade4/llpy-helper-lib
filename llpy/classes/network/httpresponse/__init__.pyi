from typing import Any, NoReturn


class HttpResponse:
    """HTTP Response Object"""

    def __init__(self) -> NoReturn: ...

    @property
    def headers(self) -> dict[str, list[str]]:
        """Response headers"""

    @property
    def status(self) -> int:
        """Response status code"""

    @property
    def body(self) -> str:
        """Response content"""

    @property
    def version(self) -> str:
        """Response version"""

    @property
    def reason(self) -> str:
        """Error reason"""

    def getHeader(self, name: str) -> list[str]:
        """
        Get the value of the specified response header

        Args:
            name: Response header name

        Returns:
            Array of values for the response header (an empty array if the header is not present)
        """

    def setHeader(self, name: str, value: Any) -> HttpResponse:
        """
        Set the value of the specified response header

        Args:
            name: Response header name
            value: Response header value

        Returns:
            Processed response object
        """

    def write(self, *args: Any) -> HttpResponse:
        """
        Write response content

        Note: This function currently functions as `res.body += arg1 + arg2 + ...`

        Args:
            *args: Response content

        Returns:
            Processed response object
        """
