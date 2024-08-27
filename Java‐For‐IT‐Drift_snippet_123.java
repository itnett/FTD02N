public int beregnSum(int a, int b) {
    int sum = a + b;
    return sum;
}

// Kalle metoden
public class Main {
    public static void main(String[] args) {
        int resultat = beregnSum(5, 3);
        System.out.println(resultat); // Output: 8
    }
}