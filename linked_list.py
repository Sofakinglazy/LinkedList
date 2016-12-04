#!usr/local/python3
'''\
Build a linked list
'''

import sys

class ListNode():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def append(self, ln):
        if not isinstance(ln, self.__class__):
            raise TypeError('Input should be <ListNode> type')
        else:
            self.next = ln

    def __str__(self):
        return str(self.val)


def print_list(ln):
    print('[', end = '')
    while ln:
        print(ln, end = '')
        if ln.next:
            print(',', end = '')
        ln = ln.next
    print(']')

'''wrapper'''
def print_backward(ln = None):
    print('[', end = '')
    print_backward_core(ln)
    print(']')

'''helper'''
def print_backward_core(ln = None, head_flag = True):
    if ln is None: return
    head = ln
    tail = ln.next
    print_backward_core(tail, False)
    print(head, end = '')
    if not head_flag:
        print(',', end = '')

def pop_second(ln):
    if ln is None: return
    first = ln
    second = ln.next
    if second is None or second.next is None:
        raise ValueError('At least three elements in the list required.')
    first.next = second.next
    second.next = None
    return second

def main(argv):
    ln1 = ListNode(1)
    ln2 = ListNode(4)
    ln3 = ListNode(6)
    ln4 = ListNode(2)
    ln5 = ListNode(3)
    ln6 = ListNode(7)

    '''linked list one'''
    ln1.append(ln2)
    ln2.append(ln3)
    '''linked list two'''
    ln4.append(ln5)
    ln5.append(ln6)

    if len(argv) > 1:
        if argv[1] == 'test':
            '''test print'''
            print('- forward print')
            print_list(ln1)
            print('- backward print')
            print_backward(ln1)
            '''test pop_second'''
            print('- pop second')
            second = pop_second(ln1)
            print(second)
            print_list(ln1)
            try:
                ln_t = ListNode(0) # only one element
                pop_second(ln_t)
                ln_t.append(ListNode(10))
                pop_second(ln_t) # two elements
            except ValueError as e:
                print('ValueError:', e)


if __name__ == '__main__': main(sys.argv)