import java.util.Scanner;

public class TekstSpill {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hva heter du?");
        String navn = scanner.nextLine();

        System.out.println("Velkommen, " + navn + "!");

        System.out.println("Velg en retning: (nord, sør, øst, vest)");
        String retning = scanner.nextLine();

        if (retning.equals("nord")) {
            System.out.println("Du gikk nord og fant en skatt!");
        } else {
            System.out.println("Du gikk feil vei og møtte en fiende!");
        }

        scanner.close();
    }
}