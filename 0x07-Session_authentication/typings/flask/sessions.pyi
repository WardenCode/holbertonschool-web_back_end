"""
This type stub file was generated by pyright.
"""

from werkzeug.datastructures import CallbackDict
from ._compat import collections_abc

"""
    flask.sessions
    ~~~~~~~~~~~~~~

    Implements cookie based sessions based on itsdangerous.

    :copyright: 2010 Pallets
    :license: BSD-3-Clause
"""
class SessionMixin(collections_abc.MutableMapping):
    """Expands a basic dictionary with session attributes."""
    @property
    def permanent(self):
        """This reflects the ``'_permanent'`` key in the dict."""
        ...
    
    @permanent.setter
    def permanent(self, value): # -> None:
        ...
    
    new = ...
    modified = ...
    accessed = ...


class SecureCookieSession(CallbackDict, SessionMixin):
    """Base class for sessions based on signed cookies.

    This session backend will set the :attr:`modified` and
    :attr:`accessed` attributes. It cannot reliably track whether a
    session is new (vs. empty), so :attr:`new` remains hard coded to
    ``False``.
    """
    modified = ...
    accessed = ...
    def __init__(self, initial=...) -> None:
        ...
    
    def __getitem__(self, key):
        ...
    
    def get(self, key, default=...): # -> None:
        ...
    
    def setdefault(self, key, default=...):
        ...
    


class NullSession(SecureCookieSession):
    """Class used to generate nicer error messages if sessions are not
    available.  Will still allow read-only access to the empty session
    but fail on setting.
    """
    setdefault = ...


class SessionInterface:
    """The basic interface you have to implement in order to replace the
    default session interface which uses werkzeug's securecookie
    implementation.  The only methods you have to implement are
    :meth:`open_session` and :meth:`save_session`, the others have
    useful defaults which you don't need to change.

    The session object returned by the :meth:`open_session` method has to
    provide a dictionary like interface plus the properties and methods
    from the :class:`SessionMixin`.  We recommend just subclassing a dict
    and adding that mixin::

        class Session(dict, SessionMixin):
            pass

    If :meth:`open_session` returns ``None`` Flask will call into
    :meth:`make_null_session` to create a session that acts as replacement
    if the session support cannot work because some requirement is not
    fulfilled.  The default :class:`NullSession` class that is created
    will complain that the secret key was not set.

    To replace the session interface on an application all you have to do
    is to assign :attr:`flask.Flask.session_interface`::

        app = Flask(__name__)
        app.session_interface = MySessionInterface()

    .. versionadded:: 0.8
    """
    null_session_class = NullSession
    pickle_based = ...
    def make_null_session(self, app): # -> null_session_class:
        """Creates a null session which acts as a replacement object if the
        real session support could not be loaded due to a configuration
        error.  This mainly aids the user experience because the job of the
        null session is to still support lookup without complaining but
        modifications are answered with a helpful error message of what
        failed.

        This creates an instance of :attr:`null_session_class` by default.
        """
        ...
    
    def is_null_session(self, obj): # -> bool:
        """Checks if a given object is a null session.  Null sessions are
        not asked to be saved.

        This checks if the object is an instance of :attr:`null_session_class`
        by default.
        """
        ...
    
    def get_cookie_domain(self, app): # -> None:
        """Returns the domain that should be set for the session cookie.

        Uses ``SESSION_COOKIE_DOMAIN`` if it is configured, otherwise
        falls back to detecting the domain based on ``SERVER_NAME``.

        Once detected (or if not set at all), ``SESSION_COOKIE_DOMAIN`` is
        updated to avoid re-running the logic.
        """
        ...
    
    def get_cookie_path(self, app):
        """Returns the path for which the cookie should be valid.  The
        default implementation uses the value from the ``SESSION_COOKIE_PATH``
        config var if it's set, and falls back to ``APPLICATION_ROOT`` or
        uses ``/`` if it's ``None``.
        """
        ...
    
    def get_cookie_httponly(self, app):
        """Returns True if the session cookie should be httponly.  This
        currently just returns the value of the ``SESSION_COOKIE_HTTPONLY``
        config var.
        """
        ...
    
    def get_cookie_secure(self, app):
        """Returns True if the cookie should be secure.  This currently
        just returns the value of the ``SESSION_COOKIE_SECURE`` setting.
        """
        ...
    
    def get_cookie_samesite(self, app):
        """Return ``'Strict'`` or ``'Lax'`` if the cookie should use the
        ``SameSite`` attribute. This currently just returns the value of
        the :data:`SESSION_COOKIE_SAMESITE` setting.
        """
        ...
    
    def get_expiration_time(self, app, session): # -> None:
        """A helper method that returns an expiration date for the session
        or ``None`` if the session is linked to the browser session.  The
        default implementation returns now + the permanent session
        lifetime configured on the application.
        """
        ...
    
    def should_set_cookie(self, app, session):
        """Used by session backends to determine if a ``Set-Cookie`` header
        should be set for this session cookie for this response. If the session
        has been modified, the cookie is set. If the session is permanent and
        the ``SESSION_REFRESH_EACH_REQUEST`` config is true, the cookie is
        always set.

        This check is usually skipped if the session was deleted.

        .. versionadded:: 0.11
        """
        ...
    
    def open_session(self, app, request):
        """This method has to be implemented and must either return ``None``
        in case the loading failed because of a configuration error or an
        instance of a session object which implements a dictionary like
        interface + the methods and attributes on :class:`SessionMixin`.
        """
        ...
    
    def save_session(self, app, session, response):
        """This is called for actual sessions returned by :meth:`open_session`
        at the end of the request.  This is still called during a request
        context so if you absolutely need access to the request you can do
        that.
        """
        ...
    


session_json_serializer = ...
class SecureCookieSessionInterface(SessionInterface):
    """The default session interface that stores sessions in signed cookies
    through the :mod:`itsdangerous` module.
    """
    salt = ...
    digest_method = ...
    key_derivation = ...
    serializer = ...
    session_class = SecureCookieSession
    def get_signing_serializer(self, app): # -> URLSafeTimedSerializer | None:
        ...
    
    def open_session(self, app, request): # -> session_class | None:
        ...
    
    def save_session(self, app, session, response): # -> None:
        ...
    


