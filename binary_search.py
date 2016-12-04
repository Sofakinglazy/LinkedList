#!usr/local/python3
'''\
The best solution to solve the twelve balls puzzle
'''

from random import shuffle

def main():
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    shuffle(l)
    ''' divide the balls into 3 sections '''
    l1 = l[0:4]
    l2 = l[4:8]
    l3 = l[8:12]
    if sum(l1) == sum(l2):
        bad = l3
        index = 8
    else:
        if sum(l1) == sum(l3):
            bad = l2
            index = 4
        else:
            bad = l1
            index = 0
    good = list()
    bad2 = list()
    for i in range(0, len(bad), 2):
        if bad[i] == bad[i+1]:
            good.append(bad[i])
            good.append(bad[i+1])
        else:
            bad2.append(bad[i])
            bad2.append(bad[i+1])
            index += i
    if len(bad2) == 2:
        if bad2[0] == good[0]:
            print('Answer: ', index+1)
        else:
            print('Answer: ', index)
    print(l)

if __name__ == '__main__': main()