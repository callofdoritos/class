#Basic Variables
oneHour=60
#User Input
speedLimit=float(input('What is the speed limit?'))
userSpeed=float(input('How fast are you going?'))
totalDis=float(input('How far are you traveling?'))
#math stuff
if (speedLimit or userSpeed or totalDis) <= 0:
    print('Invalid Input')
else:
    if userSpeed>=speedLimit:
        s1=float((totalDis/userSpeed)*oneHour)
        s2=float((totalDis/speedLimit)*oneHour)
        timeSaved=int(s2-s1)
        print('If the speed limit is', (int(speedLimit)) ,'MPH, and you are traveling at', (int(userSpeed)) ,'MPH, then you will go', (int(timeSaved)) ,'minutes faster if you were traveling the speed limit.')
    if userSpeed<speedLimit:
        s1=float((totalDis/userSpeed)*oneHour)
        s2=float((totalDis/speedLimit)*oneHour)
        timeLost=int(s1-s2)
        print('If the speed limit is', (int(speedLimit)) ,'MPH, and you are traveling at', (int(userSpeed)) ,'MPH, then you will go', (int(timeLost)) ,'minutes slower than if you were traveling the speed limit.')
    
    
    
    


