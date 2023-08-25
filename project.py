import argparse
import sys

from classes.news_interface import NewsInterface
from classes.summary_interface import SummaryInterface

def main():
    settings = process_cli_args()    

    options = [
        {"txt": "US headlines", "func": display_articles_by_country},
        {"txt": "Articles by country", "func": display_countries},
        {"txt": "Articles by source", "func": display_sources},
        {"txt": "Search for articles", "func": display_articles_by_search},
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
            print() # Print a newline
            option = options[choice - 1]

            # Assign empty list for arguments if no arguments present.
            # Use *args to unpack arguments to be used in function call.
            args = option["args"] if ("args" in option) else []
            option["func"](*args)
        
        else:
            print("Invalid entry. Try again.\n")


def display_articles(articles):
    options = []

    for article in articles:
        options.append({"txt": article["title"], "func": summarize_article, "args": [article["url"]]})
    
    create_numeric_input_loop(options)


def summarize_article(url):
    txtList = SummaryInterface.get_extractive_summary(url)

    for txt in txtList:
        print(txt)
    
    input("Press Enter to continue...")
    print() # Print a newline


def display_articles_by_country(country="us"):
    articles = NewsInterface.get_articles_by_country(country)
    display_articles(articles)


def display_countries():
    countries = [
        ("au", "Australia"), ("br", "Brazil"), ("ca", "Canada"), ("de", "Germany"),
        ("fr", "France"), ("gb", "Great Britain"), ("in", "India"), ("it", "Italy"),
        ("jp", "Japan"), ("mx", "Mexico"),
    ]

    options = []

    for code, txt in countries:
        options.append({"txt": txt, "func": display_articles_by_country, "args": [code]})

    create_numeric_input_loop(options)


def display_articles_by_source(source="abc-news"):
    articles = NewsInterface.get_articles_by_source(source)
    display_articles(articles)


def display_sources():
    sources = [
        ("abc-news", "ABC News"), ("ars-technica", "Ars Technica"),
        ("associated-press", "Associated Press"), ("bloomberg", "Bloomberg"),
        ("cbc-news", "CBC News"), ("cnn", "CNN"), ("espn", "ESPN"),
        ("fortune", "Fortune"), ("national-geographic", "National Geographic"),
        ("politico", "Politico"),
    ]

    options = []

    for code, txt in sources:
        options.append({"txt": txt, "func": display_articles_by_source, "args": [code]})

    create_numeric_input_loop(options)


def get_search_input():
    while (True):
        try:
            str = input("Enter a search term up to 30 characters: ")
            str = str.strip().lower()

            if len(str) == 0 or len(str) > 30: raise ValueError
            break
        except:        
            print("Invalid entry. Try again.")
    
    return str


def display_articles_by_search():
    search_str = get_search_input()
    articles = NewsInterface.get_articles_by_search(search_str)
    display_articles(articles)


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