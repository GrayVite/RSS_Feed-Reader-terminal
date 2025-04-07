# RSS Feed Reader in Terminal

This is a simple terminal-based RSS Feed Reader built using Python and the `feedparser` module. It allows users to input an RSS feed URL, fetch the feed, and display the titles, descriptions, and links of the feed entries in a user-friendly format.

## Features

- Accepts an RSS feed URL from the user.
- Parses the RSS feed using the `feedparser` module.
- Displays key information about each feed entry:
  - Title
  - Description
  - Link

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- `feedparser` library (installable via pip)

## Installation

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Install the required library by running:
   `pip install feedparser`

## Usage

1. Run the script by executing:
   `python main.py`
2. Enter a valid RSS feed URL when prompted (e.g., `https://rss.nytimes.com/services/xml/rss/nyt/World.xml`).

3. The program will parse the RSS feed and display information about each entry in the terminal.

## Example Output

Please enter URL: https://rss.nytimes.com/services/xml/rss/nyt/World.xml
+--------------------------------------------------+
Entry Title: Example News Title 1
Entry Description: This is a brief description of the first news article.
Entry Link: https://example.com/news/1
+--------------------------------------------------+
Entry Title: Example News Title 2
Entry Description: This is a brief description of the second news article.
Entry Link: https://example.com/news/2

## Limitations

- The script assumes that the entered URL is a valid RSS feed URL. No additional validation is performed.
- The displayed descriptions may be truncated depending on how they are provided in the RSS feed.
