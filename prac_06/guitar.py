"""
CP1404 prac_06 - Guitar class
"""
# constants -> need current year for get_age(), and what is considered vintage (50 years) for is_vintage()
# for sustainability look into date/time module -> have we learnt this/is this needed?
CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    """This class stores the details of a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string with details about a guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Return sorted guitars by year release with less than"""
        return self.year < other.year

    def get_age(self):
        """Returns the current age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns True/False depending on if a guitar is vintage or not"""
        return VINTAGE_AGE <= self.get_age()
