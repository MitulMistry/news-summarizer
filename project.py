import argparse
import sys

def main():
    settings = process_cli_args()

    choice = 1

    while (True):
        if choice == 0:
            print("Exiting program...")
            break

        elif choice == 1:
            options = [
                "US headlines",
                "Articles by country",
                "Articles by source",
                "Search for articles",
            ]

            print_options(options)

            choice = get_choice()
        
        else:
            print("Invalid entry. Try again.\n")
            choice = 1


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
        print(f"{i + 1}. {options[i]}")

    print("Type 0 to exit")


if __name__ == "__main__":
    main()