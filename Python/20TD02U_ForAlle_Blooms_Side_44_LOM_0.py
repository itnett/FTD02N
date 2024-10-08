python
  import pandas as pd
  
  # Last inn økonomiske data fra en CSV-fil
  df = pd.read_csv('regnskap.csv')
  
  # Beregn nettoresultat (inntekter - utgifter)
  df['Nettoresultat'] = df['Inntekter'] - df['Utgifter']
  
  # Lagre resultatet tilbake til regnearket
  df.to_csv('regnskap_oppdatert.csv', index=False)