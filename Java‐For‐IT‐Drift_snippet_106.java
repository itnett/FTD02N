public class Main {
    public static void main(String[] args) {
        try {
            int resultat = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Feil: Kan ikke dele med null");
        }
    }
}