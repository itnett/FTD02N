// Definerer en klasse
public class Bil {
    // Variabler (eller felt)
    String merke;
    int år;

    // Konstruktør
    public Bil(String merke, int år) {
        this.merke = merke;
        this.år = år;
    }

    // Metode
    void kjør() {
        System.out.println(merke + " fra " + år + " kjører.");
    }
}

// Hovedprogram for å opprette et objekt
public class Main {
    public static void main(String[] args) {
        // Oppretter et objekt av klassen Bil
        Bil minBil = new Bil("Toyota", 2020);
        minBil.kjør(); // Kaller kjør-metoden på objektet
    }
}