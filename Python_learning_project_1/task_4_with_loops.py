x = 0
while x < 10:
    print(f"print x-> {x}")
    x = x + 1 #it will keep printing x=0

x = 0
while x <= 4:
    print(f"print x-> {x}")
    x = x + 1 #it will break out of the loop

x = 0
while x < 10:
    print(f"print x-> {x}")
    if x == 4:
        break

    x += 1