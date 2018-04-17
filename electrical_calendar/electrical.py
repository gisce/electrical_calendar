# -*- coding: utf-8 -*-
__author__ = 'XaviTorello'

from workalendar.core import WesternCalendar, ChristianMixin, MON, TUE, WED, THU, FRI, SAT, SUN

from datetime import datetime, date, timedelta

from isoweek import Week

import logging

logger = logging.getLogger(__name__)


class ChristianMixin(ChristianMixin):

    def get_version(self):
        print ("Version ")

    def get_same_holiday(self, current, past, day):
        """
        Get the same holiday on another year taking care about non fixed holidays
        """

        # Alternative safier but heavier, match labels instead go to finded
        # index on the past year

        year = past.year
        year_current = current.year

        day_current = current.day(day).day
        month_current = current.day(day).month

        logger.debug("  - Searching {}/{}/{} holiday on {}".format(year_current,
                                                                   month_current, day_current, year))

        index = -1

        for idx, holiday in enumerate(self._holidays[year_current]):
            if holiday[0].day == day_current and holiday[0].month == month_current:
                index = idx

        if index != -1:
            same_holiday = self._holidays[year][index]
            logger.debug("  - Found same holiday: {}/{}/{} [{}]".format(year, same_holiday[
                         0].month, same_holiday[0].day, self._holidays[year][index][1]))

            return datetime(year, same_holiday[0].month, same_holiday[0].day)

        return None

    def get_next_workday(self, year, week, weekday):
        """
        Get the next working day. If entering date is friday or a weekend day, get the first workday of the next week

        It doesn't take care about the holidays, that's are controlled as a second test in ensure_same_day_scenario method

        Returns a datetime.date
        """
        logger.debug(
            "  - Getting next week day since {}".format(Week(year, week).day(weekday)))

        if weekday >= FRI:
            weekday = MON
            week += 1
        else:
            weekday += 1

        return Week(year, week).day(weekday)

    def get_next_weekend_day(self, year, week, weekday):
        """
        Get the next weekend day. If entering date is friday or a weekend day, get the first workday of the next week

        Returns a datetime.date
        """

        logger.debug(
            "  - Getting next weekend day since {}".format(Week(year, week).day(weekday)))

        if weekday == SUN:
            weekday = SAT
            week += 1
        else:
            weekday = SAT

        logger.info("{}".format(Week(year, week).day(weekday)))

        return Week(year, week).day(weekday)

    def is_workable(self, day):
        if type(day) is datetime:
            day = day.date()

        if day.weekday() in self.get_weekend_days():
            return False

        return True


class REECalendar (WesternCalendar, ChristianMixin):
    """
    REE Spanish Electrical Network (Red Eléctrica de España) Calendar
    """

    include_immaculate_conception = True
    include_assumption = True
    include_all_saints = True

    include_epiphany = False
    include_good_friday = False
    include_christmas = False

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, "Worker's day"),
        (10, 12, "National Day"),
        (12, 6, "Constitution Day")
    )
