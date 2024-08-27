public class Bibliotek {
    public static void main(String[] args) {
        Bok bok1 = new Bok("Java for Beginners", "John Doe");
        Lydbok lydbok1 = new Lydbok("Learn Java in 24 Hours", "Jane Doe", 300);

        bok1.visInfo();
        lydbok1.visInfo();
    }
}