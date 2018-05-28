R1 = [197800, 98900, 99.9]
R2 = [202300, 98300, 99]

V_inv = [0.0017, 0.0008, 0]
V_ninv = [0.0017, 0.0008, 0]

print("=======================================")
print("Exp1")
for i in range(0,3):
  ib_pos = V_ninv[i]/R2[i]
  ib_neg = V_inv[i]/R1[i]
  ib = (ib_pos + ib_neg)/2
  print("ib_pos = " + str(round(ib_pos * (10 **9), 2)) + " nA")
  print("ib_neg = " + str(round(ib_neg * (10 **9), 2)) + " nA")
  print("ib = " + str(round(ib * (10 **9), 2)) + " nA")

print("=======================================")
print("Exp2")
V_O = [-0.47, -0.95, -0.0051]
R = [98900, 202300, 978]
for i in range(0,3):
  V_os = V_O[i]*(99.9/(99.9 + R[i]))
  print("V_os = " + str(round(V_os*1000, 2)) + "mV")

print("=======================================")
print("Exp5")
dx = [4.28, 5.68]
dy = [2.34, 2.38]
SR_med = 0
for i in range(0,2):
  SR = dy[i]/dx[i]
  SR_med += SR
  print("SR = " + str(round(SR, 2)) + "V/us")
print("SR_med = " + str(round(SR_med/2, 2)) + "V/us")
