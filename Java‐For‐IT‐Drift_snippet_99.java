public class TekstManipulering {
    public static void main(String[] args) {
        String tekst = "Hei, verden!";
        String storTekst = tekst.toUpperCase(); // Til store bokstaver
        String litenTekst = tekst.toLowerCase(); // Til små bokstaver
        String erstattetTekst = tekst.replace("verden", "Java"); // Erstatt tekst

        System.out.println(storTekst); // HEI, VERDEN!
        System.out.println(litenTekst); // hei, verden!
        System.out.println(erstattetTekst); // Hei, Java!
    }
}