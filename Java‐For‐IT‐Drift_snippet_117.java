// Superklasse
class Bil {
    String merke;
    String modell;

    public Bil(String merke, String modell) {
        this.merke = merke;
        this.modell = modell;
    }

    public void start() {
        System.out.println("Bilen starter.");
    }
}

// Underklasse
class Elbil extends Bil {
    int batterikapasitet;

    public Elbil(String merke, String modell, int batterikapasitet) {
        super(merke, modell);
        this.batterikapasitet = batterikapasitet;
    }

    public void lade() {
        System.out.println("Elbilen lader.");
    }
}

public class Main {
    public static void main(String[] args) {
        Elbil minElbil = new Elbil("Tesla", "Model 3", 75);
        minElbil.start(); // Output: Bilen starter.
        minElbil.lade(); // Output: Elbilen lader.
    }
}