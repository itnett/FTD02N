import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
   import software.amazon.awssdk.regions.Region;
   import software.amazon.awssdk.services.s3.S3Client;
   import software.amazon.awssdk.services.s3.model.PutObjectRequest;
   import java.nio.file.Paths;

   public class S3Example {
       public static void main(String[] args) {
           S3Client s3 = S3Client.builder()
                   .region(Region.US_EAST_1)
                   .credentialsProvider(ProfileCredentialsProvider.create())
                   .build();

           s3.putObject(PutObjectRequest.builder()
                           .bucket("my-bucket")
                           .key("myfile.txt")
                           .build(),
                   Paths.get("myfile.txt"));

           System.out.println("File uploaded to S3.");
       }
   }