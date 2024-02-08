from datetime import datetime
from dateutil.relativedelta import relativedelta


class Day:
    key = '%Y-%m-%d'

    def __init__(self, date):
        self.date = date

    @staticmethod
    def get_key(date):
        return date.strftime('%Y-%m-%d')


class Week:
    key = '%s-W%s'

    def __init__(self, date):
        self.number = date.isocalendar()[1]
        self.year = date.isocalendar()[0]

    @staticmethod
    def get_key(date):
        return Week.key % (
            date.isocalendar()[0],
            str(date.isocalendar()[1]).zfill(2)
        )


class Month:
    key = '%s-%s'

    def __init__(self, date):
        self.number = date.month
        self.year = date.year

    @staticmethod
    def get_key(date):
        return Month.key % (
            date.year,
            str(date.month).zfill(2)
        )


class Calendar:
    def __init__(self):
        self.days = {}
        self.weeks = {}
        self.months = {}
        self.years = []

    def __add_year(self, date):
        if date.year not in self.years:
            self.years.append(date.year)

    def __add_week(self, date):
        key = Week.get_key(date)

        if key not in self.weeks.keys():
            self.weeks[key] = Week(date)

    def __add_month(self, date):
        key = Month.get_key(date)

        if key not in self.months.keys():
            self.months[key] = Month(date)

    def __add_day(self, date):
        key = Day.get_key(date)

        if key not in self.days.keys():
            self.days[key] = Day(date)

    def add(self, date):
        if not isinstance(date, datetime):
            raise Exception('`date` must be a instance of datetime')

        self.__add_year(date)
        self.__add_week(date)
        self.__add_month(date)
        self.__add_day(date)

    @staticmethod
    def get(date_from, date_to):
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
