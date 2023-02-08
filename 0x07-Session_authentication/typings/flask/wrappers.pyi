"""
This type stub file was generated by pyright.
"""

from werkzeug.wrappers import Request as RequestBase, Response as ResponseBase
from werkzeug.wrappers.json import JSONMixin as _JSONMixin
from . import json

"""
    flask.wrappers
    ~~~~~~~~~~~~~~

    Implements the WSGI wrappers (request and response).

    :copyright: 2010 Pallets
    :license: BSD-3-Clause
"""
class JSONMixin(_JSONMixin):
    json_module = json
    def on_json_loading_failed(self, e):
        ...
    


class Request(RequestBase, JSONMixin):
    """The request object used by default in Flask.  Remembers the
    matched endpoint and view arguments.

    It is what ends up as :class:`~flask.request`.  If you want to replace
    the request object used you can subclass this and set
    :attr:`~flask.Flask.request_class` to your subclass.

    The request object is a :class:`~werkzeug.wrappers.Request` subclass and
    provides all of the attributes Werkzeug defines plus a few Flask
    specific ones.
    """
    url_rule = ...
    view_args = ...
    routing_exception = ...
    @property
    def max_content_length(self): # -> None:
        """Read-only view of the ``MAX_CONTENT_LENGTH`` config key."""
        ...
    
    @property
    def endpoint(self): # -> None:
        """The endpoint that matched the request.  This in combination with
        :attr:`view_args` can be used to reconstruct the same or a
        modified URL.  If an exception happened when matching, this will
        be ``None``.
        """
        ...
    
    @property
    def blueprint(self): # -> None:
        """The name of the current blueprint"""
        ...
    


class Response(ResponseBase, JSONMixin):
    """The response object that is used by default in Flask.  Works like the
    response object from Werkzeug but is set to have an HTML mimetype by
    default.  Quite often you don't have to create this object yourself because
    :meth:`~flask.Flask.make_response` will take care of that for you.

    If you want to replace the response object used you can subclass this and
    set :attr:`~flask.Flask.response_class` to your subclass.

    .. versionchanged:: 1.0
        JSON support is added to the response, like the request. This is useful
        when testing to get the test client response data as JSON.

    .. versionchanged:: 1.0

        Added :attr:`max_cookie_size`.
    """
    default_mimetype = ...
    @property
    def max_cookie_size(self): # -> int:
        """Read-only view of the :data:`MAX_COOKIE_SIZE` config key.

        See :attr:`~werkzeug.wrappers.BaseResponse.max_cookie_size` in
        Werkzeug's docs.
        """
        ...
    


