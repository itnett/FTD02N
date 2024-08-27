python
  def beregn_npv(kontantstrømmer, diskonteringsrate):
      npv = sum([cf / (1 + diskonteringsrate)**i for i, cf in enumerate(kontantstrømmer)])
      return npv

  kontantstrømmer = [-100000, 30000, 40000, 50000, 60000]
  diskonteringsrate = 0.1
  print(f"NPV: {beregn_npv(kontantstrømmer, diskonteringsrate):.2f}")