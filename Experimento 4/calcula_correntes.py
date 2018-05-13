arquivoNome = ["tabela5V","tabela0V"]
vcc = [5,0]
i=0
for nome in arquivoNome:
  arq = nome+".txt"
  arquivo = open(str(arq))
  for linha in arquivo:
    termos = linha.split(" |")
    print((float(termos[0])-float(termos[1]))/9890)
    print((vcc[i]-float(termos[2]))/99.62)
  i+=1
