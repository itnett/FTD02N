python
# Installer et bibliotek (f.eks. requests for HTTP-forespørsler)
# pip install requests

import requests

response = requests.get('https://api.github.com')
print(response.status_code)