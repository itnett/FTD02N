// Definere klassen Person
public class Person {
    private String name;
    private int age;

    // Konstruktør
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Metode for å få navn
    public String getName() {
        return name;
    }

    // Metode for å få alder
    public int getAge() {
        return age;
    }
}

// Opprette objekter av klassen Person
public class Main {
    public static void main(String[] args) {
        Person person1 = new Person("Alice", 30);
        Person person2 = new Person("Bob", 25);

        System.out.println(person1.getName()); // Utskrift: Alice
        System.out.println(person2.getName()); // Utskrift: Bob
    }
}