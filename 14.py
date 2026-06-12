for x in range(0, 29):
    if x < 10:
        b = int(f'463{x}7921', 29) + int(f'8241{x}153', 29)
    else:
        y = chr(ord("A") + x - 10)
        b = int(f'463{y}7921', 29) + int(f'8241{y}153', 29)
    if b % 28 == 0:
        print(b / 28)