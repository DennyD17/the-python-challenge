def hide_and_seek_generator(n):
    num_of_entrances = 0
    number = '1'
    next_number = ''
    j =2
    while j != n:
        for i in range(0, len(number)):
            try:
                z = number[i + 1]
            except IndexError:
                num_of_entrances += 1
                next_number = next_number + str(num_of_entrances) + number[i]
            else:
                if number[i] == number[i + 1]:
                    num_of_entrances += 1
                else:
                    num_of_entrances += 1
                    next_number = next_number + str(num_of_entrances) + number[i]
                    num_of_entrances = 0
        yield next_number
        number, next_number, num_of_entrances = next_number, '', 0
        j += 1

for i in hide_and_seek_generator(32):
    print(len(i))
print(hide_and_seek_generator(32))