import urllib.request

page = ""

url= "http://cgi.soic.indiana.edu/~dpierz/form2.cgi?"
url += "name=Neil&shoesize=awesome&job=Astronaut&language=Ada"

print(url)

web_page = urllib.request.urlopen(url)
lines = web_page.read().decode(errors="replace")
web_page.close()

print(lines)
