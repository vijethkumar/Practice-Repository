E = "00:00"
L = "23:01"

Entry = E.split(':')
Leave = L.split(':')

print(Entry)
print(Leave)
Hours = int(Leave[0]) - int(Entry[0])
Minutes = int(Leave[1]) - int(Entry[1])

Base_Fare = 2
First_Hour_Fare = 3
Additional_hours = 0
if Minutes < 0:
    Hours=Hours-1
elif Minutes == 0:
    Hours=Hours
else:
    Hours = Hours+1

if Minutes==0 and Hours==0:
    Final_Fare=0
    Final_Fare1=0
else:
    Final_Fare= Base_Fare + First_Hour_Fare + ((Hours-1)*4)
    Final_Fare1= Base_Fare + ((Hours)*4) -1
print(Hours)
print(Minutes)
print(Final_Fare)
print(Final_Fare1)
