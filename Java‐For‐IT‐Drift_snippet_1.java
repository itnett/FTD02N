class Bil {
    // Egenskaper
    String merke;
    String modell;
    String farge;

    // Konstruktør
    public Bil(String merke, String modell, String farge) {
        this.merke = merke;
        this.modell = modell;
        this.farge = farge;
    }

    // Metoder
    public void start() {
        System.out.println("Bilen starter.");
    }

    public void stopp() {
        System.out.println("Bilen stopper.");
    }

    public void akselerere() {
        System.out.println("Bilen akselererer.");
    }
}