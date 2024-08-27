class Person {
    // Egenskaper (variabler)
    String navn;
    int alder;

    // Konstruktør
    public Person(String navn, int alder) {
        this.navn = navn;
        this.alder = alder;
    }

    // Metoder
    public void hils() {
        System.out.println("Hei, jeg heter " + navn + " og er " + alder + " år gammel.");
    }
}