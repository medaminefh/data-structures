class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

// its like __repr__ in python (a string representation for the Node) a little bit tricky though
/*Node.prototype.toString = function () {
  return `<Node data: ${this.data}>`;
};*/

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  add_at_front(data) {
    let newNode = new Node(data);
    newNode.next = this.head;
    this.head = newNode;
    if (Number(this.size()) == 1) {
      this.tail = this.head;
    }
  }

  add_at_end(data) {
    let lastNode = new Node(data);
    this.tail.next = lastNode;
    this.tail = lastNode;
  }

  insert(data, index) {
    if (index > Number(this.size())) return;
    else if (index == 0) {
      this.add_at_front(data);
    } else if (index == Number(this.size())) {
      console.log("Hellow");
      this.add_at_end(data);
    } else {
      let position = index;
      let current = this.head;
      let newNode = new Node(data);

      while (position > 1) {
        current = current.next;
        position -= 1;
      }
      newNode.next = current.next;
      current.next = newNode;
    }
  }

  remove(data) {
    let current = this.head;
    let previous = null;
    let found = false;

    while (current && !found) {
      if (current.data == data && current == this.head) {
        found = true;
        this.head = current.next;
      } else if (current.data == this.get_Last_node()) {
        found = true;
        previous.next = current.next;
        this.tail = previous;
      } else if (current.data == data) {
        found = true;
        previous.next = current.next;
      } else {
        previous = current;
        current = current.next;
      }
    }

    return current;
  }

  get_Last_node() {
    return this.tail.data;
  }

  size() {
    let count = 0;
    let current = this.head;
    while (current) {
      count += 1;
      current = current.next;
    }
    return count;
  }

  print_list() {
    let current = this.head;
    let nodes = [];
    while (current) {
      if (current == this.head) {
        nodes.push(`[Head : ${current.data}] => `);
      } else if (current == this.tail) {
        nodes.push(`[Tail : ${current.data}]`);
      } else {
        nodes.push(`[${current.data}] => `);
      }
      current = current.next;
    }

    return nodes.join("");
  }

  search(data) {
    let current = this.head;

    if (current.data == data) {
      return current;
    } else if (this.tail.data == data) {
      return this.tail;
    } else {
      while (current) {
        if (current.data == data) {
          return current;
        } else {
          current = current.next;
        }
      }
      return null;
    }
  }
}

module.exports = { Node, LinkedList };
