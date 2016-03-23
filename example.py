from electrical_calendar import REECalendar, OMIECalendar

from datetime import datetime
#logging.basicConfig(level=logging.DEBUG)


# Electrical Spanish Network Calendar aka Red Electrica de Espana
ree_cal = REECalendar()

# OMIE Spanish Electrical Market Calendar
omie_cal = OMIECalendar()

print omie_cal.holidays(2016)
print omie_cal.holidays(2017)

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
ree_cal.is_workable(day)
# Return True

# Review if 2016/2/27 (sunday) is workable (if it's a weekday)
day=datetime(2016,2,27)
ree_cal.is_workable(day)
# Return False


