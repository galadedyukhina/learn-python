inputAllMinutes = int(input())
hoursSleep = int(input())
minutesSleep = int(input())
hoursAlarm = inputAllMinutes // 60
minutesAlarm = inputAllMinutes % 60
preFinalMinutes = minutesSleep + minutesAlarm
preFinalHours = preFinalMinutes // 60
finalMinutes = preFinalMinutes % 60
finalHours = hoursSleep + hoursAlarm + preFinalHours
print(finalHours)
print(finalMinutes)
