import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FileExample {
    public static void main(String[] args) {
        // Skrive til en fil
        try {
            FileWriter writer = new FileWriter("example.txt");
            writer.write("Hei, verden!");
            writer.close();
            System.out.println("Vellykket skriving til fil.");
        } catch (IOException e) {
            System.out.println("En feil oppstod.");
            e.printStackTrace();
        }

        // Lese fra en fil
        try {
            File file = new File("example.txt");
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                String data = scanner.nextLine();
                System.out.println(data);
            }
            scanner.close();
        } catch (IOException e) {
            System.out.println("En feil oppstod.");
            e.printStackTrace();
        }
    }
}