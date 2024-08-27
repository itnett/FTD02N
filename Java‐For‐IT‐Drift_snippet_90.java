// Definerer en klasse
public class Bil {
    String merke;
    int år;

    // Konstruktør
    public Bil(String merke, int år) {
        this.merke = merke;
        this.år = år;
    }

    // Metode
    void kjør() {
        System.out.println("Bilen kjører");
    }
}

// Oppretter et objekt
public class Main {
    public static void main(String[] args) {
        Bil minBil = new Bil("Toyota", 2020); // Oppretter et objekt av klassen Bil
        minBil.kjør(); // Kaller kjør-metoden på objektet
    }
}