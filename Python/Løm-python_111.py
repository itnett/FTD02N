python
totale_kostnader = 24000000
vareforbruk = 11000000
fakturerte_timer = 26000

selvkost_per_time = (totale_kostnader - vareforbruk) / fakturerte_timer
print(f"Selvkost per time: {selvkost_per_time:.2f} kr")