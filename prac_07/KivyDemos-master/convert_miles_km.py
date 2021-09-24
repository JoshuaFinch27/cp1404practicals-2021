"""
CP1404 - prac_07
       - program to convert miles to kilometres with a GUI
"""

from kivy.app import App
from kivy.lang import Builder

ONE_MILE_EQUALS_NUMBER_KM = 1.60934


class MilesToKMConverter(App):
    """Kivy based app that converts miles to kilometres"""

    def build(self):
        """Construct the app"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def get_valid_input(self):
        """Trys to get a valid input if it fails gives a zero"""
        try:
            validated_input = float(self.root.ids.distance_miles_input.text)
            return validated_input
        except ValueError:
            return 0

    def handle_calculate(self):
        """Calculate the conversion of miles to kilometres"""
        value = self.get_valid_input()
        result = value * ONE_MILE_EQUALS_NUMBER_KM
        self.root.ids.distance_km_output.text = str(result)

    def handle_increment(self, increment):
        """Change the input number based on the increment"""
        value = self.get_valid_input() + increment
        self.root.ids.distance_miles_input.text = str(value)
        self.handle_calculate()


MilesToKMConverter().run()
