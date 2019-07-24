bottles = 99

while bottles > 0:

    if bottles > 1:
        print('%d bottles of beer on the wall.\n%d bottles of beer!' % (bottles, bottles))
        bottles = bottles - 1

        if bottles == 1:
             print('Take one down, pass it around %d bottle of beer on the wall' % bottles)
             print("\n")
        else:
            print('Take one down, pass it around %d bottles of beer on the wall' % bottles)
            print("\n")

    

    elif bottles == 1:
        print('%d bottle of beer on the wall.\n%d bottle of beer!' % (bottles, bottles))
        bottles = bottles - 1
        print('Take one down, pass it around no more bottles of beer on the wall!!!')

