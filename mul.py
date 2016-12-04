#!usr/local/python3

def print_multi_table():
    mul = 1
    by = 1
    ''' loop by til 9'''
    re_flag = False
    while by < 10 and by > 0:
        ''' increment mul til by'''
        while mul <= by:
            result = mul * by
            print('{}*{}={}'.format(mul, by, result), end = ' ')
            mul += 1
        print()
        if by == 9:
            re_flag = True
        if not re_flag: by += 1
        else: by -= 1
        '''reset mul'''
        mul = 1


def main():
    print_multi_table()

if __name__ == '__main__': main()