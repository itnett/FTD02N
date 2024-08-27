public class Person {
    private String navn;
    private int alder;

    public Person(String navn, int alder) {
        this.navn = navn;
        this.alder = alder;
    }

    public String getNavn() {
        return navn;
    }

    public int getAlder() {
        return alder;
    }

    public void setAlder(int alder) {
        if (alder > 0) {
            this.alder = alder;
        }
    }
}