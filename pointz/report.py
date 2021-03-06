from decimal import Decimal
from os import path

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

_templates_path = path.dirname(__file__)
_templates_path = path.join(_templates_path, 'templates')

_env = Environment(loader=FileSystemLoader(_templates_path))


def _to_str_with_2_digits(dec):
    return f'{dec:.2f}'


class MonthlySummary:
    def __init__(self, month, year, sales, pointz_sales):
        """Class representing a monthly summary dre data

        :param month: month of summary
        :param year: year of summary
        :param sales: total sales in cents
        :param pointz_sales: total sales with pointz in cents
        """
        self._sales = Decimal(sales) / 100
        self._pointz_sales = Decimal(pointz_sales) / 100
        self.year = year
        self.month = month

    @property
    def sales(self):
        return _to_str_with_2_digits(self._sales)

    @property
    def pointz_sales(self):
        return _to_str_with_2_digits(self._pointz_sales)

    @property
    def title(self):
        return f'{self.month}-{self.year}'


class Report:
    def __init__(self, title, monthly_summaries):
        self.monthly_summaries = monthly_summaries
        self.title = title


def render(template, report):
    return _env.get_template(template).render(report=report)
