import com.jcraft.jsch.JSch;
import com.jcraft.jsch.Session;

public class SSHExample {
    public static void main(String[] args) {
        String host = "example.com";
        String user = "username";
        String password = "password";

        try {
            JSch jsch = new JSch();
            Session session = jsch.getSession(user, host, 22);
            session.setPassword(password);
            session.setConfig("StrictHostKeyChecking", "no");
            session.connect();
            System.out.println("Connected to the server.");
            session.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}