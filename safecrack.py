import urllib.request

num1 = 0
num2 = 0
num3 = 0
num4 = 0

while True:
    url= "http://cgi.soic.indiana.edu/~dpierz/secret_vault.cgi?
	groupname=Group+1&num1=" + str(num1) + "&num2=" + str(num2) + 	"&num3=" + str(num3) + "&num4=" + str(num4)
    print(url)

    try:
       web_page = urllib.request.urlopen(url)
        lines = web_page.read().decode(errors="replace")
        web_page.close()
    except:
        print("Error opening:", url)
        web_page = ""
 if "Wrong" not in lines:
        break

    if num4 != 9:
        num4 += 1
    else:
        num4 = 0
        if num3 != 9:
            num3 += 1
        else:
            num3 = 0
            if num2 != 9:
                num2 += 1
            else:
                num2 = 0
                num1 += 1

print(lines)
