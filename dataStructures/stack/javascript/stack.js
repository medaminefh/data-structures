class Stack {
  constructor() {
    this.items = [];
    this.is_empty.bind = this.is_empty;
    this.push.bind = this.push;
    this.pop.bind = this.pop;
    this.print_queue.bind = this.print_queue;
  }

  // check if it's empty
  is_empty() {
    return this.items.length === 0;
  }

  // add element
  push(item) {
    this.items.unshift(item);
  }

  // remove element
  pop() {
    if (this.is_empty()) {
      console.log("There is nothing to delete!");
      return;
    }
    this.items.shift();
  }

  // output element
  print_stack() {
    console.log(this.items);
  }
}

module.exports = Stack;
