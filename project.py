import argparse
import sys
import pyttsx3

from classes.news_interface import NewsInterface
from classes.summary_interface import SummaryInterface

# Use settings as a global variable so all functions can access it
settings = {}
tts_engine = {}

def main():
    initialize_settings()

    # Define a list of dictionaries that represent the option to display
    # and their functions to invoke if selected.
    options = [
        {"txt": "US headlines", "func": display_articles_by_country},
        {"txt": "Articles by country", "func": display_countries},
        {"txt": "Articles by source", "func": display_sources},
        {"txt": "Search for articles", "func": display_articles_by_search},
    ]

    create_numeric_input_loop(options, True)
    

def initialize_settings():
    global settings, tts_engine
    settings = process_cli_args()
    
    # Configure text to speech engine
    if settings["tts"]:
        tts_engine = pyttsx3.init()

        # Set the voice for text to speech engine    
        voices = tts_engine.getProperty('voices')    
        tts_engine.setProperty('voice', voices[3].id)


def create_numeric_input_loop(options, start=False):
    while (True):
        print_options(options, start)
        choice = get_choice()
        print() # Print a newline

        # -1 means user pressed enter with no input: go to previous menu
        if choice == -1 and not start:
            break
        
        # 0 means exit the program
        elif choice == 0:
            sys.exit("Exiting program...")

        # Within range of options, so select that option
        elif 0 < choice <= len(options):
            option = options[choice - 1]

            # Assign empty list for arguments if no arguments present.
            # Use *args to unpack arguments to be used in function call.
            args = option["args"] if ("args" in option) else []
            option["func"](*args)
        
        # Input was out of range or not a number, so retry
        else:
            print("Invalid entry. Try again.")


def display_articles(articles):
    options = []

    # Create a list of dictionaries representing articles, the function to invoke
    # when selected (summarize_article), and the url to pass to the function.
    for article in articles:
        options.append({
            "txt": article["title"],
            "func": summarize_article,
            "args": [article["url"]]
        })
    
    create_numeric_input_loop(options)


def summarize_article(url):
    global settings, tts_engine
    
    # Make and API call using SummaryInterface to get the summary
    # of the article at the provided URL.
    print("Loading summary...\n")
    txtList = SummaryInterface.get_humanlike_summary(url)

    # The summary is provided as a list of strings.
    for txt in txtList:
        # If text to speech is enabled, add the text to the tts queue.
        if settings["tts"]: tts_engine.say(txt)
        print(txt)
    
    if settings["tts"]: tts_engine.runAndWait()
    
    input("Press Enter to continue...")
    print() # Print a newline


def display_articles_by_country(country="us"):
    # Make an API call using NewsInterface to get the articles to display.
    articles = NewsInterface.get_articles_by_country(country)
    display_articles(articles)


def display_countries():
    countries = [
        ("au", "Australia"), ("br", "Brazil"), ("ca", "Canada"), ("de", "Germany"),
        ("fr", "France"), ("gb", "Great Britain"), ("in", "India"), ("it", "Italy"),
        ("jp", "Japan"), ("mx", "Mexico"),
    ]

    options = []

    # Create a list of dictionaries representing countries, the function to invoke
    # when selected, and the country code to pass to the function (for the API call).
    for code, txt in countries:
        options.append({"txt": txt, "func": display_articles_by_country, "args": [code]})

    create_numeric_input_loop(options)


def display_articles_by_source(source="abc-news"):
    # Make an API call using NewsInterface to get the articles to display.
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

    # Create a list of dictionaries representing sources, the function to invoke
    # when selected, and the source code to pass to the function (for the API call).
    for code, txt in sources:
        options.append({"txt": txt, "func": display_articles_by_source, "args": [code]})

    create_numeric_input_loop(options)


def get_search_input():
    while (True):
        try:
            str = input("Enter a search term up to 30 characters: ")            
            str = str.strip().lower()
            
            # Only allow query strings up to 30 characters.
            if validate_search_input(str):
                break
            else:
                raise ValueError
        except:        
            print("Invalid entry. Try again.")
    
    return str


def validate_search_input(str):    
    return 0 < len(str) <= 30


def display_articles_by_search():
    search_str = get_search_input()
    articles = NewsInterface.get_articles_by_search(search_str)
    display_articles(articles)


def process_cli_args(argv=None):
    # Allow argv to be passed as an argument in order to facilitate testing
    settings = {}

    parser = argparse.ArgumentParser(
        description="Presents news articles that users can choose to summarize"
    )

    parser.add_argument("-s", action="store_true", help="Enable text to speech")
    args = parser.parse_args(argv)

    settings["tts"] = args.s
    return settings


def get_choice(description="Choice: "):
    str = input(description)
    return process_choice(str)


def process_choice(str):
    str = str.strip()
    
    # Return -1 if Enter was pressed with no input
    if (str == ""): return -1

    try:
        return(int(str))
    except ValueError:
        # Return infinity if invalid input so it can still be used in
        # numerical comparison (like <) while being out of range (invalid)
        return float("inf")


def print_options(options, start=False):
    print("Pick an option (number):")

    for i in range(len(options)):
        text = options[i]["txt"] if type(options[i]) == dict else options[i]
        print(f"{i + 1}. {text}")

    prev_str = " Type nothing to go to previous menu." if not start else ""
    print(f"Type 0 to exit.{prev_str}")


if __name__ == "__main__":
    main()