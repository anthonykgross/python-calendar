import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

VERSION = (1, 0, 1)


def get_version():
    return ".".join(map(str, VERSION))


__version__ = get_version()


class Day:
    """

    :param week: Number of the week
    :type week: int

    :param day: Number of the day in the month
    :type day: int

    :param month: Number of the month
    :type month: int

    :param year: The year
    :type year: int
    """
    key = '%Y-%m-%d'

    def __init__(self, date):
        """
        Create a :class:`~python_calendar.Day` based on :class:`~datetime.datetime`

        :param date: The date to analyze
        :type date: datetime
        """
        self.date = date

    @property
    def week(self):
        return self.date.isocalendar()[1]

    @property
    def day(self):
        return self.date.day

    @property
    def month(self):
        return self.date.month

    @property
    def year(self):
        return self.date.year

    @staticmethod
    def get_key(day):
        return day.date.strftime(Day.key)


class Week:
    key = '%s-W%s'

    def __init__(self, day):
        """
        Create a :class:`~python_calendar.Week` based on :class:`~python_calendar.Day`

        :param day: The day to analyze
        :type day: Day
        """
        self.number = day.week
        self.year = day.year
        self.days = []

    @staticmethod
    def get_key(day):
        return Week.key % (
            day.year,
            str(day.week).zfill(2)
        )


class Month:
    key = '%s-%s'

    def __init__(self, day):
        """
        Create a :class:`~python_calendar.Month` based on :class:`~python_calendar.Day`

        :param day: The day to analyze
        :type day: Day
        """
        self.number = day.month
        self.year = day.year
        self.days = []

    @staticmethod
    def get_key(day):
        return Month.key % (
            day.year,
            str(day.month).zfill(2)
        )


class Year:
    key = '%s'

    def __init__(self, day):
        """
        Create a :class:`~python_calendar.Year` based on :class:`~python_calendar.Day`

        :param day: The day to analyze
        :type day: Day
        """
        self.days = []

    @staticmethod
    def get_key(day):
        return Year.key % (
            day.year
        )


class Calendar:
    """

    :param nodes: List of nodes
    :type nodes: dict

    :param days: List of Day
    :type days: Day[]

    :param weeks: List of Week
    :type weeks: Week[]

    :param months: List of Month
    :type months: Month[]

    :param years: List of Year
    :type years: Year[]
    """
    def __init__(self):
        self.nodes = {}

    @property
    def days(self):
        return self.__get("^\d{4}-\d{2}-\d{2}$")

    @property
    def weeks(self):
        return self.__get("^\d{4}-W\d{2}$")

    @property
    def months(self):
        return self.__get("^\d{4}-\d{2}$")

    @property
    def years(self):
        return self.__get("^\d{4}$")

    def __get(self, regexp):
        result = []
        for key in self.nodes.keys():
            s = re.search(regexp, key)
            if s:
                result.append(s.group())
        return result

    def __add(self, day, t):
        if not isinstance(day, Day):
            raise Exception('`day` must be a instance of Day')

        key = t.get_key(day)
        if key not in self.nodes:
            node = day
            if t != Day:
                node = t(day)
            self.nodes[key] = node

        node = self.nodes[key]
        if not isinstance(node, Day):
            node.days.append(day)

    def add(self, date):
        """
         Add a date to the :class:`~python_calendar.Calendar`

        :param date: additional date
        :type date: datetime
        """
        if not isinstance(date, datetime):
            raise Exception('`date` must be a instance of datetime')
        day = Day(date)
        self.__add(day, Year)
        self.__add(day, Week)
        self.__add(day, Month)
        self.__add(day, Day)

    @staticmethod
    def get(date_from, date_to):
        """
        Create a :class:`~python_calendar.Calendar` based on 2 :class:`~datetime`

        :param date_from: The first date to analyze
        :type date_from: datetime

        :param date_to: The last date to analyze
        :type date_to: datetime

        :returns: Calendar
        """
        if not isinstance(date_from, datetime):
            raise Exception('`date_from` must be a instance of datetime')
        if not isinstance(date_to, datetime):
            raise Exception('`date_to` must be a instance of datetime')

        d = date_to - date_from

        calendar = Calendar()
        for i in range(0, d.days):
            t = date_from + relativedelta(days=+i)
            calendar.add(t)
        return calendar
