#!usr/local/python3

import ceil

class ListNode:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

def length(head):
    _length = 0
    while head:
        _length += 1
        head = head.next
    return _length

def build_one_two_three():
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln1.next = ln2
    ln2.next = ln3
    return ln1

def push(head, node):
    if not node:
        return head
    if not isinstance(node, ListNode):
        node = ListNode(node)
    ''' empty node'''
    if not head.data:
        head = node
        return head
    node.next = head
    head = node
    return head

def pop(head):
    if not head.data or not isinstance(head, ListNode):
        raise ValueError('The linked list is empty')
    result = head.data
    if not head.next:
        ''' set the head as an empty list'''
        head = ListNode()
    else:
        head = head.next
    return (result, head)

def add_right(head, node):
    if not node:
        return head
    if not isinstance(node, ListNode):
        node = ListNode(node)
    '''solution for empty list'''
    if not head.data:
        head = node
        return head
    curr = head
    while curr:
        '''tail of list'''
        if not curr.next:
            curr.next = node
            break
        curr = curr.next
    return head

def tail(head):
    if not head:
        raise TypeError('None type')
    curr = head
    while curr.next:
        curr = curr.next
    tail = curr
    return tail

def get(head, index = 0):
    if index > length(head) - 1:
        err = 'index out of bound {} at most'.format(length(head) - 1)
        raise ValueError(err)
    i = 0
    curr = head
    while i < index:
        curr = curr.next
        i += 1
    return curr.data

def insert(head, node, index = 0):
    if not node or node.data is None:
        raise ValueError('Invalid inserted node')
    if index > length(head) - 1:
        err = 'index out of bound {} at most'.format(length(head) - 1)
        raise ValueError(err)
    if index == 0:
        head = push(head, node)
        return head
    i = 0
    curr = head
    ''' get the last node in front of inserting point'''
    while i < index - 1:
        curr = curr.next
        i += 1
    second = curr.next
    curr.next = node
    node.next = second
    return head

def sorted_insert(head, node):
    if node is None or node.data is None:
        raise ValueError('Invalid inserted node')
    if not is_sorted(head):
        raise TypeError('Not a sorted list')
    if head and head.data is None:
        head = node
        return head
    ''' less than the first value'''
    if head.data is not None and head.data > node.data:
        node.next = head
        head = node
        return head
    ''' greater than first one'''
    curr = head
    second = head.next
    done = False
    while second and second.data:
        if second.data > node.data:
            curr.next = node
            node.next = second
            done = True
            break
        curr = second
        second = curr.next
    else:
        curr.next = node # should append at the end
    return head

def is_sorted(head):
    '''head is a None'''
    if not head:
        return False
    elif head.data is None:
        return True
    ''' singluar list'''
    if not head.next:
        return True
    curr = head
    second = head.next
    while second and second.data:
        if curr.data > second.data:
            return False
        curr = second
        second = curr.next
    return True

def append(head1, head2):
    if not head1 or not head2:
        raise TypeError('None type input')
    t = tail(head1)
    t.next = head2
    return head1

def split_half(head):
    l = length(head)
    if l == 0 or head.val is None:
        raise ValueError('Invalid input list')
    i = 0
    if l % 2 == 0:
        half = int(l / 2) # even i.e. 4 -> 2
    else:
        half = math.ceil(l / 2) # odd i.e 3 -> 2
    curr = head
    while i < half:
        curr = curr.next
    second = curr.next
    curr.next = None
    first = head
    return first, second

def delete_list(head):
    if not head:
        return
    if head.next:
        delete_list(head.next)
        head.data = None
        head.next = None

def print_list(head):
    print('[', end = '')
    while head:
        if head.data is not None:
            print(head, end = '')
        if head.next:
            print(', ', end = '')
        head = head.next
    print(']')

def main():
    head = build_one_two_three()
    print_list(head)
    print(length(head))
    head = push(head, 1)
    print_list(head)
    head = push(head, ListNode(2))
    print_list(head)
    print(length(head))

    head = add_right(head, 5)
    print_list(head)

    ''' test empty list '''
    print('---------------------')
    ln_empty = ListNode()
    print_list(ln_empty)
    ln_empty = push(ln_empty, 1)
    print_list(ln_empty)
    ln_empty = ListNode()
    ln_empty = add_right(ln_empty, 2)
    print_list(ln_empty)

    ''' test get at index'''
    print('---------------------')
    head = build_one_two_three()
    print(get(head, 0))
    print(get(head, 1))
    print(get(head, 2))
    try: print(get(head, 3))
    except ValueError as e: print('ValueError:', e)

    '''test delete list'''
    print('---------------------')
    head = build_one_two_three()
    print_list(head)
    delete_list(head)
    print_list(head)

    '''test pop method'''
    print('---------------------')
    head = build_one_two_three()
    result, head = pop(head)
    print(result)
    print_list(head)
    result, head = pop(head)
    print(result)
    print_list(head)
    head = ListNode()
    try:
        result2, head = pop(head)
        print(result2)
        print_list(head)
    except ValueError as e: print('ValueError:', e)

    '''test insert method'''
    print('---------------------')
    head = build_one_two_three()
    node = ListNode(4)
    head = insert(head, node)
    print_list(head)
    node = ListNode(0)
    head = insert(head, node, 2)
    print_list(head)
    try:
        node = ListNode()
        head = insert(head, node, 0) # out of bound
        print_list(head)
    except ValueError as e: print('ValueError:', e)

    '''test sorted_insert method'''
    print('---------------------')
    head = build_one_two_three()
    print(is_sorted(head), end = ':')
    print_list(head)
    head = push(head, ListNode(5))
    print(is_sorted(head), end = ':')
    print_list(head)
    head = ListNode(1)
    print(is_sorted(head), end = ':')
    print_list(head)
    head = ListNode()
    print(is_sorted(head), end = ':')
    print_list(head)

    '''test sorted_insert method'''
    print('---------------------')
    head = build_one_two_three()
    print_list(head)
    node = ListNode(1.5)
    head = sorted_insert(head, node)
    print_list(head)
    node = ListNode(0)
    head = sorted_insert(head, node)
    print_list(head)
    node = ListNode(4)
    head = sorted_insert(head, node)
    print_list(head)
    head = ListNode()
    node = ListNode(0)
    head = sorted_insert(head, node)
    print_list(head)
    node = ListNode(1)
    head = sorted_insert(head, node)
    print_list(head)

    '''test tail method'''
    print('---------------------')
    head = build_one_two_three()
    print_list(head)
    t = tail(head)
    print_list(t)

    '''test append method'''
    print('---------------------')
    head = build_one_two_three()
    print_list(head)
    head2 = ListNode(4)
    head2 = add_right(head2, ListNode(5))
    print_list(head2)
    head = append(head, head2)
    print_list(head)

if __name__ == '__main__': main()



