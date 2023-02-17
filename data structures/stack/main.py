# Name              :   Stack
# Version           :   Python 3.x
# Description       :   Implementation of Stack
# Time Complexity   :   For Array/List based implementation O(1)
# Space Complexity  :   Worst - O(1)


# create a stack
def create_stack():
    stack = []
    return stack


# push element into stack
def push_element(stack, element):
    stack.append(element)
    print("Element Inserted: ", element)


# pop element from stack
def pop_element(stack):
    if len(stack) == 0:
        print("Error: Stack Underflow")
    else:
        stack.pop()
        print("Element Popped!")


# is stack empty?
def is_empty(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack is not empty")


# show stack
def display_stack(stack):
    print(stack)


# main
if __name__ == '__main__':
    s = create_stack()
    push_element(s, 3)
    push_element(s, 8)
    push_element(s, 5)
    push_element(s, 1)
    pop_element(s)
    display_stack(s)
    is_empty(s)
