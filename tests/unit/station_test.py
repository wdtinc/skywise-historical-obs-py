from tests import load_fixture
from tests.unit import HistoricalObsTest

from skywisehistoricalobs import Station


class StationTest(HistoricalObsTest):

    def test_nearest(self):

        # Test Defaults
        json = load_fixture('nearest_stations')
        self.adapter.register_uri('GET', '/stations/35.5/-97.3',
                                  json=json)
        stations = Station.nearest(35.5, -97.3)
        self.assertEqual(len(stations), 3)

        # Test Limit
        self.adapter.register_uri('GET', '/stations/35.5/-97.3?limit=3',
                                  json=json)
        stations = Station.nearest(35.5, -97.3, limit=3)
        self.assertEqual(len(stations), 3)

        # Test Radius
        self.adapter.register_uri('GET', '/stations/35.5/-97.3?radius=25.5',
                                  json=json)
        stations = Station.nearest(35.5, -97.3, radius=25.5)
        self.assertEqual(len(stations), 3)

    def test_observations(self):

        station_json = load_fixture('station')
        station = Station()
        station.id = station_json['id']
        station.description = station_json['description']
        station.location = station_json['location']

        observations_json = load_fixture('observations')
        self.adapter.register_uri('GET', '/stations/%s/observations' % station_json['id'],
                                  json=observations_json)
        observations = station.observations()
        self.assertEqual(len(observations), len(observations_json))
