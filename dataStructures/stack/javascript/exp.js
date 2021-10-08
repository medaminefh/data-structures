const Stack = require("./stack");

const s = new Stack();

s.push(1);
s.push(2);
s.push(3);
s.push(4);

s.print_stack();

s.pop();
s.pop();

s.print_stack();
