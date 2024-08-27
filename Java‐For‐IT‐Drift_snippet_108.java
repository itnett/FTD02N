public class StringExample {
    public static void main(String[] args) {
        String tekst = "Hei, verden!";

        // Få lengden av strengen
        int lengde = tekst.length();
        System.out.println("Lengde: " + lengde);

        // Konverter til store bokstaver
        String storTekst = tekst.toUpperCase();
        System.out.println("Store bokstaver: " + storTekst);

        // Erstatt tekst
        String erstattetTekst = tekst.replace("verden", "Java");
        System.out.println("Erstattet tekst: " + erstattetTekst);
    }
}