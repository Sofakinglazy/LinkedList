#!usr/local/python3
'''\
Build a linked list
'''

import sys

class ListNode():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def link(self, ln):
        if not isinstance(ln, self.__class__):
            raise TypeError('Input should be <ListNode> type')
        else:
            self.next = ln

    def print_backward(self, head_flag = True):
        if self.next:
            tail = self.next
            tail.print_backward(False)
        print(self, end = '')
        if not head_flag:
            print(',', end = '')

    def __str__(self):
        return str(self.val)
    def __lt__(self, other):
        return self.val < other.val
    def __eq__(self, other):
        return self.val == other.val
    def __le__(self, other):
        return self.val <= other.val

class LinkedList():
    def __init__(self, head = None):
        self.length = 0
        self.head = head

    def sorted_link(self, ln):
        if not self.is_sorted():
            # self.sort()
            pass
        curr = self._head
        '''if head has been set'''
        if not curr:
            self._head = ln
            return
        '''operate the current node'''
        if curr > ln:
            ln.next = curr
            self._head = ln
            # print('should insert from the front')
            return
        '''check the next node and so on'''
        nextn = curr.next
        while nextn:
            '''if next val is less, then find the next one
                otherwise, found the inserting point'''
            if nextn < ln:
                curr = nextn
                nextn = nextn.next
            elif nextn == ln:
                return
            else:
                print('found the insert point')
                ln.next = curr.next
                curr.next = ln
                return
        else:
            curr.next = ln

    def sort(self):
        temp = ListNode()
        curr = self._head
        min_node = curr
        nextn = curr.next
        # while nextn:

    def is_sorted(self):
        if self._head is None:
            return False
        curr = self._head
        nextn = curr.next
        while nextn:
            if curr.val > nextn.val:
                return False
            curr = nextn
            nextn = curr.next
        return True

    def pop(self, index = 0):
        if index > self.length - 1:
            raise ValueError('index is out of bound')
        curr = self._head



    def pop_second(self):
        if self.length < 3:
            err = 'length of linked list required at least 3 but {} here'.format(self.length)
            raise ValueError(err)
        second = self._head.next
        third = second.next
        self._head.next = third
        second.next = None
        return second

    def print_backward(self):
        print('[', end = '')
        self.head.print_backward()
        print(']')

    def __str__(self):
        s = '['
        head = self._head
        while head:
            s += str(head)
            if head.next:
                s += ','
            head = head.next
        s += ']'
        return s

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, h):
        # if h is None, shouldn't create a object with an object None
        if isinstance(h, ListNode) or not h:
            self._head = h
        else:
            self._head = ListNode(h)

    @property
    def length(self):
        self._length = 0
        node = self._head
        while node:
            self._length += 1
            node = node.next
        return self._length

    @length.setter
    def length(self, l):
        self._length = l

def main(argv):
    ln1 = ListNode(1)
    ln2 = ListNode(4)
    ln3 = ListNode(6)
    ln4 = ListNode(2)
    ln5 = ListNode(3)
    ln6 = ListNode(7)

    '''linked list one'''
    ln1.link(ln2)
    ln2.link(ln3)
    '''linked list two'''
    ln4.link(ln5)
    ln5.link(ln6)

    l1 = LinkedList()
    l1.head = ln1

    ln3.link(ln4)

    if len(argv) > 1:
        if argv[1] == 'test':
            test(l1)


def test(l1):
    '''test print'''
    print('- forward print')
    print(l1)
    print('- backward print')
    l1.print_backward()
    '''test pop_second'''
    print('- pop second')
    second = l1.pop_second()
    print(l1)
    print(l1.length)
    try:
        ln_t = ListNode(0) # only one element
        l_1 = LinkedList(ln_t)
        l_1.pop_second()
        ln_t.link(ListNode(10))
        l_1.pop_second() # two elements
    except ValueError as e:
        print('ValueError:', e)
    ''' test is_sorted '''
    print('-------------------------')
    print('Sorted list: ', l1.is_sorted(), l1)
    print('Sorted list: ', l_1.is_sorted(), l_1)
    ln_t.link(ListNode(1))
    print('Sorted list: ', l_1.is_sorted(), l_1)
    empty = LinkedList()
    print('Sorted list: ', empty.is_sorted(), empty)
    ''' test cmp'''
    print('-------------------------')
    print('great than:', ListNode(0) > ListNode(1))
    print('great equal:', ListNode(0) >= ListNode(1))
    print('equal:', ListNode(0) == ListNode(1))
    print('less than:', ListNode(0) < ListNode(1))
    print('great equal:', ListNode(0) <= ListNode(1))
    ''' test sorted link'''
    print('-------------------------')
    ln1 = ListNode(1)
    ln2 = ListNode(4)
    ln3 = ListNode(6)
    ln4 = ListNode(2)
    ln5 = ListNode(3)
    lns = ListNode('a')

    '''two same listnode don't allow in the linked list'''
    l2 = LinkedList()
    l2.sorted_link(ln2)
    l2.sorted_link(ln1)
    l2.sorted_link(ln5)
    l2.sorted_link(ln3)
    l2.sorted_link(ln4)
    # l2.sorted_link(lns)
    print(l2)



if __name__ == '__main__': main(sys.argv)