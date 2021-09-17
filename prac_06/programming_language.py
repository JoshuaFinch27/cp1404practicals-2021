"""
CP1404 prac_06 - Programming language class with tests
"""


class ProgrammingLanguage:
    """Holds information on programming languages"""

    def __init__(self, name, typing, reflection, year):
        """Create the fields and set parameters"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True/False if programming language is dynamically typed or not"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string with info on Python Languages"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
