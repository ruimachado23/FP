# Transforma segundos em anos, dias, horas, minutos e segundos e retorna uma string com o resultado
# Exemplo: 3662 -> "1 hour, 1 minute and 2 seconds"
# Exemplo: 15731080 -> "182 days, 1 hour, 44 minutes and 40 seconds"

def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        h = seconds // 3600
        m = seconds // 60 - h*60
        s = seconds % 3600 - m*60
        
        if h == 0 and m == 0:
            if s == 1:
                return '1 second'
            else:
                return s + ' seconds'
        if h == 0 and s == 0:
            if m == 1:
                return '1 minute'
            else:
                return m 
        
        
        return h,m,s
    
def main():
    assert(format_duration(1) == "1 second")
    assert(format_duration(62) == "1 minute and 2 seconds")
    assert(format_duration(120) == "2 minutes")
    assert(format_duration(3600) == "1 hour")
    assert(format_duration(3662) == "1 hour, 1 minute and 2 seconds")
    assert(format_duration(15731080) == "182 days, 1 hour, 44 minutes and 40 seconds")
    assert(format_duration(132030240) == "4 years, 68 days, 3 hours and 4 minutes")
    assert(format_duration(205851834) == "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
    assert(format_duration(253374061) == "8 years, 12 days, 13 hours, 41 minutes and 1 second")
    assert(format_duration(242062374) == "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
    assert(format_duration(101956166) == "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
    assert(format_duration(33243586) == "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")
    assert(format_duration(0) == "now")
    print("All tests passed!")

if __name__ == "__main__":
    main()