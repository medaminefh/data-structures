from queue import Queue

q = Queue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)

q.print_queue()

q.pop()
q.pop()


q.print_queue()

print(q.is_empty())
