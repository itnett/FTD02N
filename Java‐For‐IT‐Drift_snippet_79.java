import com.azure.storage.blob.BlobClientBuilder;

   public class AzureBlobExample {
       public static void main(String[] args) {
           BlobClientBuilder clientBuilder = new BlobClientBuilder()
                   .connectionString("DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;EndpointSuffix=core.windows.net")
                   .containerName("my-container")
                   .blobName("myfile.txt");

           clientBuilder.buildClient().uploadFromFile("myfile.txt");

           System.out.println("File uploaded to Azure Blob Storage.");
       }
   }