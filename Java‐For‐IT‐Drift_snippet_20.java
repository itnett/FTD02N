import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class GitHubUser {
    public static void main(String[] args) throws Exception {
        String brukernavn = "octocat"; // Erstatt med ønsket brukernavn

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.github.com/users/" + brukernavn))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() == 200) {
            System.out.println(response.body());
        } else {
            System.out.println("Feil ved henting av brukerinformasjon: " + response.statusCode());
        }
    }
}