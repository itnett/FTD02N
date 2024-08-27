import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class EncryptionExample {
    public static void main(String[] args) throws Exception {
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(256);
        SecretKey secretKey = keyGen.generateKey();

        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);

        String plainText = "Hello, World!";
        byte[] encryptedText = cipher.doFinal(plainText.getBytes());
        String encryptedString = Base64.getEncoder().encodeToString(encryptedText);

        System.out.println("Encrypted Text: " + encryptedString);
    }
}