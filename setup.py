# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

INSTALL_REQUIRES = ['workalendar', 'isoweek']

setup(
    name='electrical_calendar',
    description='Electrical sector holidays and workdays using workalendar. Spain and Portugal data',
    version='0.0.1',
    url='https://www.gisce.net',
    author='GISCE Enginyeria, SL',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='General Public Licence 3',
    provides=['electrical_calendar']
)
