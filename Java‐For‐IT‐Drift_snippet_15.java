import java.util.ArrayList;
import java.util.List;

List<String> navn = new ArrayList<>();
navn.add("Ola");
navn.add("Kari");
navn.add("Per");

System.out.println(navn); // Skriver ut: [Ola, Kari, Per]

for (String n : navn) {
    System.out.println(n); // Skriver ut hvert navn på en ny linje
}

navn.remove("Kari");
System.out.println(navn); // Skriver ut: [Ola, Per]