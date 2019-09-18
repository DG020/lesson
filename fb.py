for i in range(1,1001):
    if i % 3 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 666 == 0:
        print("satan")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buz")
    else:
        print(i)
        