class MyStack:

    def __init__(self):
        self.my_queue = deque()

    def push(self, x: int) -> None:
        size = len(self.my_queue)
        self.my_queue.append(x)
        for i in range(size):
            temp = self.top()
            self.pop()
            self.my_queue.append(temp)


            
        
    def pop(self) -> int:
        return self.my_queue.popleft()

        

    def top(self) -> int:
        return self.my_queue[0]
        

    def empty(self) -> bool:
        return not bool(self.my_queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()