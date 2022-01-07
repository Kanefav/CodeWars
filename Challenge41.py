def format_duration(seconds):
    sequence = 0
    minutes = hour = 0
    while True:
        if seconds >= 60:
            minutes += 1
            seconds -= 60
        else:
            if minutes >= 60:
                hour += 1
                minutes -= 60
            else:
                if hour >= 1:
                    sequence += 1
                    if hour >= 2:
                        hours = 'hours'
                    else:
                        hours = 'hour'
                    
                if minutes >= 1:
                    sequence += 2
                    if minutes >= 2:
                        minutess = 'minutes'
                    else:
                        minutess = 'minute'
                    
                if seconds >= 1:
                    sequence += 4
                    if seconds >= 2:
                        secondss = 'seconds'
                    else:
                        secondss = 'second'
                    
                
                if sequence == 1:
                    # Horas
                    return f'{hour} {hours}'
                if sequence == 2:
                    # Minutos
                    return f'{minutes} {minutess}'
                if sequence == 3:
                    # Horas e Minutos
                    return f'{hour} {hours} and {minutes} {minutess}'
                if sequence == 4:
                    # Segundos
                    return f'{seconds} {secondss}'
                if sequence == 5:
                    # Horas e Segundos
                    return f'{hour} {hours} and {seconds} {secondss}'
                if sequence == 6:
                    # Minutos e Segundos
                    return f'{minutes} {minutess} and {seconds} {secondss}'
                if sequence == 7:
                    # Horas Minutos e Segundos
                    return f'{hour} {hours}, {minutes} {minutess} and {seconds} {secondss}'
                return 'nothing lol'



print(format_duration(366231232))

