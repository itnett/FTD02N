class Dyr {
    void lyd() {
        System.out.println("Dyret lager en lyd");
    }
}

class Hund extends Dyr {
    @Override
    void lyd() {
        System.out.println("Hunden bjeffer");
    }
}

class Katt extends Dyr {
    @Override
    void lyd() {
        System.out.println("Katten mjauer");
    }
}

public class Main {
    public static void main(String[] args) {
        Dyr mittDyr = new Hund();
        mittDyr.lyd(); // Output: Hunden bjeffer

        mittDyr = new Katt();
        mittDyr.lyd(); // Output: Katten mjauer
    }
}