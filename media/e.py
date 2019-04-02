def generator():
    i = 1
    while True:
        yield 3 * i
        i += 1


for i in generator():
    print(i)
