"""
estimate: 1 hr
actual: 45 mins

GitHub:https://github.com/Rusty-Kryo/CP1404_Practicals
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    # handles the event when greet button is pressed
    def handle_greet(self):
        # print("test") for debugging
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    # handles the event when clear button is pressed
    def handle_clear(self):
        # sets the input_name into blank ("")
        self.root.ids.input_name.text = ""
        # sets the output_label to its original state
        self.root.ids.output_label.text = "Enter Your Name"


BoxLayoutDemo().run()
