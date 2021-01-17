# importing beautifulsoup
from bs4 import BeautifulSoup
import ssl
import urllib.request
# Counter for word counting
from collections import Counter


# Unwanted Word Lists
unwanted_words = [">>>", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against",
                  "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "==", "=", "-","1","2","3","4","5","6","7","8","9","0","*","(",")","_","'","-","=","[","]",",","[]","←","()","(print(","print()","#"]


# Taking Inputs
def input_grabber():
    links = []
    i = 0
    while i < 2:
        givenbook = str(input("Enter Book " + str((i+1)) + " Name: ")) 
        givenbook=givenbook.replace(" ", "_")
        givenbook=givenbook.replace("'","%27" ) 
        link=("https://en.wikibooks.org/wiki/"+(givenbook)+"/Print_version")
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

    file1 = open(book, "a")
    file1.truncate(0)

    context = ssl._create_unverified_context()

    link = urllib.request.urlopen(
        bookLink, context=context)

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
    stripped_book.truncate(0)
    text = book.read()
    
    # for a in unwanted_words:
    #     if(a in text):
    #         text=text.replace("a"," ")
    stripped_text = " ".join(text.split())
    stripped_book.write(stripped_text.casefold())
    stripped_book.close()
    book.close()
    print(stripped_book_name)
    return stripped_book_name

    # file operations for book1


# 3. Word Counting
def word_counting(bookName, stripped_book):
    sorted_dict = {}
    
    stripped_book_text = open(stripped_book, "r+").read()
    
    def pretty(d, indent=0):
        for key, value in d.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                pretty(value, indent+1)
            else:
                print('\t' * (indent+1) + str(value))

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

        sorted_keys = sorted(counts, key=counts.get, reverse=True)
        for w in sorted_keys:
            sorted_dict[w] = counts[w]

        # Removing Unwanted Items
        for uw_word in unwanted_words:
            if(uw_word in sorted_dict):
                  del sorted_dict[uw_word]
        sorted_dic_items = sorted_dict.items()
        first_20_words = list(sorted_dic_items)[:20]
        print(first_20_words)
        print("\n\n")

        # for word, occurence in sorted_dict.items():
        #     print(str(word) + ": " + str(occurence) + "\n")

    result = open(bookName + "_result.txt", "a")
    result.truncate(0)
    #result_text = word_counter(stripped_book_text)
    result_text = word_count(stripped_book_text)
    #result.write(result_text)
    result.close()
    return sorted_dict

# 5. Finding Intersection Points


     
def intersect_elements(sorted_dictionaries):
    dict__1 = sorted_dictionaries[0]
    dict__2 = sorted_dictionaries[1]

    ortak={}
     #intersects
    for eleman in dict__1.keys():
         if eleman in dict__2.keys():
            ortak[eleman]=(dict__1["eleman"])
            
    print("ortaklar: " + str(list(ortak.items())[:20]) + "\n\n")
    
    dict_1 = sorted_dictionaries[0]
    dict_2 = sorted_dictionaries[1]

    intersects = []
    # intersects
    for item in dict_1.keys():
        if item in dict_2.keys():
            intersects.append(item)

    # print("Intersects: ", intersects)
    # commons
    for dictionary in sorted_dictionaries:
        for intersect in intersects:
            if(intersect in dictionary):
                del dictionary[intersect]
    print("---------------------------------")
    print("Intersect Words")
    print("dict_1 : " + str(list(dict_1.items())[:20]) + "\n\n")
    print("dict_2 : " + str(list(dict_2.items())[:20]))


            




# 6. Test


def test():
    #links = input_grabber()
    links = input_grabber()
    sorted_dictionaries = []
    for link in links:
        book = web_scraping(link)
        
        stripped_book = stripping(book)
        sorted_dict = word_counting(book, stripped_book)
        sorted_dictionaries.append(sorted_dict)
    intersect_elements(sorted_dictionaries)
    


test()
