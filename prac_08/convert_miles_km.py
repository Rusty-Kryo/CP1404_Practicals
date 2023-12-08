"""
estimate: 1hr 40mins
acutual: 2hr 7mins
GitHub:https://github.com/Rusty-Kryo/CP1404_Practicals
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

# miles to km conversion constant, how many km per 1 Mile
Km_Per_Miles = 1.61


class MtoKmConverter(App):
    output_km = StringProperty()

    # An app that generates a pop-up window where the user can
    # type a distance in miles and convert it to km. The user can also
    # use the increment button, up and down, to increase and decrease the
    # distance by 1.

    def build(self):
        # Build the Kivy app from the kv file
        Window.size = (400, 200)
        self.title = "Convert M to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_km = 'Enter a Distance in miles and Click convert'
        return self.root

    def handle_calculate(self):
        # Handle conversion calculation and stores it in the string property
        value = self.check_input_miles()
        answer = value * Km_Per_Miles
        self.output_km = f"{answer:.2f}"

    def handle_increment(self, increment):
        # Handles the increment, positive or negative, depending on the value of increment
        result = self.check_input_miles() + increment
        self.root.ids.input_miles.text = str(result)
        self.handle_calculate()

    def check_input_miles(self):
        # Checks whether the user input is a numeric character (like; 1, 2, 3, etc.)
        # If it is a numeric character it stores the user input as a float
        # If it is not a numeric character it returns zero
        # value = float(self.root.ids.input_miles.text)
        # if not value:
        #     return 0
        # else:
        #     return value

        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


if __name__ == '__main__':
    MtoKmConverter().run()
