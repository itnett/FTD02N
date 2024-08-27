import java.io.BufferedWriter;
     import java.io.FileWriter;
     import java.io.IOException;

     public class FileWriteExample {
         public static void main(String[] args) {
             try (BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"))) {
                 bw.write("Hello, World!");
             } catch (IOException e) {
                 e.printStackTrace();
             }
         }
     }