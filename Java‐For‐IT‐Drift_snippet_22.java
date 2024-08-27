import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.CreateBucketRequest;

public class CreateS3Bucket {
    public static void main(String[] args) {
        String bucketName = "my-java-bucket"; // Erstatt med ønsket navn

        S3Client s3 = S3Client.builder()
                .region(Region.EU_WEST_1)
                .build();

        CreateBucketRequest createBucketRequest = CreateBucketRequest.builder()
                .bucket(bucketName)
                .build();

        s3.createBucket(createBucketRequest);

        System.out.println("S3-bøtte opprettet: " + bucketName);
    }
}