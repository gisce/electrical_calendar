# -*- coding: utf-8 -*-
__author__ = 'XaviTorello'

from .electrical import REECalendar

import logging
logger = logging.getLogger(__name__)


class OMIECalendar (REECalendar):
    """
    OMIE (Spanish Electrical Market) Calendar
    """

    include_immaculate_conception = True
    include_assumption = True
    include_all_saints = True

    include_epiphany = True
    include_holy_thursday = True
    include_good_friday = True

    include_easter_monday = False
    include_christmas = False

    FIXED_HOLIDAYS = REECalendar.FIXED_HOLIDAYS + (
        (5, 2, "Workers Day next monday"),
        (5, 16, "Second Easter monday"),
        (7, 25, "St Santiago - Galicia National Day"),
        (11, 9, "St Almudena"),
        (12, 26, "St Stephen")
    )
