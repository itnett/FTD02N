import java.io.FileInputStream;
   import java.io.IOException;
   import java.util.Properties;

   public class ConfigManager {
       public static void main(String[] args) {
           Properties properties = new Properties();

           try (FileInputStream input = new FileInputStream("config.properties")) {
               properties.load(input);
           } catch (IOException e) {
               e.printStackTrace();
           }

           String dbHost = properties.getProperty("db.host");
           String dbPort = properties.getProperty("db.port");

           System.out.println("Database Host: " + dbHost);
           System.out.println("Database Port: " + dbPort);
       }
   }