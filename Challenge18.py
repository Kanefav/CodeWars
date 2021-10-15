def make_readable(seconds):
    output = "00:00:00"
    minutes = hour = 0
    verf = ''
    while True:
        if seconds >= 60:
            minutes += 1
            seconds -= 60
        else:
            if minutes >= 60:
                hour += 1
                minutes -= 60
            else:
                print(f'hour: {hour}, minutes: {minutes} seconds: {seconds}')
                if hour <= 9:
                    verf += 'hour'
                    output = f"0{hour}:00:00"
                    print('1')
                    print(output)
                else:
                    output = f"{hour}:00:00"
                    
                if minutes <= 9:
                    if verf == 'hour':
                        verf += 'minutes'
                        output = f"0{hour}:0{minutes}:00"
                    else:
                        verf += 'minutes'
                        output = f"{hour}:0{minutes}:00"
                else:
                    if verf == 'hour':
                        output = f"0{hour}:{minutes}:00"
                        print('2')
                        print(output)
                    else:
                        output = f"{hour}:{minutes}:00"

                if seconds <= 9:
                    if verf == 'hour':
                        output = f"0{hour}:{minutes}:0{seconds}"
                    if verf == 'minutes':
                        output = f"{hour}:0{minutes}:0{seconds}"
                    if verf == 'hourminutes':
                        output = f"0{hour}:0{minutes}:0{seconds}"
                    if verf == '':
                        output = f"{hour}:{minutes}:0{seconds}"
                else:
                    if verf == 'hour':
                        output = f"0{hour}:{minutes}:{seconds}"
                    if verf == 'minutes':
                        output = f"{hour}:0{minutes}:{seconds}"
                    if verf == 'hourminutes':
                        output = f"0{hour}:0{minutes}:{seconds}"
                    if verf == '':
                        output = f"{hour}:{minutes}:{seconds}"
                return output


print(make_readable(3599))