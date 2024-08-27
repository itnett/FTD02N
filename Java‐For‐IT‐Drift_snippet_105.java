import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Integer> alder = new HashMap<>();
        alder.put("Alice", 30);
        alder.put("Bob", 25);

        System.out.println("Alder til Alice: " + alder.get("Alice"));
    }
}