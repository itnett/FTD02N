import java.util.Scanner;

public class ScannerExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Lese en linje med tekst fra brukeren
        System.out.println("Skriv inn ditt navn:");
        String navn = scanner.nextLine();
        System.out.println("Hei, " + navn + "!");

        // Lese et tall fra brukeren
        System.out.println("Skriv inn din alder:");
        int alder = scanner.nextInt();
        System.out.println("Du er " + alder + " år gammel.");

        scanner.close();
    }
}