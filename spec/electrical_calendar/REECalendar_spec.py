# -*- coding: utf-8 -*-
__author__ = 'XaviTorello'

from expects import *
from expects.testing import failure

from electrical_calendar import REECalendar, OMIECalendar
import datetime

with description("A REE Calendar"):

    with context ('can be initialised '):
        with it ('without any parameter'):
            ree_cal = REECalendar()
            assert type(ree_cal) == REECalendar


    with context ('holidays'):
        with it ('for 2016 will return the expected holidays'):
            ree_cal = REECalendar()
            holidays = ree_cal.holidays(2016)
            expected_holidays = [(datetime.date(2016, 1, 1), 'New year'), (datetime.date(2016, 3, 25), 'Good Friday'), (datetime.date(2016, 5, 1), "Worker's Day"), (datetime.date(2016, 8, 15), 'Assumption of Mary to Heaven'), (datetime.date(2016, 10, 12), 'National Day'), (datetime.date(2016, 11, 1), 'All Saints Day'), (datetime.date(2016, 12, 6), 'Constitution Day'), (datetime.date(2016, 12, 8), 'Immaculate Conception'), (datetime.date(2016, 12, 25), 'Christmas Day')]

            assert len(holidays) == len(expected_holidays)
            for idx,holiday in enumerate(holidays):
                assert holiday == expected_holidays[idx]
        with it ('for 2017 will return the expected holidays'):
            ree_cal = REECalendar()
            holidays = ree_cal.holidays(2017)
            expected_holidays = [(datetime.date(2017, 1, 1), 'New year'), (datetime.date(2017, 5, 1), "Worker's Day"), (datetime.date(2017, 8, 15), 'Assumption of Mary to Heaven'), (datetime.date(2017, 10, 12), 'National Day'), (datetime.date(2017, 11, 1), 'All Saints Day'), (datetime.date(2017, 12, 6), 'Constitution Day'), (datetime.date(2017, 12, 8), 'Immaculate Conception')]

            assert len(holidays) == len(expected_holidays)

            for idx,holiday in enumerate(holidays):
                assert holiday == expected_holidays[idx]

        with context ('detection for fixed dates still works as expected'):
            with it ('for National Day'):
                ree_cal = REECalendar()
                day=datetime.date(2016,10,12)
                assert ree_cal.is_holiday(day) == True

                day=datetime.date(2015,10,12)
                assert ree_cal.is_holiday(day) == True

            with it ('for Constitution Day'):
                ree_cal = REECalendar()
                day=datetime.date(2016,12,6)
                assert ree_cal.is_holiday(day) == True

                day=datetime.date(2014,12,6)
                assert ree_cal.is_holiday(day) == True

            with it ('for a non-holiday day'):
                ree_cal = REECalendar()
                day=datetime.date(2016,12,7)
                assert ree_cal.is_holiday(day) == False

                day=datetime.date(2014,4,3)
                assert ree_cal.is_holiday(day) == False


    with context ('working days still detected correctly'):
        with it ('for a workable tuesday 2016/3/1'):
            ree_cal = REECalendar()
            day=datetime.date(2016,3,1)
            assert ree_cal.is_workable(day) == True
        with it ('for a workable tuesday 2016/3/1'):
            ree_cal = REECalendar()
            day=datetime.date(2016,2,27)
            assert ree_cal.is_workable(day) == False
