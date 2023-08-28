# News Summarizer

### A command line application written in Python for accessing news articles and summarizing them.

## Application Info

#### What is this application?
News Summarizer is a command line tool used to access recent news articles and employ an external service to summarize them. It leverages [News API][news-api] to find news articles based on a variety of factors including country, news source, or custom text search. The application then uses the [TLDRThis][tldr-this] API to use the URL of the user selected article and create an AI generated summary. Text to speech can optionally be enabled (using a command line argument) to read the summary aloud.

#### What does each file do?
[`project.py`](/project.py) - The main application file that contains all the CLI logic.

[`classes/news_interface.py`](/classes/news_interface.py) - A class used to make API calls to [News API][news-api].

[`classes/summary_interface.py`](/classes/summary_interface.py) - A class used to make API calls to [TLDRThis][tldr-this].

[`test_project.py`](/test_project.py) - Tests for functions in `project.py`.

[`requirements.txt`](/requirements.txt) - A list of dependencies used to build the application.

#### Design decisions
This is a command line application that leverages a nested, reusable loop structure to continue to take user input and reroute to desired functions, and easily return back to previous menus. Loops are maintained until valid input is provided, and then flow of control moves to a new loop representing the choice the user made.

Since many of the loops use the same structure, the basic input loop was extracted into a reusable function with options being provided in the format of a list of dictionaries. Each option is a dictionary in order to maintain associated text to be displayed, the function to be invoked (if the option is selected), and an optional list of arguments to be sent to the function.

My goal was to integrate two different APIs into a unifed CLI experience. It made sense to me to separate the API interfaces into separate classes and encapsulate the external requests into associated methods. This allows easy access to external API data just by invoking class methods.

## Video Demo
You can view a video demo of this application [here]().

## Commands
`python project.py` - Run the application.

`python project.py -s` - Run the application with text to speech enabled.

## Install Instructions
Pip is used for dependencies. To install the application locally, follow these instructions:

1. Install [Python](https://www.python.org/). Pip comes packaged with it.
2. Run `python -m pip install -r requirements.txt` in the command line while in the project directory. It will install dependencies from the [requirements.txt file](../main/requirements.txt).
3. Get API keys for both the [News API](https://newsapi.org/register) and [TLDRThis](https://rapidapi.com/tldrthishq-tldrthishq-default/api/tldrthis/). Once you have keys, put them in a `.env` file in the project's root directory. Structure them like this:
```
NEWS_API_KEY=...
TLDR_API_KEY=...
```
4. Run `python project.py` to start the application.

## Tests
Tests are written with [pytest](https://docs.pytest.org/) in the [`test_project.py`](/test_project.py) file. They can be run with the command: `python -m pytest test_project.py`

## API Info
This application is powered by [News API][news-api] and [TLDRThis][tldr-this].

## More Info
This application serves as the final project for Harvard's CS50 Python Programming course:
https://cs50.harvard.edu/python/2022/project/

## License
This project is open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

[news-api]: https://newsapi.org/
[tldr-this]: https://tldrthis.com/