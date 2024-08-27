import com.google.cloud.storage.BlobId;
   import com.google.cloud.storage.BlobInfo;
   import com.google.cloud.storage.Storage;
   import com.google.cloud.storage.StorageOptions;
   import java.nio.file.Files;
   import java.nio.file.Paths;

   public class GCPStorageExample {
       public static void main(String[] args) throws Exception {
           Storage storage = StorageOptions.getDefaultInstance().getService();
           BlobId blobId = BlobId.of("my-bucket", "myfile.txt");
           BlobInfo blobInfo = BlobInfo.newBuilder(blobId).build();
           storage.create(blobInfo, Files.readAllBytes(Paths.get("myfile.txt")));

           System.out.println("File uploaded to GCP Cloud Storage.");
       }
   }