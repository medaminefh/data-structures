class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        """
        Return a meaningfull status of the list
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head : {current.data}] => ")

            elif current.next is None:
                nodes.append(f"[Tail : {current.data}]")

            else:
                nodes.append(f"[{current.data}] => ")

            current = current.next

        return "".join(nodes)

    def add_at_front(self, data):
        """
        Add a Node at the front of the list
        """
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

        if int(self.size()) == 1:
            self.tail = self.head

    def add_at_end(self, data):
        """
        Add a Node at the end of the list
        """
        last_node = Node(data)
        self.tail.next = last_node
        self.tail = last_node

    def get_Last_node(self):
        """
        Get the last Node in the list
        """
        return self.tail

    def size(self):
        """
        Get The size of the list
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return f"{count}"

    def search(self, data):
        """
        Search for the first occurence of the data in the linked list
        """

        current = self.head

        if current.data == data:
            return current

        elif self.tail.data == data:
            return self.tail

        else:
            while current:
                if current.data == data:
                    return current
                else:
                    current = current.next
            return None

    def insert(self, data, index):
        """
        Insert a Node at any position in the linked list
        """

        # if the index is 0 then we will add the new Node at the front
        if index == 0:
            self.add_at_front(data)

        # We will add the new Node at the end
        elif index == int(self.size()) - 1:
            self.add_at_end(data)

        else:
            new_Node = Node(data)
            current = self.head
            position = index

            while position > 1:
                current = current.next
                position -= 1

            new_Node.next = current.next
            current.next = new_Node

    def remove(self, data):
        """
        Remove a Node in a Linked list
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data is data and current is self.head:
                found = True
                self.head = current.next

            elif current.data is self.get_Last_node().data:
                found = True
                previous.next = current.next
                self.tail = previous

            elif current.data is data:
                found = True
                previous.next = current.next

            else:
                previous = current
                current = current.next

        return current
