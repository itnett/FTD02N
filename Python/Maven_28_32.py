python
   import json

   with open('transaksjoner.json', 'w') as f:
       json.dump(transaksjoner, f)

   with open('transaksjoner.json', 'r') as f:
       transaksjoner = json.load(f)