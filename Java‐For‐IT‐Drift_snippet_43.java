import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;

public class CollectionExample {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Java");
        list.add("Python");

        HashSet<String> set = new HashSet<>(list);

        HashMap<String, Integer> map = new HashMap<>();
        map.put("Java", 1);
        map.put("Python", 2);

        System.out.println("List: " + list);
        System.out.println("Set: " + set);
        System.out.println("Map: " + map);
    }
}