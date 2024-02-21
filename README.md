[![Python Application](https://github.com/anthonykgross/python-calendar/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/anthonykgross/python-calendar/actions/workflows/main.yml)
# python-calendar


## Install
**From PyPI**
```commandline
pip install python-calendar
```

**From source**
```commandline
rm build/ python_calendar.egg-info dist -Rf
python3 setup.py bdist_wheel
pip3 install -I dist/python_calendar-*-py3-none-any.whl
```

## How to use
```python
from python_calendar import Calendar
from dateutil.parser import parse

date_from = parse('2023-08-23')
date_to = parse('2024-08-23')
calendar = Calendar.get(date_from, date_to)

'Nb days : %s' % len(calendar.days) 
#Nb days : 366

'Nb weeks : %s' % len(calendar.weeks) 
#Nb weeks : 53

'Nb days for the 18th week in 2024 : %s' % len(calendar.nodes['2024-W18'].days) 
#Nb days for the 18th week in 2024 : 7

'Nb months : %s' % len(calendar.months) 
#Nb months : 13

'Nb days for Feb 2024 : %s' % len(calendar.nodes['2024-02'].days) 
#Nb days for Feb 2024 : 29

'Nb years : %s' % len(calendar.years) 
#Nb years : 2

'Nb days in 2024 : %s' % len(calendar.nodes['2024'].days) 
#Nb days in 2024 : 235

calendar.days[0]
# 2023-08-23

calendar.days[-1]
# 2024-08-22

for d in calendar.nodes['2024-W34'].days:
    print(d.date)
# 2024-08-19 00:00:00
# 2024-08-20 00:00:00
# 2024-08-21 00:00:00
# 2024-08-22 00:00:00
```

## Contributors
**Anthony K GROSS**
- <http://anthonykgross.fr>
- <https://twitter.com/anthonykgross>
- <https://github.com/anthonykgross>

## Copyright and license
Code and documentation copyright 2024. Code released under [the MIT license](https://github.com/anthonykgross/python-calendar/blob/main/LICENSE).