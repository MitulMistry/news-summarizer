import argparse
import sys

from classes.news_interface import NewsInterface 

def main():
    settings = process_cli_args()    

    options = [
        {"txt": "US headlines", "func": display_articles_by_country},
        {"txt": "Articles by country", "func": display_countries},
        {"txt": "Articles by source", "func": display_sources},
        {"txt": "Search for articles", "func": get_search_input},
    ]

    create_numeric_input_loop(options)


def create_numeric_input_loop(options):
    while (True):
        print_options(options)
        choice = get_choice()

        if choice == None:
            break
        
        elif choice == 0:
            sys.exit("Exiting program...")

        elif 0 < choice <= len(options):
            option = options[choice - 1]

            # Assign empty list for arguments if no arguments present.
            # Use *args to unpack arguments to be used in function call.
            args = option["args"] if ("args" in option) else []
            option["func"](*args)
        
        else:
            print("Invalid entry. Try again.\n")


def display_articles(articles):
    print(articles)


def summarize_article(url):
    ...


def display_articles_by_country(country="us"):
    articles = NewsInterface.get_articles_by_country(country)
    display_articles(articles)


def display_countries():
    countries = [
        "au,Australia", "br,Brazil", "ca,Canada", "de,Germany",
        "fr,France", "gb,Great Britain", "in,India", "it,Italy",
        "jp,Japan", "mx,Mexico"
    ]

    options = {}

    for country in countries:
        code, txt = country.split(",")
        options.append({"txt": txt, "func": display_articles_by_country, "args": [code]})

    create_numeric_input_loop(options)    


def display_sources():
    ...


def get_search_input():
    ...


def process_cli_args():
    settings = {}

    parser = argparse.ArgumentParser(
        description="Presents news articles that users can choose to summarize"
    )

    parser.add_argument("-s", action="store_true", help="Enable text to speech")
    args = parser.parse_args()

    settings["tts"] = args.s
    return settings


def get_choice(description="Choice: "):
    str = input(description).strip()

    try:
        return(int(str))
    except ValueError:
        return None


def print_options(options):
    print("Pick an option (number):")

    for i in range(len(options)):
        text = options[i]["txt"] if type(options[i]) == dict else options[i]
        print(f"{i + 1}. {text}")

    print("Type 0 to exit. Type nothing to go to previous menu.")


if __name__ == "__main__":
    main()