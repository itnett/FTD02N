import java.util.HashSet;
import java.util.Set;

Set<Integer> tall = new HashSet<>();
tall.add(5);
tall.add(3);
tall.add(8);
tall.add(5); // Duplikat, blir ignorert

System.out.println(tall); // Skriver ut: [8, 3, 5] (Rekkefølgen kan variere)