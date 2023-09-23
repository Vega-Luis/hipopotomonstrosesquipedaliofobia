import time
second = 0
minute = 0
hour = 1
day = 0
hour24 = 0
control = 0 



def reloj():
    global second
    global minute
    global hour
    global day
    global hour24
    forma = 'AM'
    if hour24 == 1:
        forma = 'PM'
    print(f'hora: {hour}:0{minute}:{second} {forma} dia: {day}')
    second += 1
    time.sleep(0.0001)
    print('********************************************************************')
    # control += 1
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    # print(f'hora: {hour}:{minute}:{second} dia: {day}')
    if hour == 13 and hour24 == 1:
        day += 1
        hour = 1
        hour24 = 0
    if hour == 13:
        hour = 1
        hour24 += 1
    

while True:
    reloj()
# for i in range(3601):
#     reloj()