public class Main {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Feil: Kan ikke dele med null");
        } finally {
            System.out.println("Denne blokken kjøres alltid");
        }
    }
}