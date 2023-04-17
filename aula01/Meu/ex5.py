a = float (input ("Cateto A (cm) = "))
b = float (input ("Cateto B (cm)= "))

import math
c = float (math.sqrt (a*a + b*b))
ang = math.acos (b/c)

print ("Hipotenusa = " + str(c) + " cm ; Ângulo =  " + str(ang) + " graus")