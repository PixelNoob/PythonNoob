#Tasador de Inmuebles
print "Bienvenido al Tasador de Inmuebles, le ayudaremos a conocer el valor de su propiedad..."
m2 = input ("Cantidad de metros cuadrados de su propiedad")
zona = input ("introduzca la zona: alto, bajo, oeste, centro")
if zona == "alto":
   print "el valor estimado de su propiedad es", float(m2) * 30000
if zona == "bajo":
   print"el valor estimado de su propiedad es", float(m2) * 22000
if zona == "oeste":
   print "el valor estimado de su propiedad es", float(m2) * 20000
if zona == "centro":
    print "el valor estimado de su propiedad es de ARS", float(m2) * 27000
