import java.security.MessageDigest;

public class HashingExample {
    public static void main(String[] args) throws Exception {
        String data = "Hello, World!";
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hash = md.digest(data.getBytes());

        StringBuilder hexString = new StringBuilder();
        for (byte b : hash) {
            hexString.append(Integer.toHexString(0xff & b));
        }

        System.out.println("Hashed Data: " + hexString.toString());
    }
}