"""
estimate: 1 hr 30 mins
actual:

Description:
Program for the wiki API task

"""

import wikipedia

MENU = ("\nEnter page title or search phrase\n"
        ">>>")


def main():
    """
    Prompt the user to choose either search for a page title
    or search by phrase
    """
    user_input = input(MENU)

    while user_input != " ":
        try:
            page = wikipedia.page(user_input, auto_suggest=False)
            page_summary = page.summary
            print(f"Page Title:{page.title}")
            print(f"Summary:\n{page_summary}")
            print(f"URL:{page.url}")
            # user_input = input(MENU)
        except wikipedia.exceptions.DisambiguationError as errors:
            options = errors.options[:5]
            print(options)
        except KeyError:
            break

        user_input = input(MENU)


main()
