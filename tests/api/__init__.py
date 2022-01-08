import logging

from rest_api_client import HttpClient
from .testapis import TestAPIs


logger = logging.getLogger('http_logger')


class TestRestAPI(HttpClient):
    _WRAPPERS = [
        TestAPIs
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.testapis = None

        for e in self._WRAPPERS:
            attr_name = e.__name__.lower()
            setattr(self, attr_name, e(self))
