public class Main {
    public static void main(String[] args) {
        try {
            int[] tall = {1, 2, 3};
            System.out.println(tall[10]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Feil: Indeksen er utenfor rekkevidde");
        } finally {
            System.out.println("Denne blokken kjøres alltid");
        }
    }
}