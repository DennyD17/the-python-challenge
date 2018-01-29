def is_polindrom(num):
    num_str = str(num)
    first_half = num_str[:len(num_str)//2]
    second_half = num_str[len(num_str)//2:] if len(num_str) % 2 == 0 else num_str[(len(num_str) // 2)+1:]
    return True if first_half == second_half[::-1] else False


a =123999321

print(iter([1,2,3,4]))
