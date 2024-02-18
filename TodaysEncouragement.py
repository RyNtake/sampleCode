daylist = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print('What day of the week is it today?\nYou can use Mon/Tue/Wed/Thu/Fri/Sat/Sun')

dd = input()

exist = dd in daylist

if exist == False   :
    print('INSERT TRUE DAYNAME')
elif dd == 'Sat':
    print('Happpppppppppppppyyyyyyyyyyyyyyyy')
elif dd == 'Sun':
    print('Feel So Goood')
elif dd == 'Mon':
    print('I\'m Die, Thank you forever')
else :
    print('You cannot give up just yet... RyN! Stay determined...')