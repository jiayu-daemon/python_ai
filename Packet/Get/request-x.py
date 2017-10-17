import urllib.request
req = urllib.request.Request('http://python.org/')
response = urllib.request.urlopen(req)
the_page = response.read()