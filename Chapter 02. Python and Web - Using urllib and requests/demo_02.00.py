import urllib.request as req

link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
response = req.urlopen(link)

print(f"💻 {type(response)}")
print(f"💻 {response.read()}")