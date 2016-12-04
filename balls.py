#!usr/local/python3
'''\
One of twelve balls, which weighs differently,
need to be picked out.
Method:
        compare balls two by two and put
        them into good list and bad list
'''

from random import shuffle

def main():
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    shuffle(l)
    good = list()
    bad = list()
    for i in range(0, len(l), 2):
        ''' if the bad list is not empty '''
        if bad:
            break
        if l[i] == l[i+1]:
            good.append(l[i])
            good.append(l[i+1])
        else:
            bad.append(l[i])
            bad.append(l[i+1])
            index = i
    if len(bad) == 2:
        if bad[0] == good[0]:
            print('Answer: ', index+1)
        else:
            print('Answer: ', index)
    print(l)

if __name__ == '__main__': main()