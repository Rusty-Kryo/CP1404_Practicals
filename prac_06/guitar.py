"""



"""

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self, current_year = 2022):
        return current_year - self.year

    def is_vintage(self, vintage=50):
        return self.get_age() >= vintage

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"
