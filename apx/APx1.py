# isLeapYear(year) deve devolver True se year é um ano bissexto
# e False se é um ano comum.  Corrija-a.
# (See: https://en.wikipedia.org/wiki/Leap_year)

def isLeapYear(year):

   if year % 4 == 0 and year%100 != 0:
      return True

   elif year % 400 == 0 and year%100 == 0:
      return True

   else: 
      return False
            
# monthDays deve devolver o número de dias de um dado mês num dado ano.
# Por exemplo, monthDays(2004, 2) deve devolver 29.
# Corrija-a.

def monthDays(year, month):

    if isLeapYear(year) == True:
        MONTHDAYS = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    else:    
        MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    days = MONTHDAYS[month]

    return days

# nextDay deve devolver o dia a seguir a uma dada data.
# Por exemplo, nextDay(2017, 1, 31) deve devolver (2017, 2, 1)

def nextDay(year, month, day):
   
    day += 1

    if day > monthDays(year, month):
        month += 1
        day = 1
        
        if month > 12:
            year += 1
            month = 1
            

    return year, month, day

# Defina uma função dateIsValid que deve
# devolver True se os seus argumentos formarem uma data válida
# e devolver False no caso contrário.
# Por exemplo, dateIsValid(1980, 2, 29) deve devolver True,
# dateIsValid(1980, 2, 30) deve devolver False.

def dateIsValid(year, month, day):
   
    if (month > 12 or day < 1 or month < 1 or day > monthDays(year, month)):
        return False
        
    else:
        return True

# Defina uma função previousDay que devolva o dia anterior a uma dada data.
# Por exemplo, previousDay(1980, 3, 1) deve devolver (1980, 2, 29)

def previousDay(year, month, day):
   
    MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    if day ==  1 and month == 1:
        day = 31
        year -= 1
        month = 12
        
    elif day == 1 and month == 3:
        if isLeapYear(year):
            day = 29
            month = 2
            
        else:
            day = 28
            month = 2
            
    elif day == 1:
        day = MONTHDAYS[month]
        month -= 1
        
    else:
        day -= 1
        
    return(year,month,day)

# No Codecheck, não chame nenhuma função: o sistema trata disso.