from requests import HTTPError


class FreshsalesError(HTTPError):
    """
    Base error class.

    Subclassing HTTPError to avoid breaking existing code that expects only HTTPErrors.
    """


class FreshsalesBadRequest(FreshsalesError):
    """Most 40X and 501 status codes"""


class FreshsalesUnauthorized(FreshsalesError):
    """401 Unauthorized"""


class FreshsalesAccessDenied(FreshsalesError):
    """403 Forbidden"""


class FreshsalesNotFound(FreshsalesError):
    """404"""


class FreshsalesRateLimited(FreshsalesError):
    """429 Rate Limit Reached"""


class FreshsalesServerError(FreshsalesError):
    """50X errors"""
