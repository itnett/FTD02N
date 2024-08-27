// Queue class
class Queue {
    private int maxSize;
    private int[] queueArray;
    private int front;
    private int rear;
    private int nItems;

    Queue(int size) {
        maxSize = size;
        queueArray = new int[maxSize];
        front = 0;
        rear = -1;
        nItems = 0;
    }

    // Insert an element into the queue
    void enqueue(int value) {
        if (rear == maxSize - 1) {
            rear = -1;
        }
        queueArray[++rear] = value;
        nItems++;
    }

    // Remove an element from the queue
    int dequeue() {
        if (nItems == 0) {
            System.out.println("Queue is empty");
            return -1;
        } else {
            int temp = queueArray[front++];
            if (front == maxSize) {
                front = 0;
            }
            nItems--;
            return temp;
        }
    }

    // Peek at the front element
    int peekFront() {
        return queueArray[front];
    }

    // Check if the queue is empty
    boolean isEmpty() {
        return nItems == 0;
    }
}