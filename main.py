# A basic RSS Feed Reader in Terminal using the feedparser module

import feedparser

# function that get url input
def get_url():
    url = input("Please enter URL: ")

    return url

# function that parses and return list of channel entries
def access_url(url):
    d = feedparser.parse(url)

    feed_entries = d.entries

    return feed_entries

# function that prints the entries required information
def print_entries(entry_list):
    for entry in entry_list:
        print("+--------------------------------------------------+")
        print(f"Entry Title: {entry.title}")
        print(f"Entry Description: {entry.description}")
        print(f"Entry Link: {entry.link}")

# The Main Function
def main():
    user_url = get_url()
    entries = access_url(user_url)

    print_entries(entries)

if __name__ == "__main__":
    main()