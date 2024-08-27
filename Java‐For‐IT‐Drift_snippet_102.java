// Superklasse
class Dyr {
    void lyd() {
        System.out.println("Dyret lager en lyd");
    }
}

// Underklasse som arver fra Dyr
class Hund extends Dyr {
    @Override
    void lyd() {
        System.out.println("Hunden bjeffer");
    }
}

// Hovedprogram for å demonstrere arv
public class Main {
    public static void main(String[] args) {
        Hund minHund = new Hund();
        minHund.lyd(); // Kaller lyd-metoden, output: Hunden bjeffer
    }
}