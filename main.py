# importing beautifulsoup
from bs4 import BeautifulSoup
import ssl
import urllib.request
# Counter for word counting
from collections import Counter


# Unwanted Word Lists
unwanted_words = [">>>", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against",
                  "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "==", "+", "=", "-"]


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
    stripped_book_name = "Stripped_" + bookName
    stripped_book = open(stripped_book_name, "a")
    text = book.read()
    stripped_text = " ".join(text.split())
    stripped_book.write(stripped_text.casefold())
    stripped_book.close()
    book.close()
    print(stripped_book_name)
    return stripped_book_name

    # file operations for book1


# 3. Word Counting

def word_counting(bookName, stripped_book):
    stripped_book_text = open(stripped_book, "r+").read()

    def pretty(d, indent=0):
        for key, value in d.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                pretty(value, indent+1)
            else:
                print('\t' * (indent+1) + str(value))

    # def word_counter(stripped_text):
    #     text = ""
    #     wordsList = []
    #     for words in stripped_book_text.split(" "):
    #         wordsList.append(words)
    #     counted_dictionary = Counter(wordsList).most_common(20)
    #     for i in counted_dictionary:
    #         text += str(i) + "\n"
    #     print(text)
    #     return text

    # print(word_counter(stripped_book_text))

    def word_count(str):
        words = str.split()
        counts = dict()
        sorted_text = ""
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        # Sorting values
        sorted_dict = {}
        sorted_keys = sorted(counts, key=counts.get, reverse=True)
        for w in sorted_keys:
            sorted_dict[w] = counts[w]

        # for x, y in sorted_dict.items():
        #     sorted_text += str(x) + ":" + str(y) + "\n"
        # return sorted_text

        # Removing Unwanted Items
        for uw_word in unwanted_words:
            if(uw_word in sorted_dict):
                del sorted_dict[uw_word]
        sorted_dic_items = sorted_dict.items()
        first_20_words = list(sorted_dic_items)[:20]
        print(first_20_words)

        # for word, occurence in sorted_dict.items():
        #     print(str(word) + ": " + str(occurence) + "\n")

    result = open(bookName + "_result.txt", "a")
    #result_text = word_counter(stripped_book_text)
    result_text = word_count(stripped_book_text)
    #result.write(result_text)
    result.close()

# 4. Test


def test():
    #links = input_grabber()
    links = input_grabber()
    for link in links:
        book = web_scraping(link)
        stripped_book = stripping(book)
        word_counting(book, stripped_book)


test()
