public class Lydbok extends Bok {
    private int spilletid; // Spilletid i minutter

    public Lydbok(String tittel, String forfatter, int spilletid) {
        super(tittel, forfatter);
        this.spilletid = spilletid;
    }

    @Override
    public void visInfo() {
        super.visInfo();
        System.out.println("Spilletid: " + spilletid + " minutter");
    }
}