def sum(x):
    s = 0
    for number in x:
        if number % 3 and number % 5:
            s += number
    print(s)
sum(range(0, 1000))
