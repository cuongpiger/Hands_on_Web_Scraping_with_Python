# 1. Technical requirements
# 2. Accessing the web with Python
## 2.1. Setting things up
## 2.2. Loading URLs
* Code dưới đây dùng để in ra web [https://en.wikipedia.org/wiki/List_of_most_popular_websites](https://en.wikipedia.org/wiki/List_of_most_popular_websites) sau khi crawl về.

###### [demo_02.00.py](demo_02.00.py)
```python
import urllib.request as req

link = "https://en.wikipedia.org/wiki/List_of_most_popular_websites"
response = req.urlopen(link)

print(f"💻 {type(response)}")
print(f"💻 {response.read()}")
```
![](images/02_00.png)

# 3. URL handling and operations with urllib and requests
## 3.1. `urllib`
