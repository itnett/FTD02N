import java.util.Scanner;

public class Eksempel {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Skriv inn navnet ditt: ");
        String navn = scanner.nextLine();
        System.out.println("Hei, " + navn + "!");
    }
}