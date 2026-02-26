import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

// javax.crypto forma parte de la biblioteca estandar
// hay que usar throws Exception - enforced by compiler

public class Aes {

  public static void main(String[] args)  throws Exception {

    String texto = "Hola, AES!";

    KeyGenerator keyGen = KeyGenerator.getInstance("AES");

    keyGen.init(128); // 128, 192, 256

    SecretKey key = keyGen.generateKey();
    
    String encodedKey = Base64.getEncoder().encodeToString(key.getEncoded()); // mostrar en hexadecimal
    System.out.println(encodedKey);


    Cipher encryptCipher = Cipher.getInstance("AES/ECB/PKCS5Padding"); // ECB, lo más sencillo - normas para cirfrar
    encryptCipher.init(Cipher.ENCRYPT_MODE, key);  // en cambio, para descifrar, decryptCipher.init(Cipher.DECRYPT_MODE, key);

    byte[] encryptedBytes = encryptCipher.doFinal(texto.getBytes());
    String encryptedBase64 = Base64.getEncoder().encodeToString(encryptedBytes);

    System.out.println("Encrypted: " + encryptedBase64);

    

    // Descifrar ****
    Cipher decryptCipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
    decryptCipher.init(Cipher.DECRYPT_MODE, key);
    byte[] decryptedBytes = decryptCipher.doFinal(Base64.getDecoder().decode(encryptedBase64));
    String decryptedText = new String(decryptedBytes);

    System.out.println("Decrypted: " + decryptedText);

  }


}
