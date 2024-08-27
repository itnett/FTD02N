python
from zeep import Client

# Koble til en SOAP-tjeneste
wsdl = 'http://www.dneonline.com/calculator.asmx?WSDL'
client = Client(wsdl=wsdl)

# Utføre en operasjon (f.eks. addisjon)
result = client.service.Add(intA=10, intB=20)
print("Resultat av addisjon:", result)