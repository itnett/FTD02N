public void skrivHilsen(String navn) {
    System.out.println("Hei, " + navn + "!");
}

// Kalle metoden
public class Main {
    public static void main(String[] args) {
        skrivHilsen("Ola"); // Output: Hei, Ola!
    }
}