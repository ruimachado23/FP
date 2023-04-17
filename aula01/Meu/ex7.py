a = int (input ("Número de andares = "))
m = int (input ("Número de moradores por piso = "))

dist_em_metros = float (365 * (3 * a * m * 4)) 

dist_em_km = float (dist_em_metros / 1000)

t = float (dist_em_metros / 3600)

print ("O elevador percorre " + str(dist_em_km) + "km por ano, durante " + str(t) + " horas.")







