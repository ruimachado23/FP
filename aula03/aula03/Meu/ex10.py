h = int(input ("Horas: "))
m = int(input ("Minutos: "))
s = int(input ("Segundos: "))


def hms2secs(h, m, s):

    sec = h*3600 + m*60 + s 

    return  sec
    
print ( hms2secs(h,m,s), "segundos") 