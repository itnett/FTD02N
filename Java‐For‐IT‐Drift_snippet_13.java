class Dyr {
    String navn;

    public Dyr(String navn) {
        this.navn = navn;
    }

    public void lagLyd() {
        System.out.println("Dyr lager en lyd.");
    }
}

class Hund extends Dyr {
    public Hund(String navn) {
        super(navn); // Kaller konstruktøren til overklassen
    }

    @Override
    public void lagLyd() {
        System.out.println("Voff!");
    }
}

class Katt extends Dyr {
    public Katt(String navn) {
        super(navn);
    }

    @Override
    public void lagLyd() {
        System.out.println("Mjau!");
    }
}