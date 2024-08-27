import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class ServerMonitor {
    public static void main(String[] args) {
        try {
            URL url = new URL("http://your-server-url");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");

            int responseCode = connection.getResponseCode();
            if (responseCode == 200) {
                System.out.println("Server is up");
            } else {
               

 System.out.println("Server is down");
            }
        } catch (IOException e) {
            System.out.println("Error checking server status: " + e.getMessage());
        }
    }
}