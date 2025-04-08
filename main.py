# A basic RSS Feed Reader in Terminal using the feedparser module

import feedparser
import requests

# function that get url input
def get_url():
    while 1:
        url = input("Please enter URL: ")
        if (valid_url(url)):
            return url
        else:
            print("Please enter a valid URL!")

# Checks if the URL is valid
def valid_url(url):
    response = requests.head(url, timeout=5)

    # for any 4xx error (404 ...) we will return false
    if response.status_code < 400:
        return True
    else:
        return False
    

# function that parses and return list of channel entries
def access_url(url):
    d = feedparser.parse(url)
    
    if (d.bozo):
        while 1:
            print("Invalid/Poor XML formatting")
            user_conf = input("Do you wish to proceed? (Y/n) ").lower()

            if (user_conf == 'y'):
                return d.entries
            elif (user_conf == 'n'):
                return []
            else:
                print("Invalid! Please enter y or n")
    
    return d.entries

# function that prints the entries required information
def print_entries(entry_list):
    for entry in entry_list:
        print("+--------------------------------------------------+")
        print(f"Entry Title: {entry.title}")
        print(f"Entry Description: {entry.description}")
        print(f"Entry Link: {entry.link}")

# The Main Function
def main():
    no_urls = int(input("Enter the number of URLs: "))
    # list that contains the links 
    user_urls = []
    # list that contains the list of entries
    entries_list = []

    # loop to get the urls and store them in user_urls
    for i in range(0, no_urls):
        url = get_url()
        user_urls.append(url)

    # loop to get the entries list and store them in entries_list
    for url in user_urls:
        entries_list.append(access_url(url))

    # loop to print the entries in each list stored in entries_list
    for entries in entries_list:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print_entries(entries)


if __name__ == "__main__":
    main()