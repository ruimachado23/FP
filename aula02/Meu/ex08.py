print("Kryptonite phase classifier")

t = float (input("Temperature (K)? "))
p = float (input("Pressure (kPa)? "))

if p >= ((1/8) * t) and t <= 400:
    phase = "SOLID"

elif t > 400 and p > 50:
    phase = "LIQUID"

else:
    phase = "GAS"

print("At {:.1f} K and {:.3f} kPa, Kryptonite is in the {} phase.".format(t, p, phase))