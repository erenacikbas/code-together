# Stripping documents
file = open("python2.6.txt", "r")
file2 = open("stripped_python2.6.txt", "a")

file_1= open("python3.txt", "r")
file_12=open("stripped_python3.txt", "a")

text = file.read()
text = file_1.read()
   
stripped_text = " ".join(text.split())
file2.write(stripped_text.casefold())
file2.close()
stripped_text = " ".join(text.split())
file_12.write(stripped_text.casefold())
file_12.close()