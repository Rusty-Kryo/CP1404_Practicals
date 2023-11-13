"""
estimate: 1hr 40mins
actual: 1hr 50mins
GitHub:https://github.com/Rusty-Kryo/CP1404_Practicals
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

NEW_COLOUR = (0, 1, 0, 1)
OLD_COLOUR = (1, 0, 0, 1)


class DynamicLabel(App):
    # Main program for the dynamic label task
    message = StringProperty()

    def __init__(self, **kwargs):
        # Construct main app
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = ["Bob", "Fred", "Link"]

    def build(self):
        # Build the Kivy GUI.
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.message = "Names are:"
        self.handle_add_label()
        return self.root

    def handle_add_label(self):
        # Handles the addition of new labels
        for name in self.names:
            # create a label for each data entry
            label = Label(text=name)
            # add the label to the "entries_box" layout widget
            self.root.ids.main.add_widget(label)


DynamicLabel().run()
