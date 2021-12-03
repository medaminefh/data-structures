from linkedList import LinkedList

l = LinkedList()

l.add_at_front(5)
l.add_at_front(6)
l.insert(30, 0)
l.add_at_end(25)
l.insert(100, 1)
l.add_at_front(8)
l.add_at_end(22)
l.add_at_front(81)
l.insert(-25, 4)
l.remove(-25)
l.remove(81)
l.remove(22)


print(l.size())
print(l)
print(l.get_Last_node())
print(l.search(25))
