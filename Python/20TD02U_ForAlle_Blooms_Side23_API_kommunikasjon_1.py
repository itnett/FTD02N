python
from zeep import Client

wsdl = 'http://www.example.com/service?wsdl'
client = Client(wsdl=wsdl)

# Kall en SOAP-tjeneste
response = client.service.MethodName(param1='value1', param2='value2')
print(response)