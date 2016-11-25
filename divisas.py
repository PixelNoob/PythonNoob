eur = input('precio BTC/EUR:')
eur= float(eur)
bsf = input("precio BTC/BSF:")
bsf = float(bsf)
cambiar = input("monto a cambiar:")
cambiar = float(cambiar)
fee = float(0.85)
pagar = (cambiar*fee)/eur * bsf
print "pagar a cliente", pagar
cambio = float(pagar)/cambiar
print "tasa de cambio", cambio
profit = cambiar*0.15
print "profit", profit
