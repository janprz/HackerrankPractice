class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        n = len(self.stack2)
        val = 0
        if not self.stack1:
            for i in range(0,n):
                if i == n-1:
                    val = self.stack2.pop()
                    self.stack1.append(val)
                else:
                    self.stack1.append(self.stack2.pop())
        else:
            val = self.stack1[-1]
        return val
        
    def pop(self):
        if not self.stack1:
            n = len(self.stack2)
            for i in range(0,n-1):
                self.stack1.append(self.stack2.pop())
            self.stack2.pop()
        else:
            self.stack1.pop()    
        
    def put(self, value):
        self.stack2.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())