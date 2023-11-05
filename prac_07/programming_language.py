"""
estimated: 2 hrs
actual:2 hrs 15mins
GitHub Link: https://github.com/Rusty-Kryo/CP1404_Practicals

CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def is_pointer_arithmetic(self):
        """Checks whether the language has the ability to perform pointer arithmetic"""
        return self.pointer_arithmetic is True

    def __str__(self):
        """return a string that displays the details of the language, name, type, reflection, year and
        pointer arithmetic capability"""
        return (f"{self.name}, {self.typing} Typing, Reflection:{self.reflection}, First Appeared in:{self.year}, "
                f"Pointer Arithmetic:{self.pointer_arithmetic}")


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)

    languages = [ruby, python, visual_basic]
    for language in languages:
        print(language)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
