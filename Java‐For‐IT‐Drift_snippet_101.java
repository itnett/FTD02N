public class Person {
    public String navn; // Kan nås fra andre klasser
    private int alder; // Kan kun nås innen denne klassen

    public Person(String navn, int alder) {
        this.navn = navn;
        this.alder = alder;
    }

    // Offentlig metode for å få alder
    public int getAlder() {
        return alder;
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        System.out.println(person.navn); // Tilgang til offentlig variabel
        System.out.println(person.getAlder()); // Tilgang til privat variabel via offentlig metode
    }
}