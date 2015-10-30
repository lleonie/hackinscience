def sum(x):
    s = 0
    for number in x:
        if not number % 3 or not number % 5:
            s += number
    print(s)
sum(range(1000))
