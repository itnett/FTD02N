import org.springframework.web.client.RestTemplate;

public class RestClient {
    public static void main(String[] args) {
        RestTemplate restTemplate = new RestTemplate();
        String result = restTemplate.getForObject("https://jsonplaceholder.typicode.com/posts/1", String.class);
        System.out.println(result);
    }
}