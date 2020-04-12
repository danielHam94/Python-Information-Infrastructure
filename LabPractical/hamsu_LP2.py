#Sung Hoon Ham
#Group 2

import re, urllib.request, webbrowser

web_page = urllib.request.urlopen("http://cgi.soic.indiana.edu/~dpierz/news.html")
contents = web_page.read().decode(errors="replace")
web_page.close()

print("Searching: http://cgi.soic.indiana.edu/~dpierz/news.html\n")

article = re.findall('(?<=<span itemprop="headline">).+?(?=</span>)', contents, re.DOTALL)

for i in article:
    if ".edu" not in article:
        print("\t",i,"\n")

#Attempted to do the headline matching and bonus, but had trouble retrieving the article title containing the word
user_input = input("Please enter a word to search for: ")
user_article = re.findall('(?<=)user_input.+?(?=")', article, re.DOTALL)
url = re.findall('(?<=<h1><a itemprop="url" href=").+?(?=">)', contents, re.DOTALL)

for word in user_input:
    if word in user_article:
        print(article)
        
webbrowser.open_new_tab(url)

