public class Person {
    private String name;
    private int age;

    // Offentlig metode for å få tilgang til navnet
    public String getName() {
        return name;
    }

    // Offentlig metode for å sette navnet med validering
    public void setName(String name) {
        if (name != null && !name.isEmpty()) {
            this.name = name;
        }
    }
}