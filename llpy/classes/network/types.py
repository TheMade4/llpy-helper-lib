from typing import Any, Callable, Literal, TypedDict

from .httprequest import HttpRequest
from .httpresponse import HttpResponse

class T_HttpGetResp(TypedDict):
    """Response result returned by `network.httpGetSync()`"""

    status: int
    """HTTP(s) response code returned, e.g., 200 for a successful request. If the request fails, the `status` value will be `-1`"""
    data: str
    """Specific data returned"""

T_WSClientStatusOpen = Literal[0]
T_WSClientStatusClosing = Literal[1]
T_WSClientStatusClosed = Literal[2]
T_WSClientStatus = (
    T_WSClientStatusOpen | T_WSClientStatusClosing | T_WSClientStatusClosed
)

T_HTTPServerListener = Callable[[HttpRequest, HttpResponse], Any]
T_HTTPServerPreRoutingListener = Callable[[HttpRequest, HttpResponse], bool]
T_HTTPServerExceptionListener = Callable[[HttpRequest, HttpResponse, str], Any]
