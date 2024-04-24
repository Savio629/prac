probabilityTables = {}

probabilityTables['Burglary'] = [['T', 0.001]]
probabilityTables['Earthquake'] = [['T', 0.002]]

probabilityTables['Alarm'] = [['T', 'T', 0.95], ['T', 'F', 0.95], ['F', 'T', 0.29], ['F', 'F', 0.001]]
probabilityTables['JohnCalls'] = [['T', 0.90], ['F', 0.05]]
probabilityTables['MaryCalls'] = [['T', 0.70], ['F', 0.01]]

order = ['Burglary', 'Earthquake', 'Alarm', 'JohnCalls', 'MaryCalls']
print(probabilityTables)

userInp = input("Enter your preferences for Burglary, Earthquake, Alarm, JohnCalls and MaryCalls: ").split(" ")
res = 1

if userInp[0] == 'True':
    res *= probabilityTables[order[0]][0][1]
else:
    res *= (1 - probabilityTables[order[0]][0][1])
if userInp[1] == 'True':
    res *= probabilityTables[order[1]][0][1]
else:
    res *= (1 - probabilityTables[order[1]][0][1])
if userInp[0] == 'True' and userInp[1] == 'True':
    res *= probabilityTables[order[2]][0][2]
elif userInp[0] == 'True' and userInp[1] == 'False':
    res *= probabilityTables[order[2]][1][2]
elif userInp[1] == 'True' and userInp[0] == 'False':
    res *= probabilityTables[order[2]][2][2]
else:
    res *= probabilityTables[order[2]][3][2]
if userInp[3] == 'True':
    res *= probabilityTables[order[3]][0][1]
else:
    res *= (1 - probabilityTables[order[3]][1][1])
if userInp[4] == 'True':
    res *= probabilityTables[order[4]][0][1]
else:
    res *= (1 - probabilityTables[order[4]][1][1])

print(f"The probability is - {res}")