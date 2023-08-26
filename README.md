# News Summarizer

### A command line application written in Python for accessing news articles and summarizing them.

## Application Info
-What is your application?


-What does each file do?


-Design decisions


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

## API Info
This application is powered by [News API](https://newsapi.org/) and [TLDRThis](https://tldrthis.com/).

## More Info
This application serves as the final project for Harvard's CS50 Python Programming course:
https://cs50.harvard.edu/python/2022/project/

## License
This project is open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).