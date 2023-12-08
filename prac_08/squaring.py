"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015

estimate: 1 hr
actual: 45 mins
edited in: 10-11-2023
edited by: Rusty John Balatan
GitHub:https://github.com/Rusty-Kryo/CP1404_Practicals
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        # Builds the model of the window using kivy
        Window.size = (400, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        # Handles the calculation of the square and stores the result into
        # output_result.text with in the kivy file.
        try:
            result = float(value) ** 2
            self.root.ids.output_result.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()
