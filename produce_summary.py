def sending_email(day, file, find_melon):
    """
    This function arguments must be string type.
    \narguments:
    \nday = string type number
    \nfile = string type
    \nfind_melon = string type
    """

    print(f"Day {day}")
    the_file = open(f"{file}")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        # melon = words[0]
        # count = words[1]
        # amount = words[2]

        melon, count, amount = words

        if melon == find_melon:
            print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()


for i in range(1, 4):
    sending_email(f'{i}', f'um-deliveries-day-{i}.txt',
                  'Scaly Bark Watermelon')
