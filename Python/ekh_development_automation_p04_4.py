python
     # Python script to automatically fetch and integrate threat intelligence data from an API
     import requests

     def fetch_threat_intel(api_url):
         response = requests.get(api_url)
         if response.status_code == 200:
             data = response.json()
             integrate_with_security_tools(data)
         else:
             print("Failed to fetch threat intelligence data")

     api_url = "https://threatintel.example.com/api/v1/indicators"
     fetch_threat_intel(api_url)