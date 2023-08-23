import argparse
import sys

def main():
    settings = process_cli_args()


def process_cli_args():
    settings = {}

    parser = argparse.ArgumentParser(
        description="Presents news articles that users can choose to summarize"
    )

    parser.add_argument("-s", action="store_true", help="Enable text to speech")
    args = parser.parse_args()

    settings["tts"] = args.s
    return settings


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()