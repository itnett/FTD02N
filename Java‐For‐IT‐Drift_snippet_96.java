public class Main {
    // Metode som returnerer summen av to tall
    public static int leggTil(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int sum = leggTil(5, 3); // Kaller metoden
        System.out.println("Sum: " + sum); // Utskrift: Sum: 8
    }
}