v1 = float (input ("Velocidade de ida (km/h): "))
v2 = float (input ("Velocidade de regresso (km/h): "))

v3 = float ((2*v1*v2) / (v2+v1))

print ("Velocidade média: " + str(v3) + " km/h")