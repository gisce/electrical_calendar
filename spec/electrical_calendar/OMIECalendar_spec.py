# -*- coding: utf-8 -*-
__author__ = 'XaviTorello'


from expects import *
from expects.testing import failure

from electrical_calendar import OMIECalendar, OMIECalendar
import datetime

with description("A REE Calendar"):

    with context ('can be initialised '):
        with it ('without any parameter'):
            omie_cal = OMIECalendar()
            assert type(omie_cal) == OMIECalendar


    with context ('holidays'):
        with it ('for 2016 will return the expected holidays'):
            omie_cal = OMIECalendar()
            holidays = omie_cal.holidays(2016)
            expected_holidays = [(datetime.date(2016, 1, 1), 'New year'), (datetime.date(2016, 1, 6), 'Epiphany'), (datetime.date(2016, 3, 24), 'Holy Thursday'), (datetime.date(2016, 3, 25), 'Good Friday'), (datetime.date(2016, 5, 2), 'Workers Day next monday'), (datetime.date(2016, 5, 16), 'Second Easter monday'), (datetime.date(2016, 7, 25), 'St Santiago - Galicia National Day'), (datetime.date(2016, 8, 15), 'Assumption of Mary to Heaven'), (datetime.date(2016, 10, 12), 'National Day'), (datetime.date(2016, 11, 1), 'All Saints Day'), (datetime.date(2016, 11, 9), 'St Almudena'), (datetime.date(2016, 12, 6), 'Constitution Day'), (datetime.date(2016, 12, 8), 'Immaculate Conception'), (datetime.date(2016, 12, 26), 'St Stephen')]


            assert len(holidays) == len(expected_holidays)

            for idx,holiday in enumerate(holidays):
                assert holiday == expected_holidays[idx]
        with it ('for 2017 will return the expected holidays'):
            omie_cal = OMIECalendar()
            holidays = omie_cal.holidays(2017)
            expected_holidays = [(datetime.date(2017, 1, 1), 'New year'), (datetime.date(2017, 1, 6), 'Epiphany'), (datetime.date(2017, 4, 13), 'Holy Thursday'), (datetime.date(2017, 4, 14), 'Good Friday'), (datetime.date(2017, 5, 2), 'Workers Day next monday'), (datetime.date(2017, 5, 16), 'Second Easter monday'), (datetime.date(2017, 7, 25), 'St Santiago - Galicia National Day'), (datetime.date(2017, 8, 15), 'Assumption of Mary to Heaven'), (datetime.date(2017, 10, 12), 'National Day'), (datetime.date(2017, 11, 1), 'All Saints Day'), (datetime.date(2017, 11, 9), 'St Almudena'), (datetime.date(2017, 12, 6), 'Constitution Day'), (datetime.date(2017, 12, 8), 'Immaculate Conception'), (datetime.date(2017, 12, 26), 'St Stephen')]

            assert len(holidays) == len(expected_holidays)

            for idx,holiday in enumerate(holidays):
                assert holiday == expected_holidays[idx]

        with context ('detection for fixed dates still works as expected'):
            with it ('for National Day'):
                omie_cal = OMIECalendar()
                day=datetime.date(2016,10,12)
                assert omie_cal.is_holiday(day) == True

                day=datetime.date(2015,10,12)
                assert omie_cal.is_holiday(day) == True

            with it ('for Constitution Day'):
                omie_cal = OMIECalendar()
                day=datetime.date(2016,12,6)
                assert omie_cal.is_holiday(day) == True

                day=datetime.date(2014,12,6)
                assert omie_cal.is_holiday(day) == True



            with it ('for Workers Day next monday'):
                omie_cal = OMIECalendar()
                day=datetime.date(2016,5,2)
                assert omie_cal.is_holiday(day) == True


            with it ('for Second Easter monday'):
                omie_cal = OMIECalendar()
                day=datetime.date(2016,5,16)
                assert omie_cal.is_holiday(day) == True

                day=datetime.date(2014,5,16)
                assert omie_cal.is_holiday(day) == True



            with it ('for St Santiago'):
                omie_cal = OMIECalendar()
                day=datetime.date(2016,7,25)
                assert omie_cal.is_holiday(day) == True

                day=datetime.date(2014,7,25)
                assert omie_cal.is_holiday(day) == True



            with it ('for St Almudena'):
                omie_cal = OMIECalendar()
                day=datetime.date(2016,11,9)
                assert omie_cal.is_holiday(day) == True

                day=datetime.date(2014,11,9)
                assert omie_cal.is_holiday(day) == True



            with it ('for St Stephen'):
                omie_cal = OMIECalendar()
                day=datetime.date(2016,12,26)
                assert omie_cal.is_holiday(day) == True

                day=datetime.date(2014,12,26)
                assert omie_cal.is_holiday(day) == True



            with it ('for a non-holiday day'):
                omie_cal = OMIECalendar()
                day=datetime.date(2016,12,7)
                assert omie_cal.is_holiday(day) == False

                day=datetime.date(2014,04,3)
                assert omie_cal.is_holiday(day) == False


    with context ('working days still detected correctly'):
        with it ('for a workable tuesday 2016/3/1'):
            omie_cal = OMIECalendar()
            day=datetime.date(2016,3,1)
            assert omie_cal.is_workable(day) == True
        with it ('for a workable tuesday 2016/3/1'):
            omie_cal = OMIECalendar()
            day=datetime.date(2016,2,27)
            assert omie_cal.is_workable(day) == False


