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
HistoricalObsResource.set_set_app_key('{YOUR_APP_KEY}')
```

## Try It Out
Let's test out our install by requesting the stations nearest to New Orleans, LA:

```python
import arrow
import json
from skywisehistoricalobs import Station

lat = 30.426
lon = -89.065

stations = Station.nearest(lat, lon)
for station in stations:
    print station.description, '---', station.distance, '---', station.coverage
```

Your output should look something similar to this:

```bash
SUPERDOME HELIPORT US LA KVSH --- 3.1755267192 --- {u'starts_at': u'2012-07-26T00:00:00Z', u'ends_at': u'2015-01-28T00:00:00Z'}
NEW ORLEANS AUDUBON GOLF SITE (AUDUBON PARK) US LA  --- 3.2098946522 --- {u'starts_at': u'1948-07-01T00:00:00Z', u'ends_at': u'1949-01-01T00:00:00Z'}
NEW ORLEANS SUPERDOME HELIPORT US LA  --- 3.4753621144 --- {u'starts_at': u'2014-07-31T00:00:00Z', u'ends_at': u'2015-01-28T00:00:00Z'}
NEW CANAL US LA  --- 10.423849619 --- {u'starts_at': u'2008-07-21T00:00:00Z', u'ends_at': u'2016-11-23T00:00:00Z'}
NEW ORLEANS NAS US LA  --- 12.1181794653 --- {u'starts_at': u'1949-01-01T00:00:00Z', u'ends_at': u'1957-12-31T00:00:00Z'}
NEW ORLEANS ALVIN CALLENDER F US LA KNBG --- 14.2452410532 --- {u'starts_at': u'1958-01-01T00:00:00Z', u'ends_at': u'1972-12-31T00:00:00Z'}
NEW ORLEANS NAS US LA KNBG --- 14.2452410532 --- {u'starts_at': u'1973-01-01T00:00:00Z', u'ends_at': u'2016-11-24T00:00:00Z'}
LAKEFRONT US LA KNEW --- 14.3426304182 --- {u'starts_at': u'2000-01-01T00:00:00Z', u'ends_at': u'2003-12-31T00:00:00Z'}
LAKEFRONT AIRPORT US LA KNEW --- 15.3230758821 --- {u'starts_at': u'1942-09-01T00:00:00Z', u'ends_at': u'2016-11-24T00:00:00Z'}
LOUIS ARMSTRONG NEW ORLEANS INTL AP US LA KMSY --- 16.6191771139 --- {u'starts_at': u'1945-10-01T00:00:00Z', u'ends_at': u'2016-11-24T00:00:00Z'}
```

We can now get the observations from the nearby Lakefront Airport during the historic landfall of hurricane Katrina in 2005.

```python
gulfport = stations[-2]
start = arrow.get(2005, 8, 29, 6, 00)
end = arrow.get(2005, 8, 31, 00, 00)
katrina_obs = gulfport.observations(start=start, end=end)

for ob in katrina_obs:
    for measurement in ob.measurements:
        if measurement['parameter'] == 'wind_speed':
            print ob.recorded_at, ': ',  measurement['value'], measurement['units']
```

You should see output like :

(Note: the station stopped reporting just after landfall, which occurred around 11:00 UTC on the 29th)

```bash
2005-08-29 06:00:00+00:00 :  20.1 meters_per_second
2005-08-29 06:12:00+00:00 :  20.1 meters_per_second
2005-08-29 06:23:00+00:00 :  21.1 meters_per_second
2005-08-29 06:39:00+00:00 :  19.6 meters_per_second
2005-08-29 06:53:00+00:00 :  23.2 meters_per_second
2005-08-29 07:00:00+00:00 :  19.6 meters_per_second
2005-08-29 07:07:00+00:00 :  23.7 meters_per_second
2005-08-29 07:15:00+00:00 :  21.1 meters_per_second
2005-08-29 07:27:00+00:00 :  18.0 meters_per_second
2005-08-29 07:35:00+00:00 :  18.0 meters_per_second
2005-08-29 07:44:00+00:00 :  19.6 meters_per_second
2005-08-29 07:53:00+00:00 :  19.6 meters_per_second
2005-08-29 08:03:00+00:00 :  19.0 meters_per_second
2005-08-29 08:09:00+00:00 :  20.1 meters_per_second
2005-08-29 08:16:00+00:00 :  19.0 meters_per_second
2005-08-29 08:21:00+00:00 :  21.1 meters_per_second
2005-08-29 08:28:00+00:00 :  19.6 meters_per_second
2005-08-29 08:36:00+00:00 :  15.4 meters_per_second
2005-08-29 08:43:00+00:00 :  22.7 meters_per_second
2005-08-29 08:46:00+00:00 :  23.2 meters_per_second
2005-08-29 08:53:00+00:00 :  24.2 meters_per_second
2005-08-29 09:00:00+00:00 :  21.6 meters_per_second
2005-08-29 09:29:00+00:00 :  21.6 meters_per_second
2005-08-29 09:37:00+00:00 :  23.7 meters_per_second
2005-08-29 09:45:00+00:00 :  24.7 meters_per_second
2005-08-29 09:53:00+00:00 :  24.2 meters_per_second
2005-08-29 10:03:00+00:00 :  25.2 meters_per_second
2005-08-29 10:29:00+00:00 :  24.2 meters_per_second
2005-08-29 10:53:00+00:00 :  27.3 meters_per_second
2005-08-29 11:02:00+00:00 :  24.7 meters_per_second
2005-08-29 11:05:00+00:00 :  26.8 meters_per_second
2005-08-29 11:53:00+00:00 :  30.9 meters_per_second
```

# Links
- [Historical Obs API HTTP Interface docs](http://docs.api.wdtinc.com/historical-obs-api/en/latest/)