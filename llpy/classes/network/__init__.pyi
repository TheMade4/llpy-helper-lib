from typing import Any, Callable, NoReturn, overload

from typing_extensions import deprecated

from llpy.types import T_HttpGetResp

from .wsclient import WSClient


class network:
    """Network Interface API"""

    def __init__(self) -> NoReturn: ...

    @overload
    @staticmethod
    def httpGet(url: str, callback: Callable[[int, str], Any]) -> bool:
        """
        Send an asynchronous HTTP(s) GET request.

        Callback Args:
            status (int): HTTP(s) response code returned. For example, 200 for a successful request.
                          If the request execution fails, the `status` value will be `-1`.
            result (str): Specific data returned.

        Args:
            url: Target address of the request (including parameters for GET requests).
            callback: Callback function to be executed when the request returns, used to pass back the HTTP(s) response result.

        Returns:
            Whether the request was successfully sent.
        """

    @overload
    @staticmethod
    def httpGet(url: str, header: dict[str, str], callback: Callable[[int, str], Any]) -> bool:
        """
        Send an asynchronous HTTP(s) GET request.

        Callback Args:
            status (int): HTTP(s) response code returned. For example, 200 for a successful request.
                          If the request execution fails, the `status` value will be `-1`.
            result (str): Specific data returned.

        Args:
            url: Target address of the request (including parameters for GET requests).
            header: Request headers (including Request headers for GET requests).
            callback: Callback function to be executed when the request returns, used to pass back the HTTP(s) response result.

        Returns:
            Whether the request was successfully sent.
        """

    @overload
    @staticmethod
    def httpPost(url: str, data: str, post_type: str, callback: Callable[[int, str], Any]) -> bool:
        """
        Send an asynchronous HTTP(s) POST request.

        Callback Args:
            status (int): HTTP(s) response code returned. For example, 200 for a successful request.
                          If the request execution fails, the `status` value will be `-1`.
            result (str): Specific data returned.

        Args:
            url: Target address of the request.
            data: Data to be sent.
            post_type: Type of Post data to be sent, such as `text/plain` `application/x-www-form-urlencoded`, etc.
            callback: Callback function to be executed when the request returns, used to pass back the HTTP(s) response result.

        Returns:
            Whether the request was successfully sent.
        """

    @overload
    @staticmethod
    def httpPost(url: str, header: dict[str, str], data: str, post_type: str,
                 callback: Callable[[int, str], Any]) -> bool:
        """
        Send an asynchronous HTTP(s) POST request.

        Callback Args:
            status (int): HTTP(s) response code returned. For example, 200 for a successful request.
                          If the request execution fails, the `status` value will be `-1`.
            result (str): Specific data returned.

        Args:
            url: Target address of the request.
            header: Request headers (including Request headers for POST requests).
            data: Data to be sent.
            post_type: Type of Post data to be sent, such as `text/plain` `application/x-www-form-urlencoded`, etc.
            callback: Callback function to be executed when the request returns, used to pass back the HTTP(s) response result.

        Returns:
            Whether the request was successfully sent.
        """

    @staticmethod
    def httpGetSync(url: str) -> T_HttpGetResp: ...

    @deprecated("Please use `WSClient()`")
    @staticmethod
    def newWebSocket() -> WSClient: ...
