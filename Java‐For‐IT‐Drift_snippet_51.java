// Superklasse
     class Animal {
         public void makeSound() {
             System.out.println("Animal sound");
         }
     }

     // Underklasse
     class Dog extends Animal {
         @Override
         public void makeSound() {
             System.out.println("Bark");
         }
     }

     public class Main {
         public static void main(String[] args) {
             Dog dog = new Dog();
             dog.makeSound(); // Bark
         }
     }