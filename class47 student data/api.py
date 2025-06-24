import requests
import json
myapi = "8bb8630c49c646fcbdd633217c2e3361"
query = input("Enter some news topic you want to know: ")
start = input("What do you want start date to be? (YYYY-mm-Dd)")
end = input("What do you want end date to be? ")
url = f"https://newsapi.org/v2/everything?q={query}&from={start}&to={end}&pageSize=10&sortBy=publishedAt&apiKey={myapi}"
req = requests.get(url)
news = json.loads(req.text)
#print(news)
for article in news["articles"]:
    print(article["title"])
    print(article["author"])
    print(article["description"])
    print(article["url"]) 
    print("-------")