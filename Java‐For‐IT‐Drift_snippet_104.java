import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> liste = new ArrayList<>();
        liste.add("Eple");
        liste.add("Banan");
        liste.add("Appelsin");

        for (String frukt : liste) {
            System.out.println(frukt);
        }
    }
}