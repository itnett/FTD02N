python
   # Korrekt bruk av gjeldende siffer
   value1 = 12.345
   value2 = 0.00456
   value3 = 123.4

   # Antall gjeldende siffer
   sig_figs_value1 = len(str(value1).replace('.', '').replace('-', '').lstrip('0'))
   sig_figs_value2 = len(str(value2).replace('.', '').replace('-', '').lstrip('0'))
   sig_figs_value3 = len(str(value3).replace('.', '').replace('-', '').lstrip('0'))

   print(f"Verdi 1: {value1}, Gjeldende siffer: {sig_figs_value1}")
   print(f"Verdi 2: {value2}, Gjeldende siffer: {sig_figs_value2}")
   print(f"Verdi 3: {value3}, Gjeldende siffer: {sig_figs_value3}")