import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class AESEncryption {
    public static void main(String[] args) throws Exception {
        String originalText = "Hemmelig melding";
        String secretKey = "1234567890123456"; // 16 bytes nøkkel

        SecretKeySpec keySpec = new SecretKeySpec(secretKey.getBytes(), "AES");
        Cipher cipher = Cipher.getInstance("AES");

        // Kryptering
        cipher.init(Cipher.ENCRYPT_MODE, keySpec);
        byte[] encryptedBytes = cipher.doFinal(originalText.getBytes());
        String encryptedText = bytesToHex(encryptedBytes);
        System.out.println("Kryptert tekst: " + encryptedText);

        // Dekryptering
        cipher.init(Cipher.DECRYPT_MODE, keySpec);
        byte[] decryptedBytes = cipher.doFinal(hexToBytes(encryptedText));
        String decryptedText = new String(decryptedBytes);
        System.out.println("Dekryptert tekst: " + decryptedText);
    }

    // ... (hjelpemetoder for konvertering mellom bytes og hex-strenger)
}