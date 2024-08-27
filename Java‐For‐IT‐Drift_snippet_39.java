import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import java.nio.file.Paths;

public class S3Example {
    public static void main(String[] args) {
        S3Client s3 = S3Client.builder().build();

        PutObjectRequest request = PutObjectRequest.builder()
                .bucket("my-bucket")
                .key("myfile.txt")
                .build();

        s3.putObject(request, Paths.get("myfile.txt"));
    }
}