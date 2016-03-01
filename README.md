# Electrical Calendar

Provides a simple way to identify the electrical sector holidays and workdays using workalendar. 

Includes data for Spain and Portugal (WIP) data

It's important to say that the Electrical sector have a peculiar set of holidays, different than the main country holidays.


## How to use it

Just import it    # WIP pip installer [issue #1]
```
from electrical_calendar.electrical_calendar import REECalendar
``` 

and 
```
from datetime import datetime
#logging.basicConfig(level=logging.DEBUG)

from electrical_calendar.electrical_calendar import REECalendar
ree_cal = REECalendar()

# Get all holidays for 2016
print ree_cal.holidays(2016)

# Get all holidays for 2017
print ree_cal.holidays(2017)

# Review if 2016/5/1 is a holiday
day=datetime(2016,5,1)
ree_cal.is_holiday(day)
# Return True

# Review if 2016/3/1 is a holiday
day=datetime(2016,3,1)
ree_cal.is_holiday(day)
# Return False

# Review if 2016/3/1 (tuesday) is workable (if it's a weekday)
ree_cal.is_worable(day)
# Return True

# Review if 2016/2/27 (sunday) is workable (if it's a weekday)
day=datetime(2016,2,27)
ree_cal.is_worable(day)
# Return False


```

## Example of use

[GIST usage example](https://gist.github.com/XaviTorello/3b90b44983986a751685)


