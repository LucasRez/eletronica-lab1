arquivoNome = ["bc548_values","tip31_values"]
vcc = 10
Rc = 298.8
Rb = 9890
for nome in arquivoNome:
  arq = nome+".txt"
  arquivo = open(str(arq))
  print(arq)
  for linha in arquivo:
    termos = linha.split(" |")
    Vbb = float(termos[2])
    Vbe = float(termos[3])
    Vce = float(termos[1])
    Ib = (Vbb-Vbe)/Rb
    Ic = (vcc-Vce)/Rc
    print("Ib = " + Ib.__str__())
    print("Ic = " + Ic.__str__())
    print("===========================================")
