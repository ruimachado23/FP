sec = input ("Segundos: ")

h = int(sec) // 3600
m = (int(sec) % 3600) // 60
s = (int(sec) % 3600) % 60

# print(str (h) + "h : " + str (m) + "m : " + str (s) + "s")

print("{:02d}:{:02d}:{:02d}".format(h, m, s))