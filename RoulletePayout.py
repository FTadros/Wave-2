import random

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 13, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

chosen = random.randrange(0, 38)
chosen = int(chosen)

if chosen % 2 == 0:
    odd_even = 'even'
else:
    odd_even = 'odd'

if chosen in red:
    colour = 'red'
else:
    colour = 'black'

if chosen in range(19):
    int_range = '0 to 18'

else:
    int_range = '19 to 36'

var = [chosen, colour, odd_even, int_range]

if chosen == 0:
    print ('Pay 0')
elif chosen == 37:
    print('Pay 00')

else:
    for i in var:
        print('Pay', i)
