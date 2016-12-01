import requests_mock
from unittest import TestCase

from skywisehistoricalobs import HistoricalObsResource


class HistoricalObsTest(TestCase):

    def setUp(self):
        HistoricalObsResource.set_site('http://my.skywise.host')
        HistoricalObsResource.set_user('my-skywise-user')
        HistoricalObsResource.set_password('my-skywise-password')
        HistoricalObsResource.set_use_session_for_async(True)

        self.adapter = requests_mock.Adapter()
        session = HistoricalObsResource.get_session()
        session.mount('http://my.skywise.host', self.adapter)
