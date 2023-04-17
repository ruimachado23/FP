d_ida = 4000
v_andar = float (600 / 1000)

t_volta = float (d_ida / v_andar)

h = int ((t_volta // 3600) + 6) 
m = int (((t_volta % 3600) // 60) + 52)

if m >= 60:
    h += 1

print ("{}:{}".format(h,s))

