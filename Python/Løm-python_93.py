python
     class MarketingMix:
         def __init__(self, product, price, place, promotion):
             self.product = product
             self.price = price
             self.place = place
             self.promotion = promotion

     mix = MarketingMix('Smartphone', 999, 'Online Store', 'Social Media Ads')
     print(f"Product: {mix.product}, Price: {mix.price}, Place: {mix.place}, Promotion: {mix.promotion}")