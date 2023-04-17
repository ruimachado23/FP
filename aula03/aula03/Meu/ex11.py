sec = int(input ("Segundos: "))

def sec2hms(sec):

        h = sec // 3600
        m = sec // 60 - h*60
        s = sec % 3600 - m*60
        return h,m,s

h,m,s = sec2hms(sec)

print (h, "horas", m, "minutos", s, "segundos")
