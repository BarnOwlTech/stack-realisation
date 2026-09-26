from stack import Stack, LimitedStack

if __name__ == "__main__":
    stack = Stack()
    stack.push(1, 2, 3, "aboba", False, 71, 25)
    print(stack)  # Stack: [1, 2, 3]
    print(stack.pop())  # 25
    print(stack.peek())  # 71
    print(stack.contains("aboba"))  # True
    stack.clear()
    print(stack.is_empty())  # True
    print("----")
    limited_stack = LimitedStack(limit=3)
    limited_stack.push(1, 2, 3)
    print(limited_stack)  # Stack: [1, 2, 3]
    # limited_stack.push(4)  # Raises StackOverflowException
    limited_stack.pop_multiple(2)
    print(limited_stack)  # Stack: [1]
    limited_stack.push(4, False)
    print(limited_stack)  # Stack: [1, 4, False]
