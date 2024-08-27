class Bil {
    void kjør() {
        System.out.println("Bilen kjører");
    }
}

class Sportsbil extends Bil {
    @Override
    void kjør() {
        System.out.println("Sportsbilen kjører raskt");
    }
}

public class Main {
    public static void main(String[] args) {
        Bil minBil = new Sportsbil(); // Polymorfisme
        minBil.kjør(); // Utskrift: Sportsbilen kjører raskt
    }
}