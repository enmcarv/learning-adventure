# Linked Lists

## Essential Questions
+ What is an *abstract data type*?
+ What are the tradeoffs between linked lists and arrays?
+ What are the tradeoffs between singly linked lists and doubly linked lists?
+ What are the run times for insertion, deletion, and accessing from linked lists?

### Grokking Algorithms
#### Arrays
+ allows for random access
+ O(1) reading runtime
+ O(n) insertion runtime

#### Linked Lists
+ allows for quick writing
+ O(1) insertion/deletion runtime
+ O(n) reading reading runtime
+ we can traverse the list, or link hop, or pointer hop

##### Singly Linked Lists
+ collections of nodes forming a linear sequence
+ each node stores a **reference to an element** of the list and **to the next node**
An intance of a singly linked list contains:
+ *head* member, identifies first node of list, not referenced by other nodes
+ *tail* (in some applications), identifies last node on list, points to nothing, null, none
+ Each node is represented as a unique object
+ does not have predetermined fixed size, uses space proportionally
###### Inserting Elements
At the head:
- create new node
- set its element to the new element
- set its *next* link to refer to the current head
- set the list's head to point to this new node

At the tail:
- create new node
- assign its *next* link to none
- set the current tail to point to this new node
- set link's tail to this new node

###### Removing Elements
At the head:
- point head to next element

At the tail:
- must access previous node, and the one before it, and so on
- linear runtime

##### Singly Linked Lists
+ keeps reference to *next* node **and** *previous* node
    **Sentinel Nodes**
    - added to both ends of list
    - *Header* node at the beginning of the list
    - *Trailer* node at the end of the list
    - known as 'dummy' or *sentinel* (guard) nodes

###### Inserting Elements
- *ALWAYS* takes place between two existing nodes
- for front, add between header and the following node