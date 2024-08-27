public class MathExample {
    public static void main(String[] args) {
        double a = 16;
        double b = 9;

        // Finn kvadratroten av et tall
        double sqrtA = Math.sqrt(a);
        System.out.println("Kvadratrot av " + a + " er " + sqrtA);

        // Finn maksimum av to tall
        double max = Math.max(a, b);
        System.out.println("Maksimum av " + a + " og " + b + " er " + max);

        // Finn minimum av to tall
        double min = Math.min(a, b);
        System.out.println("Minimum av " + a + " og " + b + " er " + min);
    }
}