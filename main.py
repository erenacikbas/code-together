# 1. Web Scraping
# importing beautifulsoup
from bs4 import BeautifulSoup
import ssl
import urllib.request


def web_scraping():

    # python 2.6
    file1 = open("python2.6.txt", "a")
    file1.clear()
    # python 3
    file2 = open("python3.txt", "a")
    file2.clear()

    context = ssl._create_unverified_context()

    link1 = urllib.request.urlopen(
        "https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_2.6/Print_version", context=context)

    link2 = urllib.request.urlopen(
        "https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Print_version", context=context)

    # Link 1 Soup
    soupForLink1 = BeautifulSoup(link1, 'html.parser')

    # Link 2 Soup
    soupforLink2 = BeautifulSoup(link2, 'html.parser')

    # # Header Writer Subtitle
    # soup2 = BeautifulSoup(open('sample.html'), 'html.parser')
    # # Text
    # soup = BeautifulSoup(u, 'html.parser')

    Lines = [
        # Text
        soupForLink1.find(id='bodyContent').get_text()
    ]
    # file operations - 2.6
    file1.writelines(Lines)
    file1.close()

    # file2 operations - 3.0
    file2.write(soupforLink2.find(id="mw-content-text").get_text())
    file2.close()


# 2. Stripping

def stripping():
    pass


# 3. Word Counting

def word_counting():
    pass

# 4. Test

def test():
    web_scraping()
    stripping()
    word_counting()

test()

