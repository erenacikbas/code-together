from collections import Counter

# stripped_python2.6.txt
file = open('stripped_python2.6.txt', 'r')
file_1=open('stripped_python3.txt', 'r')
stripped_text = file.read()
stripped_text_1 = file_1.read()

def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


def word_counter(stripped_text):
    wordsList = []
    for words in stripped_text.split(" "):
        wordsList.append(words)
    counted_dictionary = Counter(wordsList).most_common(20)
    for i in counted_dictionary:
        print(i)



word_counter(stripped_text)
word_counter(stripped_text_1)

