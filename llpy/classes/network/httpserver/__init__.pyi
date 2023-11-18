from ..types import (
    T_HTTPServerExceptionListener,
    T_HTTPServerListener,
    T_HTTPServerPreRoutingListener,
)


class HttpServer:
    """HTTP Server Object"""

    def __init__(self) -> None:
        """Create a new server object"""

    def onGet(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        Listen for GET requests

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object

        Args:
            path: Request path, starting with `/`, may include regular expressions. Example: `/test/(.+)`. If multiple paths match the regular expression, the first defined path is chosen.
            callback: Callback function

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onPut(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        Listen for PUT requests

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object

        Args:
            path: Request path, starting with `/`, may include regular expressions. Example: `/test/(.+)`. If multiple paths match the regular expression, the first defined path is chosen.
            callback: Callback function

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onPost(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        Listen for POST requests

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object

        Args:
            path: Request path, starting with `/`, may include regular expressions. Example: `/test/(.+)`. If multiple paths match the regular expression, the first defined path is chosen.
            callback: Callback function

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onPatch(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        Listen for PATCH requests

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object

        Args:
            path: Request path, starting with `/`, may include regular expressions. Example: `/test/(.+)`. If multiple paths match the regular expression, the first defined path is chosen.
            callback: Callback function

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onDelete(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        Listen for DELETE requests

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object

        Args:
            path: Request path, starting with `/`, may include regular expressions. Example: `/test/(.+)`. If multiple paths match the regular expression, the first defined path is chosen.
            callback: Callback function

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onOptions(self, path: str, callback: T_HTTPServerListener) -> HttpServer:
        """
        Listen for OPTIONS requests

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object

        Args:
            path: Request path, starting with `/`, may include regular expressions. Example: `/test/(.+)`. If multiple paths match the regular expression, the first defined path is chosen.
            callback: Callback function

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onPreRouting(self, callback: T_HTTPServerPreRoutingListener) -> HttpServer:
        """
        Listen for PreRouting pre-routing events

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object. Can modify the response in the callback function

        Callback Returns:
            If `False` is returned, routing to the corresponding callback function for the path will not continue (but the `PostRouting` event will still be triggered).

        Args:
            callback: Callback function, called when a request is received.

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onPostRouting(self, callback: T_HTTPServerListener) -> HttpServer:
        """
        Listen for PostRouting post-routing events

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object. Can modify the response in the callback function

        Args:
            callback: Callback function, called after the callback function for the corresponding directory (or the `PreRouting` event) has completed

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onError(self, callback: T_HTTPServerListener) -> HttpServer:
        """
        Listen for Error error events

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object

        Args:
            callback: Callback function, called when an error (status code >= `400`) occurs

        Returns:
            Server object after processing (for chaining other operations)
        """

    def onException(self, callback: T_HTTPServerExceptionListener) -> HttpServer:
        """
        Listen for Error error events

        Callback Args:
            request (HttpRequest): HTTP request object
            response (HttpResponse): HTTP response object. Can modify the response in the callback function
            exception (str): Exception information

        Args:
            callback: Callback function, called when an exception is thrown in the `handler`

        Returns:
            Server object after processing (for chaining other operations)
        """

    def listen(self, addr: str, port: int) -> HttpServer:
        """
        Listen on a port and start the server

        Args:
            addr: Listening address, can be an IP address or domain name
            port: Listening port

        Returns:
            Server object after processing (for chaining other operations)
        """

    def startAt(self, addr: str, port: int) -> HttpServer:
        """
        Listen on a port and start the server

        Args:
            addr: Listening address, can be an IP address or domain name
            port: Listening port

        Returns:
            Server object after processing (for chaining other operations)
        """

    def stop(self) -> None:
        """Stop the server"""

    def close(self) -> None:
        """Stop the server"""

    def isRunning(self) -> bool:
        """
        Get whether the server is running

        Returns:
            Whether the server is running or not
        """
