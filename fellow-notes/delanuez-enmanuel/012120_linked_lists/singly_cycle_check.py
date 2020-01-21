'''
Cycle check: determine if any node points to a node previously referenced node

Example:
A -> B -> C -> B
'''
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

# Testing, create cycle list
a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a # cycle

# Non cycle list
e = Node(1)
f = Node(2)
g = Node(3)

e.next_node = f
f.next_node = g
g.next_node = None

def my_cycle_check(node):
    refs = {}
    while node.next_node != None:
        if node.value in refs:
            return True
        else:
            refs[node.value] = 1
        node = node.next_node
    return False

print(my_cycle_check(a) == True)
print(my_cycle_check(e) == False)

# Best solution (linear run and space time)

def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True
    return False

print(cycle_check(a) == True)
print(cycle_check(e) == False)

'''
This works because marker2 moves faster than marker1, if this is a cycle, then marker2 will eventually 'lap' over marker1
We check that it is indeed a cycle by checking in our while loop if we are reaching or are at a node that is the last of its sequence
'''