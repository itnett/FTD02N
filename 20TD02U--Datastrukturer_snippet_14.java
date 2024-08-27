// Stack class
class Stack {
    private int maxSize;
    private int[] stackArray;
    private int top;

    Stack(int size) {
        maxSize = size;
        stackArray = new int[maxSize];
        top = -1;
    }

    // Push an element onto the stack
    void push(int value) {
        if (top == maxSize - 1) {
            System.out.println("Stack is full");
        } else {
            stackArray[++top] = value;
        }
    }

    // Pop an element from the stack
    int pop() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            return stackArray[top--];
        }
    }

    // Peek at the top element
    int peek() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            return stackArray[top];
        }
    }

    // Check if the stack is empty
    boolean isEmpty() {
        return top == -1;
    }
}