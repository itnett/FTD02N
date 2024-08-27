public class Main {
    public static void main(String[] args) {
        // Testing LinkedList
        LinkedList linkedList = new LinkedList();
        linkedList.add(1);
        linkedList.add(2);
        linkedList.add(3);
        linkedList.display();
        linkedList.remove(2);
        linkedList.display();

        // Testing Stack
        Stack stack = new Stack(5);
        stack.push(10);
        stack.push(20);
        stack.push(30);
        System.out.println("Top of the stack: " + stack.peek());
        System.out.println("Popped from stack: " + stack.pop());

        // Testing Queue
        Queue queue = new Queue(5);
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        System.out.println("Front of the queue: " + queue.peekFront());
        System.out.println("Dequeued from queue: " + queue.dequeue());

        // Testing BinaryTree
        BinaryTree binaryTree = new BinaryTree();
        binaryTree.insert(50);
        binaryTree.insert(30);
        binaryTree.insert(70);
        binaryTree.insert(20);
        binaryTree.insert(40);
        binaryTree.insert(60);
        binaryTree.insert(80);
        System.out.print("Inorder traversal: ");
        binaryTree.inorder();
    }
}