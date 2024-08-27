python
     import requests

     def get_latest_tech_news():
         response = requests.get("https://api.technews.com/latest")
         if response.status_code == 200:
             news = response.json()
             for article in news:
                 print(article['title'])

     get_latest_tech_news()