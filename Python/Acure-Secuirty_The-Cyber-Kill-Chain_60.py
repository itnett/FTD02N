python
import requests

UID = 'your-uid'
SECRET = 'your-secret'
url = 'https://censys.io/api/v1/search/certificates'
params = {
    'query': 'example.com',
    'page': 1,
    'fields': ['parsed.subject_dn', 'parsed.extensions.subject_alt_name.dns_names']
}

response = requests.get(url, auth=(UID, SECRET), json=params)
print(response.json())