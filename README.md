[![Build Status](https://travis-ci.org/wdtinc/skywise-historical-obs-py.svg?branch=master)](https://travis-ci.org/wdtinc/skywise-historical-obs-py)

# Overview
A Python client library for the Historical Obs API. Check out [the API docs](http://docs.api.wdtinc.com/historical-obs-api/en/latest/overview.html) to reference exposed endpoints.

# Installation

## Prerequisites

- [Python 2.7](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

```bash
pip install skywise-historical-obs
```

> **Windows Users**
> You will most likely need to install **gevent** beforehand. You can typically find the latest wheel [here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gevent).

## Configure App ID/Key
The easiest (and recommended) way to configure authentication to the API is by setting the following environment variables:

```bash
SKYWISE_HISTORICAL_OBS_APP_ID='{YOUR_APP_ID}'
SKYWISE_HISTORICAL_OBS_APP_KEY='{YOUR_APP_KEY}'
```

Otherwise, you'll need to set your App ID/Key explicitly in your app/script before making API calls:

```python
from skywisehistoricalobs import HistoricalObsResource

HistoricalObsResource.set_app_id('{YOUR_APP_ID}')
HistoricalObsResource.set_app_key('{YOUR_APP_KEY}')
```

## Try It Out
Let's test out our install by requesting the stations nearest to the Lakefront Airport in New Orleans, LA:

```python
import arrow
import json
from skywisehistoricalobs import Station

lat = 30.037
lon = -90.039

lakefront = Station.nearest(lat, lon)[0]
print lakefront
```

Your output should look something similar to this:

```bash
{u'distance': 1.6430734391, u'latest_recorded_at': u'2016-12-13T00:00:00Z', u'description': u'LAKEFRONT AIRPORT US LA KNEW', u'earliest_recorded_at': u'1942-09-01T00:00:00Z', u'location': {u'latitude': 30.049, u'elevation': 2.7, u'longitude': -90.029}, u'id': u'722315-53917'}
```

We can now get the observations from the nearby Lakefront Airport during the historic landfall of hurricane Katrina in 2005.

```python
start = arrow.get(2005, 8, 29, 11, 00)
end = arrow.get(2005, 8, 29, 12, 00)
katrina_obs = lakefront.observations(start=start, end=end)

print katrina_obs[-1]
```

You should see output like :


```bash
{u'metar': u'08/29/05 05:53:00 METAR KNEW 291153Z 04060G75KT 1/4SM FG SCT001 BKN009 OVC016 26/A2859 RMK AO2 PRESFR SLP679 P0123 60663 70719 T0261 10267 20250 58182 RVRNO', u'measurements': [{u'parameter': u'wind_direction', u'value': 40, u'unit': u'degrees'}, {u'parameter': u'wind_speed', u'value': 30.9, u'unit': u'meters_per_second'}, {u'parameter': u'visibility', u'value': 402, u'unit': u'meters'}, {u'parameter': u'temperature', u'value': 26.1, u'unit': u'celsius'}, {u'parameter': u'wind_gust', u'value': 38.6, u'unit': u'mps'}, {u'parameter': u'cloud_cover', u'value': 100, u'unit': u'percent'}, {u'parameter': u'precipitation_1h', u'value': 31.2, u'unit': u'millimeters'}, {u'parameter': u'precipitation_6h', u'value': 168.4, u'unit': u'millimeters'}, {u'parameter': u'precipitation_24h', u'value': 182.6, u'unit': u'millimeters'}, {u'parameter': u'altimeter', u'value': 968.2, u'unit': u'millibars'}], u'recorded_at': u'2005-08-29T11:53:00Z'}
```

# Links
- [Historical Obs API HTTP Interface docs](http://docs.api.wdtinc.com/historical-obs-api/en/latest/)
