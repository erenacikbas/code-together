# importing beautifulsoup
from bs4 import BeautifulSoup
import ssl
import urllib.request

# Taking Inputs


def input_grabber():
    links = []
    i = 0
    while i < 2:
        link = str(input("Enter Book " + str((i+1)) + " Link: "))
        links.append(dict({"Book " + str(i+1) + ".txt": link}))
        i += 1
    return links


# 1. Web Scraping

def web_scraping(link):
    book = ""
    bookLink = ""
    for key, value in link.items():
        book = key
        bookLink = value

    # python 2.6
    file1 = open(book, "a")
    file1.truncate(0)

    context = ssl._create_unverified_context()

    link = urllib.request.urlopen(
        bookLink, context=context)

    # Link 1 Soup
    soupForLink = BeautifulSoup(link, 'html.parser')

    Lines = [
        # Text
        soupForLink.find(id='bodyContent').get_text()
    ]
    file1.writelines(Lines)
    file1.close()
    return book


# 2. Stripping

def stripping(bookName):
    book = open(bookName, "r+")
    stripped_book = open("Stripped_" + bookName, "a")
    text = book.read()
    stripped_text = " ".join(text.split())
    stripped_book.write(stripped_text.casefold())
    stripped_book.close()
    book.close()

    # file operations for book1


# 3. Word Counting

def word_counting():
    pass

# 4. Test


def test():
    links = input_grabber()
    for link in links:
        book = web_scraping(link)
        stripping(book)
        # word_counting()


test()
