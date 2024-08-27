import java.io.File;
   import java.io.IOException;
   import java.nio.file.Files;
   import java.nio.file.StandardCopyOption;

   public class BackupFiles {
       public static void main(String[] args) {
           File source = new File("/data");
           File backup = new File("/backup/data");

           try {
               Files.walk(source.toPath())
                       .forEach(path -> {
                           File dest = new File(backup, path.toString().substring(source.toString().length()));
                           try {
                               if (Files.isDirectory(path)) {
                                   dest.mkdirs();
                               } else {
                                   Files.copy(path, dest.toPath(), StandardCopyOption.REPLACE_EXISTING);
                               }
                           } catch (IOException e) {
                               e.printStackTrace();
                           }
                       });
               System.out.println("Sikkerhetskopiering fullført.");
           } catch (IOException e) {
               e.printStackTrace();
           }
       }
   }