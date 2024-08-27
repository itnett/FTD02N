// Superklasse
class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

// Underklasse som arver Animal
class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}

// Bruk av polymorfisme
public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        myDog.sound(); // Utskrift: Dog barks
    }
}