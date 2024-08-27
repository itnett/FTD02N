public class StringExample {
    public static void main(String[] args) {
        String tekst = "Hei, verden!";
        System.out.println("Lengde: " + tekst.length());
        System.out.println("Store bokstaver: " + tekst.toUpperCase());
        System.out.println("Erstattet tekst: " + tekst.replace("verden", "Java"));
    }
}