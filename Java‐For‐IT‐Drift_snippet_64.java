import java.io.File;
   import java.io.IOException;
   import java.nio.file.Files;
   import java.nio.file.StandardCopyOption;

   public class DeployApp {
       public static void main(String[] args) {
           File source = new File("build/myapp.jar");
           File destination = new File("/deployments/myapp.jar");

           try {
               Files.copy(source.toPath(), destination.toPath(), StandardCopyOption.REPLACE_EXISTING);
               Runtime.getRuntime().exec("systemctl restart myapp.service");
               System.out.println("Applikasjonen ble deployert og restartet.");
           } catch (IOException e) {
               e.printStackTrace();
           }
       }
   }