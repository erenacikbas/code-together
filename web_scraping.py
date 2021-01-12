# importing beautifulsoup
from bs4 import BeautifulSoup
import ssl
import urllib.request
# python 2.6
file = open("python2.6.txt", "a")
# python 3
file2 = open("python3.txt", "a")


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
# file operations
file.writelines(Lines)
file.close()

# file2 operations
file2.write(soupforLink2.find(id="mw-content-text").get_text())
file2.close()

print("hello world")
