pos = input("Please input a chess squares: ")

letters = ['a', 'c', 'e', 'g',]

if pos[0] in letters and int(pos[1]) % 2 != 0:
    print('Black')
else:
    print("White")