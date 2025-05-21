def main():

   
  dIN = {'César Hilal': 175, 'Aldo Carvalho': 180, 'Maria Eleonora': 165, 'Pedro Cunha': 190}
  dOUT = {}

  print ("ENTRADA", dIN)

  for k in dIN.keys():
    if dIN[k] > 170:
      dOUT[k] = dIN[k]

  print("SAÍDA", dOUT)

main()
