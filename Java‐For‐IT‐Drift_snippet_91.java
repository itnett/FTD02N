// Superklasse
class Bil {
    void kjør() {
        System.out.println("Bilen kjører");
    }
}

// Underklasse som arver fra Bil
class Sportsbil extends Bil {
    void turbo() {
        System.out.println("Sportsbilen bruker turbo");
    }
}

// Bruk av arv
public class Main {
    public static void main(String[] args) {
        Sportsbil minBil = new Sportsbil();
        minBil.kjør(); // Arvet metode
        minBil.turbo(); // Egen metode
    }
}