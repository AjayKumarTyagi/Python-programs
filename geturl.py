import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('https://en.wikipedia.org/wiki/Avengers:_Endgame')
for line in fhand:
    print(line.decode().strip())
