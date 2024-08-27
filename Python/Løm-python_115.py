python
totale_kostnader = 24000000  # Totale kostnader i kr
vareforbruk = 11000000  # Vareforbruk i kr
fakturerte_timer = 26000  # Antall fakturerte timer

selvkost_per_time = (totale_kostnader - vareforbruk) / fakturerte_timer
print(f"Selvkost per time: {selvkost_per_time:.2f} kr")