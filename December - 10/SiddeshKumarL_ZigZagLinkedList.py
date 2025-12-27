class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

n = int(input("Enter N:"))
vals = list(map(int, input('Enter node values:').split()))

if n == 0:
    exit()

head = Node(vals[0])
cur = head
for v in vals[1:]:
    cur.next = Node(v)
    cur = cur.next

slow = head
fast = head
prev = None
while fast and fast.next:
    prev = slow
    slow = slow.next
    fast = fast.next.next

if prev:
    prev.next = None

prev = None
curr = slow
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
second = prev

first = head
dummy = Node(0)
tail = dummy
toggle = True
while first or second:
    if toggle and first:
        tail.next = first
        tail = tail.next
        first = first.next
    elif not toggle and second:
        tail.next = second
        tail = tail.next
        second = second.next
    toggle = not toggle
tail.next = None

res = []
cur = dummy.next
while cur:
    res.append(str(cur.val))
    cur = cur.next
print(" ".join(res))
